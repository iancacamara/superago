import pandas as pd
import os

def converter_coordenadas(coordenadas):
    return coordenadas.replace(',', '.')

# Diretório onde o arquivo será salvo
diretorio = 'troca'
if not os.path.exists(diretorio):
    os.makedirs(diretorio)

# Lista de coordenadas
coordenadas = [
    "-1,7391819, -48,8551145",
"-7,8644425, -35,0833408",
"-4,9515026, -47,500732",
"-2,8869514, -40,1194713",
"-7,7513559, -37,6030313",
"-15,7392283, -48,2793357",
"-12,133526, -38,420772",
"-21,4297405, -45,9479419",
"-25,3133048, -49,2997838",
"-3,204065, -52,209961",
"-23,5341639, -47,2703266",
"-29,9981184, -51,0772509",
"-22,7237485, -47,2780375",
"-22,6968402, -46,7915394",
"-1,3432245, -48,3912182",
"-16,3332828, -48,9525756",
"-23,0063966, -44,316326",
"-22,908546, -45,2393714",
"-16,8226769, -49,2452546",
"-23,5525327, -51,4610764",
"-11,0119986, -37,0909236",
"-4,558259, -37,767894",
"-21,1415, -50,4832133",
"-7,193241, -48,2018597",
"-9,7605, -36,6408553",
"-23,4152862, -51,4293961",
"-26,3703324, -48,7210994",
"-28,9348832, -49,4858389",
"-21,7886713, -48,1773096",
"-22,3337071, -47,3357556",
"-3,4547602, -44,7772723",
"-7,5768582, -40,5038509",
"-22,8733203, -42,3428897",
"-25,5861107, -49,4051209",
"-19,6009149, -46,940923",
"-20,282223, -45,539444",
"-8,3751712, -37,0110413",
"-22,7597805, -41,8875267",
"-22,9662839, -42,024427",
"-22,5562511, -47,1310317",
"-23,379245, -46,3262973",
"-22,5777148, -50,4005167",
"-23,137, -46,5868359",
"-23,1045215, -48,9259103",
"-31,3314264, -54,1062808",
"-26,9924395, -48,6339782",
"-26,7638889, -48,6716667",
"-23,107788, -50,370407",
"-21,2254524, -43,7735087",
"-5,496823, -45,248496",
"-10, -55",
"-10,8477365, -36,9658438",
"-26,6338203, -48,6835001",
"-12,1440031, -44,9967406",
"-8,8159644, -35,1831905",
"-20,5531437, -48,5697509",
"-23,5112184, -46,8764612",
"-22,2391397, -49,1135454",
"-7,1252349, -34,9226399",
"-20,949077, -48,479083",
"-1,45056, -48,4682453",
"-22,7667284, -43,4033603",
"-19,9227318, -43,9450948",
"-8,3338293, -36,4176419",
"-23,848568, -46,139586",
"-19,968056, -44,198333",
"-8,2372132, -35,7558262",
"-27,4961277, -48,6542432",
"-21,27, -50,356776",
"-23,6208734, -46,0180378",
"-26,9195567, -49,0658025",
"3,0121994, -60,74727",
"-17,1160208, -43,8122678",
"-23,2853559, -47,6893541",
"-19,7224666, -45,2628492",
"-13,2498754, -43,4101019",
"-27,1519159, -48,4875691",
"-22,8879628, -48,4410712",
"-1,0574255, -46,7635232",
"-22,9360936, -46,5638442",
"-15,7934036, -47,8823172",
"-7,4909841, -38,9859152",
"-27,0964628, -48,9136323",
"-4,3227472, -46,4516989",
"-7,0308237, -34,8443931",
"-8,2838945, -35,0320984",
"-22,8804369, -42,0189227",
"-23,3076663, -47,1324726",
"-26,7737784, -51,0134844",
"-23,1035771, -45,7116825",
"-30,0482234, -52,8901686",
"-29,9189661, -51,0930328",
"-20,848084, -41,11129",
"-14,0691776, -42,4852428",
"-6,461341, -37,0607214",
"-23,3561111, -46,8769444",
"-6,8897849, -38,5570389",
"-17,745, -48,625",
"-12,6998188, -38,3260762",
"-7,9811054, -34,9874515",
"-23,2782035, -51,2779583",
"-27,0273601, -48,6535657",
"-2,9009918, -40,8427389",
"-7,2246743, -35,8771292",
"-22,9056391, -47,059564",
"-20,8975, -45,277223",
"-29,665956, -51,0495276",
"-20,4640173, -54,6162947",
"-25,4597726, -49,5270851",
"-23,2099737, -46,7579173",
"-4,8339574, -42,1739786",
"-24,046329, -52,37802",
"-22,738299, -45,5903769",
"-21,7546, -41,3242",
"-22,7434964, -50,38924",
"-29,3447872, -50,756948",
"-4,3547946, -39,3108516",
"-29,9153779, -51,1772699",
"-26,1755121, -50,3949592",
"-25,6704878, -53,8083036",
"-17,693889, -42,518611",
"-23,62028, -45,41306",
"-20,9523934, -43,8043903",
"-23,5234673, -46,8406808",
"-19,7900887, -42,140533",
"-20,263202, -40,416549",
"-7,3313437, -47,4738762",
"-7,8265, -35,2585295",
"-8,2829702, -35,9722852",
"-24,9554996, -53,4560544",
"-1,2927031, -47,9223903",
"-24,794072, -49,9972914",
"-21,387426, -42,6957219",
"-21,1306497, -48,9814897",
"-3,7300563, -38,6593082",
"-4,8654201, -43,353664",
"-29,1685045, -51,1796385",
"-5,6322688, -35,4213484",
"-23,1871877, -47,7484815",
"-3,7416803, -43,3548006",
"-27,0922364, -52,6166878",
"-29,9956856, -51,5484918",
"-23,662036, -52,6103989",
"-4,455623, -43,892354",
"-25,2925439, -49,2243472",
"-11,5629384, -39,2839543",
"-19,037222, -43,425278",
"-22,337512, -47,172927",
"-27,2312011, -52,0231024",
"-20,5015168, -43,8564586",
"-20,6596107, -43,785743",
"-19,9132749, -44,0840953",
"-23,1825218, -50,6499263",
"-4,1282283, -44,1360269",
"-19,5200067, -42,6282686",
"-22,6437398, -47,1972086",
"-23,603889, -46,918889",
"-5,1782451, -40,6696545",
"-21,3062656, -47,7226987",
"-28,6789941, -49,3695627",
"-20,4911591, -49,9839147",
"-23,8614614, -46,4138008",
"-10, -55",
"-25,4295963, -49,2712724",
"-27,2900659, -50,5779683",
"-6,2424054, -36,4283396",
"-18,7571926, -44,4305993",
"-23,6983419, -46,6088553",
"-20,1597921, -44,8739341",
"-22,2206145, -54,812208",
"-22,7896225, -43,309929",
"-23,6488638, -46,8535993",
"-23,8317997, -46,8156204",
"-27,6350709, -52,2738654",
"-8,3623847, -35,2366232",
"-29,8509795, -51,1832033",
"-6,5583016, -47,4432212",
"-29,5010545, -51,962226",
"-16,3123058, -39,6325702",
"-3,8889838, -38,4546585",
"-25,645841, -49,3126653",
"-12,2578934, -38,9598047",
"-20,2825647, -50,2500762",
"-23,541056, -46,37097",
"-6,7675739, -43,022261",
"-27,5973002, -48,5496098",
"-20,4648425, -45,4266753",
"-15,5492443, -47,3301212",
"-3,7304512, -38,5217989",
"-25,5304023, -54,5830692",
"-20,5937063, -47,3914187",
"-26,0790979, -53,0533527",
"-23,2752097, -46,7285777",
"-23,3141635, -46,7339125",
"-8,8905889, -36,4930896",
"-28,0274798, -48,6240197",
"-26,9307306, -48,9566824",
"-7,560603, -34,99591",
"-15,3118269, -49,1162001",
"-16,680882, -49,2532691",
"-27,317161, -48,557608",
"-18,8698882, -41,9459383",
"-29,3924346, -50,9125926",
"-8,1993049, -35,5631137",
"-29,9440222, -50,9930938",
"-27,0864326, -48,9781319",
"-14,223066, -42,779943",
"-6,8513982, -35,4915582",
"-20,377, -49,0226351",
"-26,4744805, -48,9981151",
"-20,6718755, -40,4984617",
"-25,3950986, -51,4622016",
"-21,2542739, -50,6440083",
"-22,8131263, -45,257554",
"-25,8806192, -48,5750905",
"-23,9927768, -46,2558332",
"-23,4675941, -46,5277704",
"-21,3087615, -46,7190609",
"-11,72794, -49,068046",
"-22,8692626, -47,198053",
"-23,8452962, -50,1905666",
"-23,2684137, -51,0475907",
"-20,0214251, -44,0621506",
"-21,75623, -48,831903",
"-28,7116553, -49,2971441",
"-20,068789, -44,3017439",
"-7,8354423, -34,9061125",
"-29,5648814, -50,7739578",
"-6,361934, -39,2972233",
"-14,792599, -39,0453843",
"-28,241827, -48,6643444",
"-5,5269279, -47,478115",
"-26,8901747, -49,2416736",
"-23,1118339, -47,2215149",
"-19,7999954, -41,7138807",
"-19,4777807, -42,5270802",
"-23,3508977, -47,687611",
"-8,3980773, -35,0611068",
"-11,3034965, -41,8557929",
"-20,346479, -41,6392581",
"-22,7496231, -42,8557428",
"-14,8626965, -39,2886416",
"-26,3391899, -49,9071983",
"-22,4238234, -45,4524156",
"-26,9046787, -48,6552979",
"-17,8575, -42,859722",
"-6,726, -67,9028195",
"-23,659424, -51,9903555",
"-24,0957883, -46,8516945",
"-21,2069948, -41,8893455",
"-23,588607, -48,048326",
"-23,9849105, -48,8803886",
"-23,5512905, -46,9598849",
"-3,4960586, -39,5819197",
"-22,436111, -46,821667",
"-7,7442328, -34,9091039",
"-26,1162431, -48,6180177",
"-23,015, -46,8221146",
"-20,075556, -44,576389",
"-16,6066757, -41,7702077",
"-22,2536514, -47,8212546",
"-23,2973646, -47,2855559",
"-23,1452138, -47,0771667",
"-20,3366604, -47,7797924",
"-8,1752476, -34,9468716",
"-23,3050682, -45,9723075",
"-10, -55",
"-10,2575875, -40,1944363",
"-5,8854585, -38,6212957",
"-4,831508, -37,780997",
"-20,255, -50,5276187",
"-23,5409977, -46,9046393",
"-15,4875, -44,361111",
"-10,5370191, -36,9000007",
"-22,6427642, -43,6533831",
"-15,7528866, -49,3344033",
"-26,4897432, -49,0778063",
"-17,8856178, -51,7202967",
"-22,293585, -48,559193",
"-13,8604033, -40,0719627",
"-17,2328217, -44,4383463",
"-16,4335098, -41,0035557",
"-10,0754917, -38,3476326",
"-10,8778148, -61,9277854",
"-7,1519328, -34,8523098",
"-26,3044898, -48,8486726",
"-9,4336959, -40,5068201",
"-7,2153453, -39,3153336",
"-19,954001, -44,3407921",
"-21,7609533, -43,3501129",
"-23,2015635, -46,9398507",
"-19,6357376, -43,8966132",
"-28,4837443, -48,7816572",
"-8,682, -36,2817143",
"-25,4073197, -52,4150132",
"-12,8602189, -38,3223396",
"-21,2425512, -44,9991978",
"-21,5314282, -42,6403534",
"-19,3816944, -40,0612213",
"-22,775, -45,07175",
"-23,08639, -46,95056",
"-22, -49",
"-12,0869117, -45,7834163",
"-16,2535456, -47,9500276",
"-22,3712958, -41,7866922",
"0,0401529, -51,0569588",
"-9,5421049, -35,7076219",
"-9,1717089, -39,0574899",
"-22,6042779, -43,1081091",
"-23,5401247, -47,1846323",
"-23,3190348, -46,5876377",
"-14,4970828, -46,1115108",
"-2,573, -60,3724681",
"-23,3485076, -52,0966215",
"-22,9600193, -44,04111",
"-20,2574434, -42,0340769",
"-20,3599141, -41,9554606",
"-5,5254959, -49,9455045",
"-21,6163005, -55,164605",
"-3,8779438, -38,6247697",
"-12,7766206, -38,9174729",
"-3,8922967, -38,6835427",
"-2,2429316, -45,8588977",
"-21,0443673, -40,8272204",
"-28,4493053, -52,2002156",
"-24,5582532, -54,0587821",
"-9,7190176, -35,8974587",
"-23,425269, -51,9382078",
"-22,146153, -51,170949",
"-12,530685, -38,300898",
"-19,5576547, -44,0816035",
"-23,6658093, -46,4398236",
"-25,2954233, -54,0940666",
"-17,3728243, -40,2203882",
"-22,783092, -43,4293599",
"-22,4539417, -43,4691978",
"-7,3106846, -38,9447146",
"-17,5653879, -52,5536721",
"-21,4121, -42,1966",
"-8,1202103, -38,728459",
"-22,2925861, -51,907143",
"-20,8141411, -49,507449",
"-18,1263191, -40,3641584",
"-16,7495727, -43,8687268",
"-5,1076699, -38,3727852",
"-5,1840003, -37,3530787",
"-21,130556, -42,366389",
"-13,3264515, -39,5052046",
"-17,8393915, -40,3494631",
"-5,805398, -35,2080905",
"-26,8898813, -48,6495828",
"-12,9784418, -38,5076399",
"-23,205, -46,3767619",
"-16,4069816, -49,219438",
"-14,4648655, -48,4572244",
"-10,1846191, -37,5527235",
"-10,873332, -37,1579737",
"-19,766111, -43,036944",
"-22,2800004, -42,5325303",
"-22,7592175, -43,4508728",
"-22,7804806, -47,2783127",
"-29,3759836, -51,1123342",
"-29,8468808, -51,2917859",
"-19,875834, -44,984166",
"-29,734108, -51,0224276",
"-7,9994355, -34,8710469",
"-20,736634, -48,910625",
"0,2692478, -57,5232205",
"-23,5352768, -46,7882797",
"-20,5230256, -43,6917329",
"-20,385527, -43,5035214",
"-19,9236941, -50,3988565",
"-4,171073, -38,464988",
"-3,9841, -38,6180383",
"-27,6447774, -48,6646323",
"-10,1837852, -48,3336423",
"-22,786384, -50,2198965",
"-28,3549019, -53,4996461",
"-22,6109158, -43,7096912",
"-3,1241888, -47,4037376",
"-21,547222, -45,7375",
"-10,1752474, -48,886759",
"-19,8668656, -44,5912664",
"-25,5148822, -48,5226695",
"-23,08165, -52,461724",
"-22,1636384, -43,2916915",
"-23,2196461, -44,7154196",
"-6,1987191, -50,4298045",
"-6,7108694, -36,6308299",
"-2,6344567, -56,7319324",
"-5,9178169, -35,2240207",
"-20,7167803, -46,6156864",
"-9,3991006, -38,226711",
"-27,964968, -48,6830299",
"-22,7630391, -47,1532213",
"-7,9102565, -34,842971",
"-22,351086, -48,778113",
"-19,617778, -44,043055",
"-26,775418, -48,6465251",
"-10,2323006, -36,5076845",
"-26,775418, -48,6465251",
"-22,5075743, -43,1785356",
"-7,2043881, -37,9373215",
"-7,0823544, -41,4685053",
"-23,7995, -47,44575",
"-22,9364, -45,4622602",
"-25,4443488, -49,1900307",
"-22,7836414, -46,5794451",
"-10,5765266, -37,763662",
"-25,4443488, -49,1900307",
"-22,725165, -47,6493269",
"-23,1938491, -49,3842588",
"-21,9957877, -49,4549675",
"-17,3493765, -44,9507904",
"-22,4169596, -49,1856779",
"-21,013203, -48,220951",
"-24,759586, -51,7637582",
"-21,0342185, -49,928323",
"-23,5398662, -46,3439704",
"-25,0891685, -50,1601812",
"-25,574765, -48,3614806",
"-20,4164353, -42,90878",
"-22,5286917, -55,723426",
"-9,6604975, -35,7034391",
"-29,6887102, -51,2514464",
"-30,0324999, -51,2303767",
"-21,8429211, -47,4524535",
"-23,2378262, -47,5229432",
"-22,4195607, -44,2896491",
"-16,443473, -39,064251",
"-26,2336416, -51,082771",
"-22,2343858, -45,9327241",
"-17,3432883, -39,2187741",
"-19,307222, -48,923889",
"-22,0064609, -51,5542973",
"-21,765074, -52,11114",
"-22,1225167, -51,3882528",
"-10, -55",
"-22,107205, -41,4723411",
"-8,0426045, -34,9276752",
"-22,4683626, -44,4463494",
"-22,0692867, -48,1781765",
"-19,7672898, -44,0875436",
"-23,7129388, -46,4150871",
"-21,1776315, -47,8100983",
"-21,1881942, -45,0627632",
"-22,7108378, -42,6271864",
"-9,992, -68,1577252",
"-22,4100108, -47,5603933",
"-22,5269448, -41,944972",
"-22,9110137, -43,2093727",
"-27,2162607, -49,643654",
"-32,0334252, -52,0991297",
"-9,4818831, -35,8603319",
"-26,259075, -49,517746",
"-17,7921255, -50,9191219",
"-23,3119901, -51,3674145",
"-10, -55",
"-10,6814045, -37,0503317",
"-19,8900372, -43,8107916",
"-18,6656839, -43,0830439",
"-19,8652854, -47,4402746",
"-0,7064037, -47,3507753",
"-12,8767614, -38,4860518",
"-2,438489, -54,699611",
"-22,8029986, -47,4335451",
"-16,2240804, -39,2062339",
"-7,948019, -36,206092",
"-20,2663083, -50,9734419",
"-17,8115199, -50,5976641",
"-23,29474, -46,23539",
"-29,6860512, -53,8069214",
"-7,128465, -34,9846186",
"-21,7103738, -47,4777943",
"-27,8643546, -54,4779287",
"-30,8894097, -55,5317694",
"-27,6865324, -48,7769405",
"-22,0145, -51,7061522",
"-23,6533509, -46,5279039",
"-13,0147319, -39,2302015",
"-20,9413389, -44,9187397",
"-23,8646677, -46,2902657",
"-12,461, -39,2655",
"-26,2483669, -49,3820672",
"-23,7080345, -46,5506747",
"-23,6251004, -46,5644369",
"-22,0180395, -47,891154",
"-15,948889, -44,864444",
"-12,628108, -38,6811326",
"-29,448454, -50,5833027",
"-30,334214, -54,3227149",
"-22,8219014, -43,0309252",
"-3,6099755, -38,9687182",
"-21,8905238, -45,5935943",
"-21,63439, -41,0499142",
"-22,8043744, -43,3724125",
"-21,1335755, -44,2588086",
"-27,6157733, -48,6276491",
"-20,7180697, -46,3125073",
"-8,992, -36,03325",
"-6,078347, -35,265048",
"-20,8125851, -49,3804212",
"-23,1867782, -45,8854538",
"-29,7420897, -51,1688985",
"-7,9959607, -35,039335",
"-26,35566, -52,849837",
"-2,5295265, -44,2963942",
"-23,8807771, -47,9963492",
"-25,349171, -54,240498",
"-9,7775393, -36,1063263",
"-23,5506507, -46,6333824",
"-22,558265, -47,9342667",
"-9,0149761, -42,6888427",
"-23,8027866, -45,4070527",
"-23,9552495, -46,4406413",
"-22,9257974, -42,507633",
"-23,444117, -51,876016",
"-20,1252961, -40,3064477",
"-21,2175, -47,6055",
"-21,1375782, -47,9913741",
"-19,466111, -44,246944",
"-16,6599718, -48,608326",
"-10,7396358, -37,8184319",
"-12,7652971, -38,3970537",
"-3,6879135, -40,3456372",
"-23,6846044, -46,7116969",
"-23,4684836, -47,4424129",
"-6,7520882, -38,2412448",
"-22,8217964, -47,267105",
"-23,5427842, -46,3108391",
"-23,6211189, -46,7875117",
"-27,1167574, -50,0002159",
"-15,811859, -42,2319723",
"-8,7500009, -35,1045787",
"-22,7353777, -42,7202272",
"-21,4064327, -48,5056132",
"-23,031448, -45,5612792",
"-24,3282939, -50,6318021",
"-17,8579267, -41,5081533",
"-5,0874608, -42,8049571",
"-22,4164578, -42,975194",
"-19,5771395, -42,6436108",
"-24,7222438, -53,7402476",
"-29,3373663, -49,7299648",
"-28,471488, -49,014132",
"-3,7991756, -49,8069939",
"-5,2630885, -44,6448502",
"-23,433162, -45,083415",
"-21,12, -42,942777",
"-23,7621152, -53,3116192",
"-16,3628767, -46,892413",
"-29,7560726, -57,0867546",
"-28,5191381, -49,3201776",
"-13,3723582, -39,0694243",
"-22,9797018, -46,9841708",
"-21,5565914, -45,4340674",
"-4,1958345, -40,4735305",
"-17,5983328, -44,7317086",
"-10, -55",
"-22,4093928, -43,6609318",
"-17,9896107, -46,9003899",
"-12,9608153, -38,6099216",
"-28,9802065, -51,5380555",
"-30,0819338, -51,0261927",
"-27,00544, -51,1533733",
"-12,1285, -60,1118585",
"-23,0298535, -46,9749847",
"-20,7538586, -42,8815888",
"-20,3200917, -40,3376682",
"-14,8567487, -40,8414804",
"-22,521856, -44,1040128",
"-23,5846472, -47,4016009",
"-20,4252908, -49,972028",
"-26,8748603, -52,4035964",
"-3,270145, -45,655344",

]

# Converte todas as coordenadas
coordenadas_convertidas = [converter_coordenadas(coord) for coord in coordenadas]

# Cria um DataFrame com o resultado
df = pd.DataFrame({'Coordenadas': coordenadas_convertidas})

# Caminho para salvar o arquivo Excel
arquivo_excel = os.path.join(diretorio, 'coordenadas_convertidas.xlsx')

# Salva o DataFrame no arquivo Excel
df.to_excel(arquivo_excel, index=False)

print(f"Coordenadas convertidas salvas em {arquivo_excel}")
