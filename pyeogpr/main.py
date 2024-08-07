import openeo
import numpy as np
import scipy
import scipy.signal
from pyeogpr.sensors import sensors_dict
from pyeogpr.udfgpr import udf_gpr
from pyeogpr.udfsgolay import udf_sgolay

class Datacube:
    """
    

    Attributes
    ----------
        sensor : SENTINEL2_L1C, SENTINEL2_L2A, SENTINEL3_OLCI_L1B
            Satellite's sensor to process the data with.
                    
        biovar : Biophysical variable to process. The selected variable's map will be retrieved.
    
            Currently "built-in" variables available for each sensor:
            
            - SENTINEL2_L1C: Cab, Cm, Cw, FVC, LAI, laiCab, laiCm, laiCw
            - SENTINEL2_L2A: Cab, Cm, Cw, FVC, LAI, laiCab, laiCm, laiCw, CNC_Cab, CNC_Cprot
            - SENTINEL3_OLCI_L1B: FAPAR, FVC, LAI, LCC
            
        bounding_box : list
            Your region of interest. Insert bbox as list. Can be selected from https://geojson.io/
            (e.g.: [-4.55, 42.73,-4.48, 42.77])
    
        temporal_extent : list
            Your temporal extent to be processed. (e.g.: ["2021-01-01", "2021-12-31"])
    
        cloudmask : Boolean
            If "True" the Sentinel 2 cloud mask will be applied (only to S2 data), with Gaussian convolution to have
            smoother edges when masking.


    """
    def __init__(self,sensor:str, biovar: str, bounding_box: list, temporal_extent: list, cloudmask = False):
        
        self.connection = openeo.connect("https://openeo.dataspace.copernicus.eu").authenticate_oidc()
        print("""\n\n""")
        self.sensor = sensor
        self.biovar = biovar
        self.bounding_box = bounding_box
        self.temporal_extent = temporal_extent
        self.cloudmask = cloudmask
        self.spatial_extent = {"west": self.bounding_box[0], "south": self.bounding_box[1], "east": self.bounding_box[2], "north": self.bounding_box[3]}
        self.sensors_dict = sensors_dict  
        self.bands = None
        self.scale_factor = None
        self.data = None
        self.masked_data = None
        self.gpr_cube = None
        self.gpr_cube_gapfilled = None

        
    def construct_datacube(self, composite=None):
        """
        

        Parameters
        ----------
        composite : "hour","day","dekad","week","season","month","year"
            Compositing temporal interval. The resulting maps will have the following temporal steps. 
            For more information: https://processes.openeo.org/#aggregate_temporal_period
        


        Returns
        -------
        Datacube object containing user defined parameters and temporal compositing. This will be processed into an openEO datacube.

        """
        if self.sensor not in self.sensors_dict.keys():
            raise Exception("Sensor/satellite not available.")
                
        data = self.connection.load_collection(self.sensor,
                                               self.spatial_extent,
                                               self.temporal_extent,
                                               self.sensors_dict[self.sensor]["bandlist"]) * self.sensors_dict[self.sensor]["scale_factor"]
        self.data = data
        print(self.data)
        if self.cloudmask == True and "SENTINEL2" in self.sensor:

            s2_cloudmask = self.connection.load_collection("SENTINEL2_L2A",self.spatial_extent, self.temporal_extent, ["SCL"])
            scl = s2_cloudmask.band("SCL")
            mask = ~((scl == 4) | (scl == 5))
            
            #Gaussian convolution to have a smooth edged cloud mask
            g = scipy.signal.windows.gaussian(11, std=1.6)
            kernel = np.outer(g, g)
            kernel = kernel / kernel.sum()
            mask = mask.apply_kernel(kernel)
            mask = mask > 0.1

            if composite != None:
                
                self.masked_data = self.data.aggregate_temporal_period(composite,"mean").mask(mask)
                print(f"Cloud masked, temporally composited datacube constructed: {composite} by mean values.")
                
            elif composite == None:
                
                self.masked_data = self.data.mask(mask)
                print("Cloud masked, datacube constructed")
                
        elif self.cloudmask == False and "SENTINEL2" in self.sensor:
            
            if composite != None:
                
                self.masked_data = self.data.aggregate_temporal_period(composite,"mean")
                print(f"Temporally composited datacube constructed: {composite} by mean values. ")
                
            elif composite == None:
                
                self.masked_data = self.data
                print("Datacube constructed")

        else:
            print(f"{self.sensor} can't be masked")
    
    def process_map(self, gapfill = False):
        """
        

        Parameters
        ----------
       
        gapfill : type, e.g. "Sgolay"
            To apply Savitzy Golay interpolator for cloud-induced gap filling

        Returns
        -------
        Starts the openEO based GPR processing of the biophysical maps. You will need to open the openEO
        Web Editor to download your maps.

        """
        if self.biovar not in self.sensors_dict[self.sensor]["sensor_biovar"]:
            raise Exception(f"'{self.biovar}' not available for this satellite/sensor. Please select from: " +  str(self.sensors_dict[self.sensor]["sensor_biovar"]))
        
        print(f"Processing {self.sensor} based {self.biovar}")
        
        context = {"sensor": self.sensor,"biovar":self.biovar}
        
        self.gpr_cube = self.masked_data.apply_dimension(process=udf_gpr,
                                                         dimension="bands",
                                                         context =context).filter_bands(bands = ["B02"])
                   
        if gapfill == False:
            

            self.gpr_cube.execute_batch(title=f"{self.sensor}_{self.biovar}",outputfile=f"{self.sensor}_{self.biovar}.nc",
                                        job_options = {'executor-memory': '10g','udf-dependency-archives': 
                                                       ['https://github.com/daviddkovacs/pyeogpr/raw/main/models/GPR_models_bulk.zip#tmp/venv']})
            print("""Click the download icon next to the batch job on: https://openeo.dataspace.copernicus.eu/""")

        elif gapfill == "Sgolay":
            print("Smoother: Savitzky-Golay")
            self.gpr_cube_gapfilled = self.gpr_cube.apply_dimension(process=udf_sgolay, dimension="t")

            self.gpr_cube_gapfilled.execute_batch(title=f"{self.sensor} {self.biovar} {gapfill}", outputfile=f"{self.sensor}_{self.biovar}_GF.nc",
                                                  job_options={'executor-memory': '10g', 'udf-dependency-archives': 
                                                                ['https://github.com/daviddkovacs/pyeogpr/raw/main/models/GPR_models_bulk.zip#tmp/venv']})
            print("""Click the download icon next to the batch job on: https://openeo.dataspace.copernicus.eu/""")

        else:
            raise Exception(f"'{gapfill}' is not a valid smoother")
   
