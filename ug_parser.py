import json

ticketlist = []

with open('ug_data_merged.json') as file:
	for obj in file:
		ticket = json.loads(obj)
		ticketlist.append(ticket)

for t in ticketlist:
	print(t['subject'])