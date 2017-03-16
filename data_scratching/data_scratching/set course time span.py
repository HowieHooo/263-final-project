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
stattime = []
endtime = []
# for tt in all_time2:
# 	c,d= tt.split('-')
# 	stattime.append(c)
# 	endtime.append(d)

for mm in stattime:
	a,b = mm.split(':')
	# print a
for item in data:
	if item['Day_And_Time']!= " TBA To Be Arranged" and "Cancelled" not in item :
		aa,bb = item['Day_And_Time'].split()
		if  bb !="Cancelled":
			cc,dd = bb.split('-')
			start,ff= cc.split(':')
			end,gg = dd.split(':')
			if "00" not in gg:
				end = int(end)+1
			if "PM" in dd and "12" not in dd:
				end = int(end)+12
			if "PM" in cc and "12" not in cc:
				start = int(start)+12	
			item['starttime'] =int(start)
			item['endtime'] = int(end)

# with open('data3333333333.json', 'w') as outfile:
#     json.dump(data, outfile)

print data










