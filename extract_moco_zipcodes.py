import json

moco_zips = ['20883', '20822', '20837', '20866', '20887', '20871', '21771', '20877', '20880', '20842', '20882', '20838', '20862', '20777', '20707', '20833', '20876', '20912', '20860', '21797', '20885', '20855', '20867', '20760', '20839', '20868', '20878', '20905', '20886', '20903', '20906', '20814', '20702', '20851', '21753', '20879', '20861', '20910', '21770', '20854', '20872', '20904', '20875', '20709', '20841', '20901', '20902', '20801', '20834', '20818', '20853', '20976', '20830', '20874', '20850', '20786', '20787', '20783', '20985', '20954', '20812', '20859', '20820', '20810', '37215', '20896', '20913', '20891', '20815', '20852', '20727', '20816', '20817', '20873', '20908', '22102', '28032', '20847', '20940', '20895', '20190', '20750', '20916', '20845', '20584', '20705', '20832']


zip_colors = {
'20883': 'EDF8FB',
'20822': 'EAF6F9',
'20837': 'E8F5F6',
'20866': 'E5F3F4',
'20887': 'E3F2F2',
'20871': 'E0F0F0',
'21771': 'DDEFED',
'20877': 'DBEDEB',
'20880': 'D8ECE9',
'21778': 'D6EAE7',
'20842': 'D3E9E4',
'20882': 'D0E7E2',
'20838': 'CEE6E0',
'20862': 'CBE4DD',
'20777': 'C9E3DB',
'20707': 'C6E1D9',
'20833': 'C3E0D7',
'20876': 'C1DED4',
'20912': 'BEDDD2',
'20860': 'BCDBD0',
'21797': 'B9D9CE',
'20885': 'B6D8CB',
'20855': 'B4D6C9',
'20867': 'B1D5C7',
'20760': 'AED3C4',
'20839': 'ACD2C2',
'20868': 'A9D0C0',
'20878': 'A7CFBE',
'20905': 'A4CDBB',
'20886': 'A1CCB9',
'20903': '9FCAB7',
'20906': '9CC9B4',
'20814': '9AC7B2',
'20702': '97C6B0',
'20851': '94C4AE',
'21753': '92C3AB',
'20879': '8FC1A9',
'20861': '8DBFA7',
'20910': '8ABEA5',
'21770': '87BCA2',
'20854': '85BBA0',
'20872': '82B99E',
'20904': '80B89B',
'20875': '7DB699',
'20709': '7AB597',
'20841': '78B395',
'20901': '75B292',
'20902': '73B090',
'20801': '70AF8E',
'20774': '6DAD8C',
'20834': '6BAC89',
'20818': '68AA87',
'20853': '66A985',
'20976': '63A782',
'20830': '60A680',
'20874': '5EA47E',
'20850': '5BA27C',
'20786': '59A179',
'20781': '569F77',
'20787': '539E75',
'20783': '519C73',
'20985': '4E9B70',
'20954': '4C996E',
'20812': '49986C',
'20859': '469669',
'20820': '449567',
'20810': '419365',
'37215': '3F9263',
'20708': '3C9060',
'20896': '398F5E',
'20913': '378D5C',
'21045': '348C59',
'20891': '318A57',
'20815': '2F8855',
'20852': '2C8753',
'20727': '2A8550',
'20816': '27844E',
'20817': '24824C',
'20873': '22814A',
'20908': '1F7F47',
'22102': '1D7E45',
'28032': '1A7C43',
'20847': '177B40',
'20940': '15793E',
'20895': 'FF0000',
'20190': '10763A',
'20750': '0D7537',
'20916': '0A7335',
'20845': '087233',
'20584': '057031',
'20705': '036F2E',
'20832': '006D2C'
}




f = open('/home/abba/maryland-politics/clean_slate_moco/housing_assessment_data/Maryland_Political_Boundaries_-_ZIP_Codes_-_5_Digit.geojson','r')
outfile = open('/tmp/moco_zip_boundaries.js','w')
outfile.write('var zipBorderLatLongs = new Map();\n')
data = json.load(f)
features = data['features']
for feature in features:
	
	zipcode = feature["properties"]["ZIPCODE1"]
	if zipcode in moco_zips:
		print(zipcode + ' ' + zip_colors[zipcode])
		outfile.write('otherMap = new Map();\n')
		outfile.write("otherMap.set('name', '{0}')\n".format(feature["properties"]["ZIPNAME"]))
		outfile.write("otherMap.set('fillcolor', '#{0}')\n".format(zip_colors[zipcode]))
		outfile.write("otherMap.set('tooltip', '{0} {1}')\n".format(feature["properties"]["ZIPNAME"], feature["properties"]["ZIPCODE1"]))
		coordinates = feature["geometry"]["coordinates"][0][0]
		coordinates_list = []
		for coord in coordinates:
			coordinates_list.append("[ {0}, {1} ]\n".format(coord[1],coord[0]))
		coordinates_string = "[" + ", ".join(coordinates_list) + "]"
		outfile.write("otherMap.set('coordinates',{0})\n".format(coordinates_string))
		outfile.write("zipBorderLatLongs.set('{0}', otherMap)\n".format(zipcode));
f.close()
outfile.close()
