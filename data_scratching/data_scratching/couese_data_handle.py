import json

json_data = open('course_data.json').read()
count = 0
data = json.loads(json_data)
all_time = []
all_time2 = []
for item in data: 	
	if str(item['Day_And_Time']) in all_time:
		continue
	all_time.append(str(item['Day_And_Time']))
	# print item['Day_And_Time']
for ii in all_time:
	if ii!= " TBA To Be Arranged":
		a,b = ii.split()
		if b in all_time2 or b =="Cancelled":
			continue
		all_time2.append(b)

# for ii in all_time2:
# 	print '<option value="',ii,'">',ii,'</option>'
# 	count = count+1
# print count	

for tt in all_time2:
	c,d= tt.split('-')
	print c







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

# with open('data2222222222.json', 'w') as outfile:
#     json.dump(data, outfile)