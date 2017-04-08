import csv
#change input for the stations that you want to count crowdedness
input = '101'
def stopid_to_name(x):
	with open('SubwayStops.csv') as SubwayStops:
		reader = csv.DictReader(SubwayStops)
		for row in reader:
			if row['stop_id'] == x :
				stopname = row['stop_name']
	return stopname
			

a = {}
with open('turnstile_170401.txt') as turnstile:
	for row in turnstile:

		temp = row.split(',')
		stopname = temp[3]
		time = temp[6]+temp[7]
		entries = int(temp[9])
		exits = int(temp[10])
		if stopname not in a:
			a[stopname] = {}
		if time not in a[stopname]:
			a[stopname][time] = 0

		a[stopname][time] += (entries - exits)


		# a[stopname][time] = entries
		# if stopname not in b:
		# 	b[stopname] = {}
		# b[stopname][time] = exits
print len(a)
#print a ['59 ST']['03/29/201720:00:00']
#print a ['stopid_to_name(input)']['03/29/201720:00:00']

#print a ['59 ST']['03/29/201720:00:00'] - a ['59 ST']['03/29/201716:00:00']


	 


		



