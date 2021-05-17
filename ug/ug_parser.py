import json

ticketlist = []

with open('ug_data_merged.json') as file:
	for obj in file:
		ticket = json.loads(obj)
		ticketlist.append(ticket)

unique_tickets = set()
output_tickets = []

for i in range(0, len(ticketlist) -1):
	# check if the ticket description is unique and if it has the product subject
	if ticketlist[i]["description"] not in unique_tickets and ticketlist[i]["subject"] is not "Product Submission":
		unique_tickets.add(ticketlist[i]["description"])
		output_tickets.append(ticketlist[i])

open("updated-file.json", "w").write(
    json.dumps(output_tickets, sort_keys=True, indent=4, separators=(',', ': '))
)