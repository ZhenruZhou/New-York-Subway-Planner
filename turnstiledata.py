import csv
#change input for the stations that you want to count crowdedness
input = 'R11'

def stopid_to_Remote(x):
	with open('TurnstileIDtoStationID.csv') as Turnstile:
		reader = csv.DictReader(Turnstile)
		for row in reader:
			if row['stop_id'] == x :
				turnstileid = row['Remote']
	return turnstileid


a = {}
with open('turnstile_170401.txt') as turnstile:
	for row in turnstile:

		temp = row.split(',')
		turnstileid = temp[1]
		time = temp[6]+temp[7]
		entries = int(temp[9])
		exits = int(temp[10])
		if turnstileid not in a:
			a[turnstileid] = {}
		if time not in a[turnstileid]:
			a[turnstileid][time] = 0

		a[turnstileid][time] += (entries - exits)



weight = a [stopid_to_Remote(input)]['03/29/201720:00:00']-a [stopid_to_Remote(input)]['03/29/201716:00:00']




	 


		



