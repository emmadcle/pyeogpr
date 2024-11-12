import ee
ee.Initialize()

X_train_GREEN = ee.Array([[-0.452896161308052,-0.626428765500269,-0.593480766265231,-0.510830578952977,-0.319509527415989,-0.00878150307219396,-0.131771883822435,-0.389303348554622,-0.695263645077721,-1.00872830047004],[2.84472248464159,1.51385662935936,2.15843073898485,1.48882550256119,-0.284589014170228,-1.04042910552281,-1.16741180566023,-0.786758805253509,2.26324061613578,2.33099578911967],[0.457440779075316,0.0727823127460218,0.218055041209813,0.307221997168543,-0.0147033332279903,-0.359699997000407,-0.131668896558927,-0.11574069763524,0.433376174100213,0.437476803611897],[0.229700271902274,0.170206955155186,-0.479271662219973,-0.124730926071477,0.993002906149681,1.58669003005082,1.3385772772832,1.11299880705294,0.329873573860181,-0.285574110131786],[0.133668186535416,-0.177799127963431,-0.248575703344883,-0.716124740225728,-1.74439118396177,-1.83004645695584,-1.97102142281421,-1.906175135105,-0.0235954972355568,-0.0486117014854278],[-0.477112545419366,-0.689269614744852,-0.326608765517523,-0.893843954021884,-0.45707140638054,0.00938345077776228,0.237540443117735,0.382479549290563,-0.110177290217665,-0.395506307460218],[-0.38517826118798,0.0897365463940232,-0.200180198439736,0.487989697620404,0.323651496899686,0.0875231963893081,0.221165468219941,0.462357805648402,-1.17300176168458,-0.886024230946767],[-0.508413263697089,-0.81296087909505,-0.448468432492139,-0.53912355841046,0.0651149827623205,-0.1498389659294,-0.0912978892637385,0.06143824089318,-0.563852700399293,-0.673526900035713],[0.825293673095085,-0.00551994454233609,0.159744621124763,0.0617054479137166,-0.258024480879703,-0.70666076355349,-0.616120984101191,-0.523486592972062,1.31996054919238,1.08421778914743],[-0.0395970320965902,-0.0414366177106911,-0.152521612906068,-0.507731704088088,0.331508612379982,0.195599597787095,0.348354738652487,0.552526500644176,0.717294134843572,0.481197228645437],[-0.901651688479818,-0.726092646315773,-0.261250716534326,-0.709914393443653,0.192824288346817,0.760945731296081
,0.589653897052046,0.435358139915203,-0.912377379763819,-0.875042486391098],[-0.0697633308509335,-0.401367533929736,-0.621966049606412,-0.744090196323507,1.08915903369426,2.04903377161731,1.49130738906576,1.02914701498342,-0.356517873803814,-0.527470844963033],[-0.718730013047783,-0.438954750036154,-0.324880354628054,-0.00984580912924968,-0.467298128116798,-0.833815440503187,-0.637027398593343,-0.336730414523188,-0.664059039485185,-0.70934092799626],[-0.465120110457932,0.717327539104208,-0.000421454632747905,0.182007297343352,0.472313110431639,0.184639737363657,-0.123635890005293,-0.424555742304383,-0.722842363400702,-0.547552405017809],[-0.470329179697937,0.0470843862732653,0.0755750303678044,0.223325628875206,1.71199133065615,1.79908806584947,1.71993911405382,1.74316081671267,-0.680320594512281,-0.883947223878245],[0.0859531122969655,-0.0125042357621103,-0.387317523193388,-0.675247305524244,-0.289702375038357,-0.774855450632657,-0.473380636878917,-0.449517697416207,-0.930177189996182,-0.53745424910455],[0.774545762988009,0.731722643144963,1.03188199800346,0.426264141368549,-1.11420063599452,-1.32589287747771,-1.33105856737466,-1.31554471149991,0.636425861195309,1.21985438334597],[0.0880830428306567,0.386862156835253,0.761901537361509,0.514065595873738,-1.06456362073804,-1.96460918771027,-1.77987706174311,-1.48548977732246,0.628295083681761,0.838763749392195],[-0.495008592186141,-1.14227109869407,-0.777780281511987,-1.033595652197,-0.730199706409884,-0.364368085699279,-0.420136221645211,-0.519207400667179,-0.75360746750602,-0.72261770798676],[-0.646279962915902,-0.421325190519574,-0.44652564505824,-0.596641699195352,-0.337219216276339,-0.47356076917723,-0.487489891979531,-0.553848481230526,0.912762421284143,0.405575811067738],[1.97723882053933,1.02708885198121,1.53070941982478,1.06531260435969,-0.761628168331069,-1.02449671583318,-0.93249785759818,-1.02618980326489,0.844419940021617,2.17722841498596],[-0.0785145671741427,-0.287983874942055,-0.364124660792831,0.230883860252984
,1.38224191272118,0.874907983662011,1.08625848168827,0.997154958227857,-0.0955638657676389,-0.285459358360045],[-0.354896205339414,-0.384964224016628,-0.233984699789593,0.50184645514633,0.346474546628165,0.857047470379371,1.15670176992783,1.28274010181334,1.54102979726345,1.21010048274794],[-0.16889770634295,-0.0229184715249287,-0.219594674244707,-0.163277906098146,0.9755426495268,0.645562756282669,1.06885363415539,1.56261965565898,-0.640545709918978,-0.754082643798301],[-0.406755383551025,-0.306093271259994,-0.37828691125926,-0.527836599552978,0.384512962842297,0.419972295900246,0.405718644426517,0.602348525336756,-0.309930716158619,-0.258722195544257],[-0.772647352394667,-0.107796270165237,-0.224753109845062,-0.190739480104073,-0.593635556395212,-1.34791407851369,-1.45423133453039,-1.47041071872429,-1.42711053405732,-1.18968036932933],[-0.89054085954798,-1.08314454172667,-0.343678497867788,-0.951160541970035,0.00350522010729952,0.855017866597253,0.974414313518436,0.855941612166679,-0.727017627529281,-0.986030400019552],[-0.704392339357404,-0.773045565915374,-0.503348827866304,-0.146523826544071,-0.042016163230925,-0.0840798033887745,0.176057046803378,-0.00356472792863288,-1.24068499071628,-0.84477096900567],[-0.441760328843862,-0.832403155416762,-0.809810816956684,-1.13917154749227,-0.0648392129594044,0.688184435707148,1.063910245507,1.11391577683255,-0.563742825027489,-0.722227551962839],[0.245350631041135,0.0125183648420678,-0.185415013942097,0.12846982508409,0.258799115157558,0.124157544656539,-0.0753348634199777,-0.150381778198588,-0.570555098079381,-0.738568204258839],[2.50879539720834,2.13320153777953,2.34038283107009,1.56503766895379,0.598276390353848,-0.212756683175059,-0.183368502840011,-0.15863450621515,2.6724165007365,3.17384755256156],[-0.0662443151865742,0.420717308931104,-0.401064419104982,0.523639355618924,1.62518891201669,1.0173861691667,0.555874074621378,0.49924036789526,-1.01060596215723,-0.975542088082372],[-0.621484793333476,-0.768282741368556
,-0.399242218477325,-0.334471846804821,1.31876140828514,1.89975641344253,2.04661471390162,1.66562592756941,0.00815848521600314,-0.365670846807408],[-0.554716101386027,-0.227382264103812,-0.393293269369383,-0.426241372783344,0.255307063832982,0.29677534632568,0.496553410840692,0.67489102345765,0.189782474809181,-0.0618081552357094],[-0.701123359016565,-0.875588467539029,-0.767470109578291,-0.947444411542628,0.0124847806562094,0.789157223867522,1.16421984016393,1.54478968772197,0.273287757380757,-0.205362621684423],[0.909680594783174,0.525570535894634,0.454391782910226,0.187675970876686,-0.126698407851895,0.158457848574334,0.056488833870434,0.0965887491118711,0.665323083979946,1.07572615803855],[-0.639681808545228,-0.788969039027123,-0.70693285313797,-0.986583453027222,-0.550109630956746,0.0119204555054101,0.563186170330455,0.622521860488353,-0.772506031456429,-0.891211011029487],[-0.75405213277879,0.168571955683891,-0.072076814608586,0.0218987626574184,-0.449339007018978,0.103354105889829,-0.157621686962977,-0.316149537247316,0.118363483136123,-0.0800536869426201],[-0.291924346082458,-0.429393557475751,-0.659321162473397,-0.678333583336837,0.347472275578044,0.940261225446212,0.592743514957289,0.318087893655163,-0.244554869934819,-0.222116380358694],[-0.676474043372858,-0.823854951659227,-0.577322134228795,-1.02835527844174,-0.269872512159514,0.520031762358667,1.05453840452776,1.27509868698319,0.0247496663585138,-0.11493822555206],[0.0284681393061488,-0.75934355947658,-0.540636948063155,-0.651060965115354,-0.255779590742475,0.238728678157103,0.390991465744854,0.782482144266167,0.0116744971137539,-0.184248295683973],[-0.888808438875849,-1.05085330216858,-0.557063550780129,-0.987490440792556,-0.223727548227616,0.530382741647469,0.664216675831935,0.39501146961201,-0.535944355960899,-0.475029285277132],[-0.665264126368367,-0.335700979077153,-0.295269594428614,-0.300333835081856,0.019718315542831,-0.0203502446302672,-0.297169429016499,-0.493939788962148,-0.670541686421662
,-0.717109622943164],[-0.243815697723652,-0.700376948109633,-0.229536386492664,-0.0811451251262901,-0.335972055088991,-0.193779887812256,-0.11498495987061,-0.0186437865267961,0.0427692273344855,-0.237952124859032],[-0.642182161780431,-0.215759550470905,-0.195410320326161,-0.429340247648233,0.156531897794973,-0.0103037059087829,-0.0629763917990018,0.100766055885687,-0.462767358338965,-0.667686034854067],[0.252851690746743,-0.0335104246215836,-0.225342645342246,-0.201698915601851,-1.28194381569291,-1.25221826018683,-1.44897898409147,-1.69129855008117,-0.860845830387412,-0.718165339243187],[0.930563174580885,0.829289459421197,0.211998903829656,0.373104580678176,1.14902277068699,0.215591195040958,-0.0177649831189308,0.0439139295493685,0.540394786237996,1.02316984658091],[-0.206310399195612,-0.229052807041875,-0.55788086135577,-0.497162777211495,-0.780585018378767,-0.80103733942198,-0.662156290889327,-0.586757507765707,-0.918090899097664,-0.786534444846819],[8.82843819918306,7.42597917409791,7.05197732162796,6.33491152094661,3.46737070184931,2.18522018539743,2.18080711825272,1.88936655379621,4.13584657780337,4.76029079688888],[-0.899787999262838,-1.38702341085368,-0.729891241193056,-1.5105326491871,-3.7586812176485,-3.9025763590657,-4.00357805541074,-4.03527707784703,-2.0094829672338,-1.29286516247936],[3.73975633716876,3.68325212350141,4.60674486171949,4.11153179065021,2.0044506290894,0.885258962950812,0.83064409366108,1.01111327598427,4.50173156591304,4.76717590319337],[1.96172736991354,2.23130150605728,3.88054431746175,3.37838334700573,1.2449294659941,0.367709998510706,0.490786124084237,0.474176527252368,2.23280513814587,1.70904118628032],[0.00649744282274773,-0.681823258457103,-0.365665492205924,-0.923913117853145,-1.33956266254841,-0.954576865539211,-1.19377654511832,-1.17453513650087,0.0919933939029934,0.261332833988574],[0.0256436662071235,-0.981152563837905,-0.189528363888354,-0.393539425022157,-0.603737562012736,0.126288628627763,0.352165267402288,0.662766645260478
,1.7266093002416,1.19105168863884],[0.140821974958357,0.864299774186986,0.14922677191365,0.916289475694498,1.55073338913198,1.10191916669192,1.62807447500456,1.68692000356276,0.385690262736971,0.0568451767450824],[1.25560909515723,1.5364267307566,2.99892077849201,2.54823760067976,0.413072954032581,-0.340621721448497,-0.193049305609775,-0.122872684810047,2.04601700607788,1.57592913106009],[0.77838889851619,2.4539813253544,1.16546538225161,2.33307994745901,2.94268999033175,1.73272002217421,1.53765165764442,1.40765176290353,0.4027209453667,-0.15636361515077],[0.908939749380152,0.99527744922448,0.831439928961097,1.27908458182785,0.540906975735812,0.283278481174595,-0.197374770677117,-0.337545498771737,0.210219293964856,0.143827019725198],[-0.664893703666855,-1.16370380915475,-0.694813879110643,-0.97325577169774,-1.21696671783204,-1.73090031219937,-1.27111998001293,-1.0573667757719,-0.665926920805865,-0.520470986886796],[0.79019612212687,1.02637798264587,0.502264744988324,1.28374549117748,1.05049703688645,0.274449704722382,0.619623190732912,1.14101732809682,0.727292793677801,0.482459498134595],[0.861942369125879,1.61977616032591,0.493126944781981,1.16306573017895,1.7189754333053,1.04996130986969,1.22158374593796,1.29527202213479,-0.483314052866444,-0.658494417937566],[1.4662870066419,1.81544294487989,2.96676429682746,2.6729484184131,1.17009979475318,0.284496243443866,0.283781724432887,0.260216912008157,2.55364122381561,2.63049791336519],[0.0889396453279019,0.423027634270978,-0.0628184275960011,0.720279341964118,0.934760478700501,0.914383777224207,0.417459192466445,0.259911255414952,0.522155474518415,0.142794253779524],[-0.206426156289834,-0.149097778548837,0.492550807818825,0.213625898607057,-1.1452549495595,-0.642423803849454,-0.839706333177351,-0.923489187947666,0.393930915622324,0.559802192288418],[0.08183215974265,0.263970620487319,1.24505267437137,0.973606063642649,-0.277854343758546,-0.838889449958482,-0.960304418745376,-0.809581164212892,0.889029340974327
,0.964302187677481],[-0.449979082533649,-0.990056202263113,-0.65305064854881,-0.836716321858178,-0.113727931503469,0.973952648229372,0.810664564540502,0.624865227702932,1.36303169493983,1.34975338895744],[-0.705920333001139,-0.827835819937164,-0.161592420442276,-0.677300625048541,-0.650256674300839,0.112385842720254,0.020443291642587,-0.0725412324621234,0.866504889754363,1.17647821362766],[0.280679696197795,1.75946198472139,0.655651162528226,1.29344522144563,0.363435938776106,0.0147619008003755,-0.0854276152437747,-0.0570546317396851,-0.673947822947608,-0.454718221678872],[1.06433207266423,0.594169426755519,1.52427812349187,0.938586258258944,-1.50007230736018,-1.85582242498874,-1.6632954794519,-1.71727936050368,1.04560174579603,1.84467778047887],[-0.0154037994041201,0.157340220185424,0.856495187591392,0.652381230087078,-0.781707463447381,-1.33309797090423,-1.38873143493922,-1.38727212537226,0.142975566420377,0.0198951062442942],[1.0648877067165,0.523437927888596,-0.00390507347974083,0.306466174030765,-0.0431386082995385,0.704319785774987,0.67327955502065,0.807851641502266,1.24722305305767,1.13746261123552],[-0.309218455959277,-0.588379484325876,0.0754276464935084,-0.677476983780689,-2.07426531801547,-2.29918937119243,-2.47112757440971,-2.51911849001413,-0.658235644779536,-0.12079056591088],[0.269682772246672,-0.244460899885498,-0.527908340737604,-0.177512575192961,0.512596416782999,0.0158781828805404,-0.305305422833642,-0.754970519560084,0.0102461172802925,0.290479784010935],[-0.502810620336727,0.108308007779936,0.117566036008095,0.340730156276693,1.78245593774135,0.918240024410231,1.14825681432017,1.33724886093508,-1.31605949577431,-1.16635133413427],[-0.427499054835669,-0.868035480850978,-0.673403021735664,-0.843014848006326,-1.12604866727433,-0.626694374538038,-0.398508896308503,-0.396129679136223,0.0913341416721651,0.0283867373531709],[-0.331003941091922,-1.11559572688521,-0.556661594759322,-1.1393982944336,-1.13789669855414,-0.134819897941726,-0.0795573412238114
,-0.0550169211183119,-1.55595039503552,-1.17021846884196],[0.135821268487952,0.895222590274535,0.308615732697601,0.270690545509282,0.439013906729432,-0.0894582534113871,-0.487283917452515,-0.586248080110364,1.36193294122178,1.33277012673969],[-0.315122067764616,-0.184943364783658,-0.666824341528458,-0.208249382795926,1.20402257904906,1.5469097959213,1.3524805578568,1.31554724281745,1.37841424699248,0.982891974699616],[-0.040175817567702,1.3041501754323,-0.056534515137387,1.04440149754784,1.96304487766942,1.45638946723884,1.36123447525499,1.30321909355815,-1.17607827209511,-1.07494007276493],[0.0781047813086905,0.695646024376156,0.0659682814705201,0.567351127087074,0.0556365577384706,0.459245129084231,0.452989798376751,0.735818571036715,-0.38794223013996,-0.277197230794651],[-0.210639714519528,-0.654472560779667,-0.132597992808074,-0.555235188297424,-1.5348681044872,-1.77250718973279,-1.64022633242608,-1.2928242380716,0.375252102415524,0.529507724548642],[-0.160285378532807,0.342130703908608,-0.125590559512007,0.387213279250028,2.03637795548552,1.25677793526752,0.75556637856365,0.972804316302446,-0.461558729249113,-0.632675269295711],[-0.595485749971137,-1.17116793717588,-0.489454548080413,-0.877266233199958,-0.176709571464574,-0.252029516359044,-0.0833678699736122,-0.0902693148680718,-1.63146773807689,-1.17962811412477],[-0.110648736530266,0.0688903031350027,-0.246619517376956,0.309237525535951,0.333129921923535,-0.467674918209088,-0.63991104197157,-0.521754538943895,0.0669418091315205,0.216005884150651],[0.00457587505865681,-0.590743124865901,-0.614690645629807,-0.379758249810008,1.05373965597356,1.01961873332703,0.614782789348031,0.21936081404962,0.816401720211417,0.171137941399694],[-0.0663600722807965,0.678052008326343,0.0344951250413423,0.256959758506319,1.80827217431946,1.79573921960898,1.43126581444052,1.14111921362789,0.962535964711675,0.419116520133244],[-0.776999819137428,0.308719845147348,-0.337340991273067,-0.0889552975499943,0.294592641234463,0.81523763246774
,0.765659130387447,0.818651507795546,0.534131890045129,0.387904038219535],[-0.663527769955031,-0.794176156908532,-0.621738274527954,-0.580177351844092,0.131962822404205,0.609334328771862,0.776060844001769,1.11228560833546,-1.29913868851638,-1.12300958994747],[-0.246362353796543,0.167807771148394,0.301876270082073,0.617991277318188,0.004627665175913,-0.842035335820765,-0.679870100212726,-0.689865665207203,0.846727322829515,1.14446246931176],[-0.863086054968701,-0.949838769615915,-0.553539736331055,-1.14065799966323,-0.912659388118985,0.644040553446081,0.488829366077582,0.0419781044590635,-0.553524415449651,-0.8940912805002],[-0.759006536411506,-0.661545710666359,-0.526541690266861,-0.300459805604819,-0.254781861792596,-0.659573955808351,-0.686152323286723,-0.592259326443416,0.27779264762475,-0.00374375873447088],[0.684486743683024,1.0022084252441,0.696114735289451,1.67626964073009,0.675350951731992,0.507042298153112,0.36915816588113,-0.0688733533436509,0.287681431087174,0.411313399654817],[-0.578816728403119,-0.00256983680065035,-0.343557911061546,0.0222766742263074,0.69892229817288,-0.0536357466570035,-0.131977858349452,-0.0258776592326716,-0.11753894012858,-0.237263614228582],[-0.177903608273448,0.424271655607834,0.06186833005829,0.404597211418918,0.303946350139578,0.222085927143736,-0.157621686962977,-0.357005635205854,0.419422001881016,0.346019641533859],[-0.537630354278809,-0.496517394465794,-0.487337579704164,-0.655646292151206,0.0485277389705841,0.839389917474945,1.42240890977882,1.49945062639641,-0.805139016882427,-0.773934700309594],[0.615217698500373,0.142696311877297,-0.58209201234237,0.187801941399649,0.563231160989352,0.816455394737011,0.866071712307878,1.06266735470501,-0.0287596397103779,-0.534011695952303],[-0.453590703873386,-1.10203589431349,-0.384061679424852,-0.780583856825879,-0.699394825082373,0.713250042416307,0.902220241799233,0.872956495855147,-0.331466289032341,-0.349949854078812],[0.762622782283107,1.07471709744939,0.908347514275478
,0.651121524857448,0.131339241810531,-0.515675047656181,-0.708088610413955,-0.573919930851055,1.43862595074146,1.6650912577033],[-0.111621096121733,-0.194291296543457,-0.165598582116318,-0.2954209846863,-0.023184029301961,-0.28978014670644,0.0822356497474676,0.276009169323802,0.771572568515097,0.776912544423484],[-0.072009018478847,-0.316614137423114,-0.272532282184972,-0.608747466452093,-1.08464291585436,-1.12191769737485,-1.05474373938234,-1.12593573818112,0.513914821633063,0.832222898402925],[0.420745780206833,0.140314899603888,0.368922534352658,0.122045328412979,-0.38111929007101,-0.176629735853358,-0.515296453126727,-0.663579198191485,0.571379641086924,0.708176233150279],[-0.333342234395214,-0.622661158022935,-0.347309500589077,-0.294287249979634,-1.88095533397644,-2.10647849208032,-2.20016808411981,-2.33470567877983,0.0801268537480852,0.00945269501581072],[0.369650598817089,0.540676509270736,0.433315888885919,-0.0357957368596214,-0.0511204398985692,-0.0984899902418125,0.288210176763736,0.46938790729214,0.528967747570307,0.577703468680104],[0.206271036031671,0.761756872563331,0.0399885239923694,-0.0951278531751796,0.903830881254256,0.776878120985708,0.686770886540216,0.583092159964777,0.264717478379991,-0.085791275529699],[1.60519551970871,1.56486150417043,2.73362980475948,2.17284544225011,-0.17558712639596,-0.772927327039645,-0.579251543765279,-0.543659928123659,2.65252905843985,2.26788231466181],[-0.479335081628436,0.366033685309616,0.154907750341054,0.595316583184853,0.903581449016786,1.12972473850693,1.62251316277512,1.75049657494961,0.291527069100338,0.0330915599945755],[-0.790251691284002,-1.18705586682086,-0.562905311615855,-1.07913399624812,-0.822863782629885,-0.982788358110653,-0.952683361245774,-1.08120799004197,-0.735478031158243,-0.76321688482893],[1.39988873739596,1.10101926285719,1.05251574040488,0.59178940854189,-0.0703267221837382,-0.361932561160737,-0.311381671380622,-0.130921641764472,0.273397632752562,1.12151211496344],[-0.609469206953196
,0.0333112929009371,-0.706039170918377,-0.219586729862593,-0.207639168910819,-0.168511320724886,-0.163800922773465,-0.0332134174696159,-1.47548866026293,-1.15960392995586],[-0.664754795153788,-0.673079565632347,-0.717482858830748,-1.31086937029079,-1.22569684614348,-0.156333698032177,-0.178013165137587,-0.151910061164618,-0.698120404744644,-0.631344148743509],[0.338280426282834,0.154710003644644,-0.0466195999574842,0.148121226666313,0.442630674172742,-0.0639867259458053,0.214574283355421,0.236783239862363,1.23282937935125,1.20000232683468],[-0.525869433505818,0.0552949270965111,-0.450183444847582,0.117384419063349,0.2349783364792,0.308445568072859,-0.0144693906866706,-0.0448283680114448,-1.31408173908182,-0.956826074111321],[0.0602318859607603,0.0215819488677288,-0.37539282790945,-0.732601684629284,-1.14201233047239,-1.16159645131525,-1.08131445336743,-0.955175588110023,-0.437825648939296,0.0483535456362054],[-0.677363057856486,-0.251160843371134,-0.564017389940088,-0.0530536985055481,0.918173234908765,1.82658919709717,1.50119416636254,1.48966961541381,0.0310125625513819,-0.587853227253451],[-0.573515053487736,0.0363147158427738,-0.437387844851897,-1.03588831571493,-1.83032058977009,-2.26001801819755,-2.20758316709239,-1.92084665157889,-0.188628305686224,-0.106446594443183],[-0.189849740397194,-0.269643446090129,-0.316452676725136,-0.563901960277276,-0.646141042382588,-0.463818671023064,-0.206334662602325,-0.17096265547446,-1.08279408143292,-0.830553224486888],[-0.491674787872537,-0.966757459797149,-0.803032498592477,-1.16120379195849,0.253935186526899,0.42707590913766,0.738058543767267,0.671630686463453,-0.234336460356982,-0.333655102491507],[1.20787086949994,0.5161515172013,0.203624820062846,-0.133674833201848,-0.444849226744524,-0.5228801410827,-0.603247576162674,-0.743253683487187,0.411071473623858,0.362888151979871],[0.43130282719991,0.423738503606324,-0.276364262916664,-0.119692105152959,-0.803283351988512,-1.01150725162762,-1.00191127320266,-1.09771344607509
,-0.207966371123852,-0.468258930744378],[-0.321535010784534,-0.883834551829042,-0.522240760844227,-0.729364242189136,-0.758510265362697,-0.738829983500061,-0.681002960111316,-0.844833557962652,0.207582285041544,-0.297278790849427],[0.100862626032804,-0.446738769258193,-0.396267743923354,-0.423658977062603,-0.961922255019255,-0.815853447031442,-1.07369339586783,-1.17107102844454,-0.0308472717746673,-0.334802620208923],[-0.510057014435046,-0.748182910911649,-0.371842216392323,-0.429907115001566,0.121361952311742,0.0805210633410006,0.0275494128246485,0.165565253645362,1.05505102777124,0.826370558044104],[-0.31778448093173,-0.734089926338415,-0.10080327156225,-0.204344296584074,-0.614088999867729,-0.6690116133952,-0.675441647881876,-0.780340016796183,-0.101607011216898,-0.100938509399587],[-0.279885608283335,0.216146885951919,-0.6278882016463,-0.098151145726291,1.15999778913566,1.44512516624808,1.03527978625174,0.70097371941123,0.164840765409513,-0.400440633645106],[-0.392957137919721,0.168998477285098,-0.436798309354713,0.310245289719654,0.3330052058048,0.732023877400899,0.76164262711063,0.469184136230003,-0.854033557335521,-0.896856798199172],[-0.25981332814518,0.306605008874693,0.13558706427427,-0.120321957767773,-0.360291698242288,-0.677535949280096,-0.891714901248958,-1.11309816126646,0.0660628061570829,0.300922195239418],[-0.447895454837646,-0.818523431644132,-0.400501680675853,-0.678043851134022,1.0513700497176,1.38961550280715,1.36350019505217,1.28182313203373,0.499521147926646,0.399264463621951],[-0.168666192154505,-0.104615129889563,-0.491102567765721,-0.346401255329414,0.147552337246063,0.662915868619779,1.3043855057985,1.49415257878084,0.142426189561353,-0.325966733784822],[0.066830040331434,-0.116255615255854,0.240283209160433,-0.290130222721856,-1.95441312791127,-1.98186081985827,-2.04146471105377,-1.93419365614889,-0.439254028772758,0.378379641164984],[0.274845538648989,-0.288694744277401,0.181048290227527,-0.124730926071477,-0.641775978226868,-0.673375261526754
,-0.728068139534533,-0.72379354705307,-0.724270743234164,-0.338015669817687],[-0.0678417630868425,0.299993924055976,-0.234212474868051,0.167142775633722,1.12046277949671,0.396631852405889,0.601291457828465,0.744275070115415,-1.34517646930255,-0.992387648174036],[-0.131299802139532,-0.170103967408311,-0.493688484832912,-0.361631091555637,-0.975142163605149,-1.5062231735189,-1.10335372775817,-0.885078342734777,-0.255432531743485,-0.199166026010378],[-0.30907954744621,-0.440536434307299,-0.267976780615828,-0.24490680497815,-0.614587864342669,-0.161813628243896,-0.133316692775058,0.00591062646075398,0.408214713956936,0.381822194317231],[-0.108981834373464,0.915660083665732,-0.207000052259425,0.964914097558204,1.21724248763496,1.09664219685841,0.954125822607333,0.645446104978804,-0.715590588861592,-0.519208717397639],[-0.195822806459067,-0.893502374789747,-0.750106949332837,-0.516524446590903,-0.543374960545063,-0.122134874303488,0.0186925081629486,-0.0312775923793115,-0.193462822045631,-0.192280919705883],[-0.587614267564017,-1.08911584414357,-0.413190092399323,-0.607664119954611,-0.0806781600387316,0.656725577084319,0.788007366568713,1.01416984191633,-0.45705383900512,-0.410768293101848],[-0.57529771273876,-0.668725490953354,-0.363856690112293,-0.509583470775644,-0.476028256428239,-0.417442224601666,-0.667717603118766,-0.651149163401108,-0.700208036808933,-0.604870915002727],[-0.473292561310029,-0.131361588631955,-0.347229109384916,0.23793820953891,0.213277731819335,-0.26897670793973,-0.328786518913496,-0.49679258383207,-0.862493960964483,-0.754977707617885],[0.0831054877790958,0.329192882005311,-0.169926308607005,0.0395346358722342,0.997243254186666,0.348530242769691,0.702630925120469,1.03261112303975,-0.833486862808041,-0.970917591681187],[-0.199133459353827,-0.603929751036569,-0.531740321469296,-0.457267912589123,0.682584486618614,1.27433400798284,1.1106664631397,0.783602885107923,0.794866147337694,0.126269998648737],[0.0126788716542209,-0.525094341746701,-0.575633918941406
,-0.930513973256405,-0.0362792217691212,1.05219387403002,0.605204973841774,0.470814304727101,-0.452878574876541,-0.523110277636853],[-0.351354038256211,-0.907986337497422,-0.652916663208541,-0.72149108450395,0.34634983050943,1.12363592716058,0.923126656291384,0.863277370403624,0.0166188888449654,-0.311508010545383],[-0.80963868942436,-0.712390639876979,-0.743237520937247,-1.04954352040411,-0.997092200502485,-0.413890417982959,-0.632084009944952,-0.650028422559352,-0.487709067738633,-0.338589428676395],[-0.138847164682829,0.426226546280035,-0.0184022872968419,0.783390573968566,0.0513962097014853,-0.122642275249017,-0.407159826443187,-0.649620880435078,-0.645709852393799,-0.628567155867363],[-0.463731025327263,-0.760818613347423,-0.46430549971193,-0.677691133669726,-0.752648607782159,-1.28002383200184,-1.02199378958675,-0.82659604790136,-0.80755627506213,-0.534470703039269],[-0.746460782539688,-0.528346568955909,-0.50371058828503,-0.549138214986016,0.317789839319148,0.970603801988877,0.846298157714316,0.704947255122908,-1.04862284080165,-0.755803920374424],[-0.62803664486646,-0.0919794274537891,-0.478615134052655,-0.228656607515927,-1.18005074668653,-1.1847339344314,-1.4480520987199,-1.4199773808453,-0.804809390767013,-0.734987948980502],[-0.50028711568268,-1.00660168604329,-0.254605043656986,-0.549339767822757,-0.379747412764927,0.947567799061837,0.711899778836201,0.719007458410385,-0.260706549590111,-0.575815766397759],[-0.229415515202392,-0.700856784910991,-0.481388630596222,-0.767747460535952,-0.468420573185412,-0.0628704438656403,-0.00571547328847901,0.145697575086971,-1.1174048235514,-1.09038566124134],[-0.195290323825645,0.10082610802542,-0.26127751360238,-0.0107276027899906,1.07219764154632,0.749884390683538,0.910562210143392,0.69027573864902,-0.319379998133824,-0.498782902027638],[-0.408514891383205,-0.685075485666311,-0.621322919973121,-0.659312034369429,-1.11881513238771,-0.193373967055832,-0.178013165137587,-0.263984145340157,-0.752508713787973
,-0.620809936097632],[0.0938708975417739,-0.105610346959048,-0.285609251395222,-0.310033565350005,-0.817251557286816,-0.529882274131007,-0.626522697715513,-0.816916922449836,-0.392776746499367,-0.385063896231734],[0.013327111381866,-0.324113808911014,-0.229228220210045,0.20443005043076,0.923785460251833,1.5021570325256,1.23754677178172,0.994200277826866,-0.256531285461532,-0.500159923288537],[-0.422753013972553,-0.573451228283611,-0.304045634216231,-0.502088224659347,-0.69315901914563,-0.744512874089992,-0.767924210512181,-0.88487457167264,-0.631975430918211,-0.366703612753082],[-0.125465644590726,0.322546253719827,-0.128404251657655,0.655278552115226,1.12245823739647,0.232436906432537,0.292741616358094,0.0767210705534807,-0.910619373814944,-1.019136286167],[-0.667394056902058,-0.721631941236477,-0.428464421189984,-0.47020508529742,0.553628019846768,0.690518480056584,0.746503499374934,1.05696176496517,-0.730973140914251,-0.736479722013143],[-0.394230465956167,-0.599575676357575,-0.508386676660417,-0.854515956752845,-0.842818361627463,-0.540436213798021,-0.36833362810062,-0.262455862374127,-0.686473615333345,-0.634786701895756],[-0.0473990602471763,0.0290283051554778,-0.0506927543016605,-0.465871699307494,-2.12714495235905,-2.34749394120684,-2.4900772308952,-2.54988792039687,-0.551656534128971,-0.101397516486554],[-0.204828708389566,0.782727517956036,-0.0956448359618955,0.457000948971513,0.314671936350776,-0.331082583672542,-0.38985796617382,-0.388895806430348,-0.478919037994256,-0.615806758849699],[0.1812443522608,-0.135804521977868,-0.126046109668922,-0.12271539770407,-0.834088233316023,-0.819303773461042,-0.769366032201295,-0.882429318926992,-0.314105980287198,-0.182182763792625],[-0.38517826118798,0.0897365463940232,-0.200180198439736,0.487989697620404,0.323651496899686,0.0875231963893081,0.221165468219941,0.462357805648402,-1.17300176168458,-0.886024230946767]]);

alpha_coefficients_GREEN = ee.Array([[0.87967655568246,0.531044699357085,-0.322697178980696,-0.42254091012129,0.0769590489053362,-2.01469693684146,-2.1255555238898,2.33955115109939,0.854239312450154,-1.47767174167638,0.530141656117564,2.85155746584698,2.26894969233157,5.84070414255357,-1.35801153321276,-0.418190321083771,0.481063649029109,0.591437268115217,-2.93503483561637,1.43263476564453,1.08266047522518,-1.55811432898259,2.18554550148672,-2.49485337785018,-2.75448774678014,0.948607077287867,-2.72038867709387,0.921221195655112,-0.233743530819598,1.42873047334888,0.774091120719599,-2.04636544298539,-0.397393223042006,-0.182781344542959,-3.06192207093889,-1.67969776532839,2.27419082224464,1.53916469925204,-4.07128811572446,0.374518312262558,0.447144922139846,-1.57601240888986,-1.3407128633761,1.05828650279049,-0.778747787417153,-0.493318360317194,-1.4640796561808,-1.72866115393925,-0.306333654233299,-0.36180742184529,-0.369278477900329,-0.00841108666830245,-0.381185654117453,0.484030789705796,-0.604973811317584,0.135019726835693,1.90577654854404,0.680162225102038,-0.646484762219064,-0.190471913012513,1.27474560188822,-0.405335453606281,0.564535694382513,-1.19502437033905,-1.00109461532786,-0.603108716507285,0.719374279334023,1.42359753151542,0.522069939191971,-0.953163916927887,-1.50153734700054,0.309713548915219,1.05331938809476,0.583779769160231,-0.162821897545744,0.749491017608772,-0.849333470453691,0.708385110697281,1.54316755788749,-0.0290699698878854,0.850879742425867,0.625690219807613,3.75028745733495,0.0597226129954663,-0.70555407579255,0.205150498340189,0.394936368950726,0.947169143152033,0.227423974992814,-0.447024782969776,0.679074153988655,-0.732019077075964,1.7845259753162,-0.90238899245476,1.92375977036271,0.162169543362531,3.06323119587552,0.079439467405994,-0.383017288626696,0.810890807019686,-0.417541331454251,0.281402547522157,-1.12372799853208,-1.2245430304822,-0.275320714160756,-2.32990794875132,0.683098587925601,-0.349449842514591,-1.04915995850411
,0.821223417128316,0.0277607706469176,0.044179934731865,-0.660159966209304,-1.50611757209992,-0.465171033375496,-0.547603488904525,1.1729118445795,-0.355766262059663,0.793875328887416,-0.257891345345056,-0.54392913316077,-0.721733508157848,-1.33892717248354,3.32948323650599,-0.493830573573397,-0.964331574772248,-0.882435990823794,1.4424088680201,-0.0816767745733771,-0.485071434209763,1.16629560441583,-0.263612970771751,-0.677137425353725,-1.54344055394584,4.65665535906117,0.846914501970048,-0.461773332338935,-0.0332166762078741,-2.08300654958453,1.3459088570676,0.274313102029103,3.07760172615189,0.347556989692802,-1.73597923739842,-1.18914884093616,-1.86859620912678,-1.48596531298664,0.507484676313064,-1.01360462052387,1.8891928937608,0.491998892036598,1.01805830214265,-1.72341832057226,-2.8018582521835,-0.524795498793366,1.83897112332399,3.55181127794817,0.134701973729608,-0.357585192419391,-1.11365947087943,-2.1255555238898]]);

mx_GREEN       =  ee.Array([[0.0389653501242236,0.078146602484472,0.0622754552795031,0.126311596273292,0.305578944099379,0.390265341614907,0.405244968944099,0.408459875776398,0.22588747826087,0.148166248447205]]);

sx_GREEN       =  ee.Array([[0.0431938969580218,0.056269131345401,0.0746350308170013,0.0793836507524833,0.0801820975623805,0.0985414009187956,0.0970993854906162,0.098149363261992,0.0910122062455833,0.087144623984718]]);

mean_model_GREEN = 2.71246024844721;

hyp_ell_GREEN  = ee.Array([0.0266810416590947,0.000365020725886048,2.37724223502881e-05,0.0285428016127414,2.90274102447957e-07,0.0805401141974204,0.0350642607484264,1.34789714785041e-06,0.0659898344704746,0.000185253130639712]);

hyp_sign_GREEN = ee.Array([0.418673633400068]);

hyp_sig_GREEN  =6.59858408473693;

XDX_pre_calc_GREEN =  ee.Array([[0.0457751988192008],[0.754126023042303],[0.0317380049160293],[0.274660065919257],[0.42112694099041],[0.0318698994711132],[0.104034812864882],[0.0386034531307501],[0.18700382728275],[0.0487334157182252],[0.150171631054508],[0.440575783737914],[0.113276149680487],[0.0447227967654764],[0.402431165708482],[0.126579138797867],[0.252133085349385],[0.455943760032208],[0.0919779104158602],[0.102778499869631],[0.300100613979944],[0.105363975396168],[0.273662505221965],[0.102332148014072],[0.0387332980690034],[0.372119684004605],[0.174646212764575],[0.117441778191778],[0.141419007731548],[0.0251015901750169],[0.717612078633986],[0.169786079712149],[0.451297695979048],[0.031535647706723],[0.141654854063781],[0.054749410977566],[0.0896001236719983],[0.0178522657858191],[0.102965396025557],[0.103468851114317],[0.0223044219601157],[0.106444016474127],[0.0473223970310642],[0.00557349836607096],[0.0306446745955032],[0.251780438557692],[0.0505494898053256],[0.131008019200472],[4.93065534687424],[2.14291331047712],[2.2899654925902],[0.779491120114736],[0.148471747444741],[0.207414562027668],[0.225324188321475],[0.515839827654918],[0.509186446314226],[0.0798681641893411],[0.366607833563396],[0.118568697231438],[0.216008828634709],[0.703655014536396],[0.106530678644385],[0.070717001596232],[0.168641349463069],[0.248133066734865],[0.0774758355013481],[0.0812790500013599],[0.50272709083615],[0.224288405361155],[0.191776840551001],[0.684258108062714],[0.00618042138774779],[0.238754969612826],[0.0631980894820866],[0.202140112548208],[0.13458039618611],[0.386341008514519],[0.359093595441065],[0.0436550338428771],[0.366861439407611],[0.166372860258782],[0.213195590562441],[0.0353381303631042],[0.145226194479994],[0.394889131359498],[0.109310780187421],[0.184226090627805],[0.133399572187021],[0.119501593152671],[0.0747530496634399],[0.124058184109487],[0.0107205896531186],[0.0220572073791372],[0.190659522819082],[0.0912187871009479],[0.100117072398707],[0.204147439057378]
,[0.0492354434776324],[0.168696968047592],[0.0386197117047118],[0.533126831221299],[0.0260138946199261],[0.0713790368642287],[0.729710172674089],[0.217008264353027],[0.195844552183785],[0.0818671415621099],[0.158440506786658],[0.0963307372547529],[0.106195166146431],[0.129568968942069],[0.177742959257046],[0.360220018172578],[0.624021456704541],[0.106383290505281],[0.082728996731839],[0.0854908786657617],[0.125938816535883],[0.0813210335318743],[0.099588301495868],[0.0865549873691926],[0.0568122628063143],[0.209996278112163],[0.118661691424058],[0.0674093855176452],[0.255935764426958],[0.10060807793378],[0.477769377633249],[0.0922355290406963],[0.14589433684723],[0.233932191756342],[0.018089027753236],[0.189821779692251],[0.012633521072118],[0.0905165167369752],[0.0784995052436643],[0.0664147355271861],[0.0733830082510349],[0.22290894491205],[0.140422233265389],[0.150067016814547],[0.0926539059828366],[0.0527094130893357],[0.230737333851029],[0.197239769794986],[0.241441003352339],[0.110296505355068],[0.101347553395653],[0.0821669042977479],[0.0586031723891872],[0.0495711905674134],[0.241066287581216],[0.103789080572215],[0.0749840018756407],[0.111694037760884],[0.0845789608981885],[0.687599530112253],[0.0366683989867593],[0.0826501545360137],[0.104034812864882]]);

veg_index = 'LAI' ;

scaleFactor_GREEN= 10000;

bands = ['B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B8A', 'B11', 'B12']

bands_dict = {"B2": ee.PixelType.float(),
  "B3": ee.PixelType.float(),
  "B4": ee.PixelType.float(),
  "B5": ee.PixelType.float(),
  "B6": ee.PixelType.float(),
  "B7": ee.PixelType.float(),
  "B8": ee.PixelType.float(),
  "B8A": ee.PixelType.float(),
  "B11": ee.PixelType.float(),
  "B12": ee.PixelType.float()
};