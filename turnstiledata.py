import csv
#change input for the stations that you want to count crowdedness


def wieght_for_cowededness(input):
	def crowdedness(x):
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



		crowdedness = int(a [x]['03/29/201720:00:00']-a [x]['03/29/201716:00:00'])
		return crowdedness


	weight = 0
	with open('TurnstileIDtoStationID.csv') as Turnstile:
			reader = csv.DictReader(Turnstile)
			for row in reader:
				if row['stop_id'] == input :
					weight += crowdedness(row['Remote'])
	return weight



	 


		



