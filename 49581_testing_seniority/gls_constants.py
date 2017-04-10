

########## COUNTRIES NAME ####################
Country_name = dict(
 Country_fullname = ["AFGHANISTAN","ALBANIA","ALGERIA","ANDORRA","ANGOLA","ANTIGUA AND BARBUDA","ARGENTINA","ARMENIA","AUSTRALIA","AUSTRIA","AZERBAIJAN","BAHAMAS","BAHRAIN","BANGLADESH","BARBADOS",\
                    "BELARUS","BELGIUM","BELIZE","BENIN","BHUTAN","BOLIVIA","BOSNIA AND HERZEGOVINA","BOTSWANA","BRAZIL","BRUNEI","BULGARIA","BURKINA FASO","BURMA","BURUNDI",\
                    "CABO VERDE","CAMBODIA","CAMEROON","CANADA","CENTRAL AFRICAN REPUBLIC","CHAD","CHILE","CHINA","COLOMBIA","COMOROS","CONGO BRAZZAVILLE","CONGO KINSHASA","COSTA RICA","C.TE D.IVOIRE","CROATIA","CUBA","CYPRUS","CZECH",\
                    "DENMARK","DJIBOUTI","DOMINICA","DOMINICAN REPUBLIC","ECUADOR","EGYPT","ENGLAND","EL SALVADOR","EQUATORIAL GUINEA","ERITREA","ESTONIA","ETHIOPIA",\
                    "FIJI","FINLAND","FRANCE","GABON","GAMBIA","GEORGIA","GERMANY","GHANA","GREECE","GRENADA","GUATEMALA","GUINEA","GUINEA-BISSAU","GUYANA",\
                    "HONG KONG","HAITI","HOLY SEE","HONDURAS","HUNGARY","ICELAND","INDIA","INDONESIA","IRAN","IRAQ","IRELAND","ISRAEL","ITALIA","ITALY","JAMAICA",\
                    "JAPAN","JORDAN","KAZAKHSTAN","KENYA","KIRIBATI","KOREA NORTH","KOREA SOUTH","KOSOVO","KUWAIT","KYRGYZSTAN","LAOs","LATVIA","LEBANON","LESOTHO","LIBERIA","LIBYAN","LIECHTENSTEIN","LITHUANIA","LUXEMBOURG",\
                    "MACEDONIA","MADAGASCAR","MALAWI","MALAYSIA","MALDIVES","MALI","MALTA","MARSHALL ISLANDS","MAURITANIA","MAURITIUS","MEXICO","MICRONESIA FEDERATED STATES OF","MOLDOVA","MONACO","MONGOLIA","MONTENEGO","MOROCCO","MOZAMBIQUE",\
                    "NAMIBIA","NAURU","NEPAL","NETHERLANDS","NEW ZEALAND","NICARAGUA","NIGER","NIGERIA","NORWAY","OMAN","PAKISTAN","PALAU","PANAMA","PAPUA NEW GUINEA","PARAGUAY","PERU","PHILIPPINES","POLAND","PORTUGAL",\
                    "QATAR","ROMANIA","RUSSIA","RUSSIAN FEDERATION","RWANDA","SAINT KITTS AND NEVIS","SAINT LUCIA","SAINT VINCENT AND THE GRENADINES","SAMOA","SAN MARINO","SAO TOME AND PRINCIPE","SAUDI ARABIA","SENEGAL","SERBIA","SEYCHELLES","SIERRA LEONE","SINGAPORE",\
                    "SLOVAKIA","SLOVENIA","SOLOMON ISLANDS","SOMALIA","SOUTH AFRICA","SOUTH SUDAN","SPAIN","SRI LANKA","SUDAN","SURINAME","SWAZILAND","SWEDEN","SWITZERLAND","SYRIAN",\
                    "TAIWAN","TAJIKISTAN","TANZANIA","THAILAND","TIMOR-LESTE","TOGO","TONGA","TRINIDAD AND TOBAGO","TUNISIA","TURKEY","TURKMENISTAN","TUVALU","UGANDA","UKRAINE","UNITED ARAB EMIRATES","UNITED KINGDOM","UNITED KINGDOM","UNITED STATES","URUGUAY","UZBEKISTAN","VANUATU","VENEZUELA",\
                    "VIET NAM","YEMEN","ZAMBIA","ZIMBABWE"],
  Acronym_name_2W = ["AF","AL","DZ","AD","AG","AG","AR","AM","AU","AT","AZ","BS","BH","BD","BB","BY","BE","BZ","BJ","BT","BO","BA","BW","BR","BN","BG","BF","MM","BI","CV","KH","CM","CA","CF","TD","CL","CN","CO","KM","CG","\
                  CD","CR","CI","HR","CU","CY","CZ","DK","DJ","DM","DO","EC","EG","EN","SV","GQ","ER","EE","ET","FJ","FI","FR","GA","GM","GE","DE","GH","GR","GD","GT","GN","GW","GY","HK","HT","VAT","HN","HU","IS","IN","ID","IR","IQ","IE","\
                  IL","ITs","IT","JM","JP","JO","KZ","KE","KI","KP","KR","XK","KW","KG","LA","LV","LB","LS","LR","LY","LI","LT","LU","MK","MG","MW","MY","MV","ML","MT","MH","MR","MU","MX","FM","MD","MC","MN","ME","MA","MZ","NA","NR","NP","NL","NZ","\
                  NI","NE","NG","NO","OM","PK","PW","PA","PG","PY","PE","PH","PL","PT","QA","RO","RU","RS","RW","KN","LC","VC","WS","SM","ST","SA","SN","RS","SC","SL","SG","SK","SI","SB","SO","ZA","SS","ES","LK","SD","SR","SZ","SE","CH","SY","TW","TJ","\
                  TZ","TH","TL","TG","TO","TT","TN","TR","TM","TV","UG","UA","AE","GB","UK","US","UY","UZ","VU","VE","VN","YE","ZM","ZW"],

  Acronym_name_3W = ["AFG","ALB","DZA","AND","AGO","ATG","ARG","ARM","AUS","AUT","AZE","BHS","BHR","BGD","BRB","BLR","BEL","BLZ","BEN","BTN","BOL","BIH","BWA","BRA","BRN","BGR","BFA","MMR","BDI","\
                    CPV","KHM","CMR","CAN","CAF","TCD","CHL","CHN","COL","COM","COG","COD","CRI","CIV","HRV","CUB","CYP","CZE","DNK","DJI","DMA","DOM","ECU","EGY","ENG","SLV","GNQ","ERI","EST","ETH","FJI","\
                   FIN","FRA","GAB","GMB","GEO","DEU","GHA","GRC","GRD","GTM","GIN","GNB","GUY","HKO","HTI","VAT","HND","HUN","ISL","IND","IDN","IRN","IRQ","IRL","ISR","ITY","ITA","JAM","JPN","JOR","KAZ","KEN","KIR","\
                   PRK","KOR","XKS","KWT","KGZ","LAO","LVA","LBN","LSO","LBR","LBY","LIE","LTU","LUX","MKD","MDG","MWI","MYS","MDV","MLI","MLT","MHL","MRT","MUS","MEX","FSM","MDA","MCO","MNG","MNE","MAR","MOZ","\
                   NAM","NRU","NPL","NLD","NZL","NIC","NER","NGA","NOR","OMN","PAK","PLW","PAN","PNG","PRY","PER","PHL","POL","PRT","QAT","ROU","RUS","RSS","RWA","KNA","LCA","VCT","WSM","SMR","STP","SAU","SEN","SRB","SYC","\
                   SLE","SGP","SVK","SVN","SLB","SOM","ZAF","SSD","ESP","LKA","SDN","SUR","SWZ","SWE","CHE","SYR","TWN","TJK","TZA","THA","TLS","TGO","TON","TTO","TUN","TUR","TKM","TUV","UGA",\
                   "UKR","ARE","GBR","UK","USA","URY","UZB","VUT","VEN","VNM","YEM","ZMB","ZWE"]
                   )
########### DATE TIME #################
Date_time = dict(
     month_of_year = {"january": "01","february": "02","march": "03","april": "04","may": "05",\
                      "june": "06","july": "07","august": "08","september": "09","october": "10",\
                      "november": "11", "december": "12","jan": "01","feb": "02","mar": "03",\
                      "apr": "04","may": "05","jun": "06","jul": "07","aug": "08","sep": "09",\
                      "sept": "09","oct": "10","nov": "11","dec": "12","1": "01","2": "02","3": "03",\
                      "4": "04","5": "05","6": "06","7": "07","8": "08","9": "09","01": "01","02": "02",\
                      "03": "03","04": "04","05": "05","06": "06","07": "07","08": "08","09": "09",\
                      "10": "10","11": "11","12": "12"},
     day_of_month = {"1": "01","2": "02","3": "03","4": "04","5": "05","6": "06","7": "07","8": "08",\
                    "9": "09","01": "01","02": "02","03": "03","04": "04","05": "05","06": "06",\
                    "07": "07","08": "08","09": "09","10": "10","11": "11","12": "12","13": "13",\
                    "14": "14","15": "15","16": "16","17": "17","18": "18","19": "19","20": "20",\
                    "21": "21","22": "22","23": "23","24": "24","25": "25","26": "26","27": "27",\
                    "28": "28","29": "29","30": "30","31": "31"},
     total_day_of_month = {"01": "31","02": "28","03": "31","04": "30","05": "31","06": "30",\
                          "07": "31","08": "31","09": "30","10": "31","11": "30","12": "31"}
                          )
    