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

with open("ug_cleaned_updated.json", "w") as f:
    for ticket in output_tickets:
        json.dump(ticket, f)
        f.write("\n")
