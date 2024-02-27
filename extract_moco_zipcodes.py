import json

moco_zips = ['20883', '20822', '20837', '20866', '20887', '20871', '21771', '20877', '20880', '20842', '20882', '20838', '20862', '20777', '20707', '20833', '20876', '20912', '20860', '21797', '20885', '20855', '20867', '20760', '20839', '20868', '20878', '20905', '20886', '20903', '20906', '20814', '20702', '20851', '21753', '20879', '20861', '20910', '21770', '20854', '20872', '20904', '20875', '20709', '20841', '20901', '20902', '20801', '20834', '20818', '20853', '20976', '20830', '20874', '20850', '20786', '20787', '20783', '20985', '20954', '20812', '20859', '20820', '20810', '37215', '20896', '20913', '20891', '20815', '20852', '20727', '20816', '20817', '20873', '20908', '22102', '28032', '20847', '20940', '20895', '20190', '20750', '20916', '20845', '20584', '20705', '20832']


zip_colors = {
'20883': 'EDF8FB',
'20822': 'EAF6F9',
'20837': 'E8F5F6',
'20866': 'E5F3F4',
'20887': 'E3F2F2',
'20877': 'E0F0F0',
'21778': 'DDEFED',
'21771': 'DBEDEB',
'20882': 'D8ECE9',
'20842': 'D6EAE7',
'20777': 'D3E9E4',
'20838': 'D0E7E2',
'20880': 'CEE6E0',
'20871': 'CBE4DD',
'20876': 'C9E3DB',
'20862': 'C6E1D9',
'20707': 'C3E0D7',
'20860': 'C1DED4',
'20833': 'BEDDD2',
'20912': 'BCDBD0',
'21797': 'B9D9CE',
'20885': 'B6D8CB',
'20855': 'B4D6C9',
'20867': 'B1D5C7',
'20760': 'AED3C4',
'20839': 'ACD2C2',
'20905': 'A9D0C0',
'20878': 'A7CFBE',
'20886': 'A4CDBB',
'20903': 'A1CCB9',
'20906': '9FCAB7',
'20702': '9CC9B4',
'20868': '9AC7B2',
'21753': '97C6B0',
'20851': '94C4AE',
'20861': '92C3AB',
'20814': '8FC1A9',
'20872': '8DBFA7',
'20910': '8ABEA5',
'20875': '87BCA2',
'20709': '85BBA0',
'20854': '82B99E',
'20904': '80B89B',
'20879': '7DB699',
'20801': '7AB597',
'20774': '78B395',
'20834': '75B292',
'20902': '73B090',
'20976': '70AF8E',
'20830': '6DAD8C',
'20874': '6BAC89',
'20818': '68AA87',
'20853': '66A985',
'21770': '63A782',
'20850': '60A680',
'20786': '5EA47E',
'20781': '5BA27C',
'20787': '59A179',
'20985': '569F77',
'20901': '539E75',
'20954': '519C73',
'20812': '4E9B70',
'20859': '4C996E',
'20783': '49986C',
'20820': '469669',
'20841': '449567',
'20810': '419365',
'37215': '3F9263',
'20708': '3C9060',
'20913': '398F5E',
'21045': '378D5C',
'20891': '348C59',
'20815': '318A57',
'20727': '2F8855',
'20896': '2C8753',
'20852': '2A8550',
'20873': '27844E',
'20908': '24824C',
'22102': '22814A',
'20816': '1F7F47',
'20817': '1D7E45',
'28032': '1A7C43',
'20847': '177B40',
'20940': '15793E',
'20190': '12783C',
'20750': '10763A',
'20916': '0D7537',
'20895': '0A7335',
'20845': '087233',
'20584': '057031',
'20705': '036F2E',
'20832': '006D2C',

}




f = open('/home/abba/maryland-politics/clean_slate_moco/housing_assessment_data/Maryland_Political_Boundaries_-_ZIP_Codes_-_5_Digit.geojson','r')
outfile = open('js/zip_lat_long.js','w')
outfile.write('var zipBorderLatLongs = new Array();\n')
data = json.load(f)
features = data['features']
for feature in features:
	
	zipcode = feature["properties"]["ZIPCODE1"]
	if zipcode in moco_zips:
		print(zipcode + ' ' + zip_colors[zipcode])
		
		coordinates_level_0 = feature["geometry"]["coordinates"]
		print("Number of coordinates_level_1 for {0} {1}: {2}".format(feature["properties"]["ZIPNAME"], feature["properties"]["ZIPCODE1"], len(feature["geometry"]["coordinates"])))
		for coordinates_level_1 in coordinates_level_0:

			for coordinates_level_2 in coordinates_level_1:
				coordinates_list = []
				for coord in coordinates_level_2:
					coordinates_list.append("[ {0}, {1} ]".format(coord[1],coord[0]))

				coordinates_string = "[" + ", ".join(coordinates_list) + "]"
				outfile.write('otherMap = new Map();\n')
				outfile.write("otherMap.set('zipcode', '{0}')\n".format(feature["properties"]["ZIPCODE1"]))
				outfile.write("otherMap.set('name', '{0}')\n".format(feature["properties"]["ZIPNAME"]))
				outfile.write("otherMap.set('fillcolor', '#{0}')\n".format(zip_colors[zipcode]))
				outfile.write("otherMap.set('tooltip', '{0} {1}')\n".format(feature["properties"]["ZIPNAME"], feature["properties"]["ZIPCODE1"]))
				outfile.write("otherMap.set('coordinates',{0})\n".format(coordinates_string))
				outfile.write("zipBorderLatLongs.push(otherMap)\n".format(zipcode));
f.close()
outfile.close()
