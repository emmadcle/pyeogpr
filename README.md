

# pyeogpr [![GitHub](https://img.shields.io/badge/GitHub-pyeogpr-purple.svg)](https://github.com/daviddkovacs/pyeogpr)   [![Documentation](https://img.shields.io/badge/docs-pyeogpr-blue.svg)](https://pyeogpr.readthedocs.io/en/latest/pyeogpr.html)


Python based machine learning library to use Earth Observation data to retrieve biophysical maps using Gaussian Process Regression.

## Features

- Access to openEO is required. Works best with the Copernicus Data Space Ecosystem. Register [here](https://documentation.dataspace.copernicus.eu/Registration.html) or [here](https://docs.openeo.cloud/join/free_trial.html)
 - The package uses satellite observations and machine learning to infer biophyiscal maps.
- Get your maps in a few lines of code: select your region, temporal domain and satellite sensor to get the maps you are looking for!	
- Built in gap filling to avoid cloud cover
- Runs "in the cloud" with the openEO API. No local processing needed.
- Resulting maps in .tiff or netCDF format

## Available biophysical variables

This package currently features the following satellite sensors and biophysical variables for mapping:

## **- Sentinel 2 MultiSpectral Instrument (MSI)**

 - **Top of atmosphere: Level 1C** 
 [![DOI](https://img.shields.io/badge/DOI-j.rse.2022.112958/Estévez_et_al_2022-doi.svg)](https://doi.org/10.1016/j.rse.2022.112958)
 
	 Leaf variables:
	 - _Cab_: Leaf chlorophyll content
	 - _Cm_: Leaf dry matter content
	 - _Cw_: Leaf water content
	 	 
	Canopy variables
	 - 	 _FVC_: Fractional Vegetation Cover
	 - _LAI_: Leaf Area Index
	 - _laiCab_ Canopy chlorophyll content
	 - _laiCm_: Leaf dry matter content
	 - _laiCw_ Canopy water content

- **Bottom of atmosphere: Level 2A** 
[![DOI](https://img.shields.io/badge/DOI-/De_Clerck_et_al_2024_(under_review)-doi.svg)](https://doi.org/)    [![DOI](https://img.shields.io/badge/DOI-rs14010146/Salinero_et_al_2021-doi.svg)](https://doi.org/10.3390/rs14010146)

	 Leaf variables:
  	 - _Cab_: Leaf chlorophyll content
	 - _Cm_: Leaf dry matter content
	 - _Cw_: Leaf water content

  	Canopy variables:
	 -  _CNC_Cab_: Canopy Nitrogen Content (via chlorophyl-nitrogen relationship)
	 - 	 _CNC_Cprot_: Canopy Nitrogen Content (via protein content
	 - _FVC_: Fractional Vegetation Cover
	 - _LAI_: Leaf Area Index
	 - _laiCab_ Canopy chlorophyll content
	 - _laiCm_: Leaf dry matter content
	 - _laiCw_ Canopy water content

## **- Sentinel 3 Ocean and Land Colour Instrument (OLCI)**

 - **Top of atmosphere: Level 1B**
 [![DOI](https://img.shields.io/badge/DOI-rs14061347/ReyesMuñoz_et_al_2022-doi.svg)](https://doi.org/10.3390/rs14061347)
  [![DOI](https://img.shields.io/badge/DOI-rs15133404/D.Kovács_et_al_2023-doi.svg)](https://doi.org/10.3390/rs15133404)
 
	 - _FAPAR_: Fraction of Absorbed Photosynthetically Active Radiation
	 - _FVC_ Fractional Vegetation Cover
	 - _LAI_: Leaf Area Index
	 - _LCC_ Leaf Chlorophyll Content

## 
Supported by the European Research Council (ERC) under the ERC-2017-STG SENTIFLEX project.

![erc](https://github.com/user-attachments/assets/940bf34f-04d3-4fb0-9d68-8d6f19c14bab)
