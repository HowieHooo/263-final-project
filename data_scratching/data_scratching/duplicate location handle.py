import json

json_data = open('data.json').read()
count = 0
data = json.loads(json_data)
all_time = []
duplicate_location= ["TA Studio","TA Lecture","TA Mainstage","TA 2nd Stage","TA Offices","TA Foundry",]
duplicate_location2=["Martial Arts","Fitness/Wellness","East Field","Dance Studio","E Racquet Ct","E Tennis Ct","E Racquet Ct","East Gym","OPERS Conference","50 Mtr Pool",]
for item in data: 	
	for ii in duplicate_location:
		if ii in item['Class_Location']:
			item['Class_Location']= item['Class_Location']+'  (Theater Arts)'
	for ee in duplicate_location2:
		if ee in item['Class_Location']:
			item['Class_Location']= item['Class_Location']+'  (East field)'








# for item in data: 	
# 	a,b = item['Capacity'].split('E')
# 	item['Capacity']=a
# 	c,d = item['Capacity'].split('of')
# 	c = int(c)
# 	d = int(d)
# 	if c>d:
# 		item['Capacity'] = c
# 	else:
# 		item['Capacity'] = d
# 	item['Capacity']=int(item['Capacity'])
# 	if item['Capacity']<10:
# 		print item

with open('data55555555.json', 'w') as outfile:
    json.dump(data, outfile)






