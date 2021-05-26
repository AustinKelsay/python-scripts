import calendar
import json
from collections import Counter
from datetime import date
from pprint import pprint
import os

from pymongo import MongoClient

with open(os.path.expanduser('~/.mongo/mongo.json'),'r') as config:
    mongo_uri = json.load(config)['mongo_uri']
client = MongoClient(mongo_uri)
db = client.forethought

organization_id = '372'
start = '2021-04-01T00:00:00Z'
end = '2021-05-21T00:00:00Z'
mongo_org_collection = db[str(organization_id)]

target_field_value = 'cs__ds__solicitation___spam'
target_macro = '360019446493'

target_macros = {
    "cs__order_order_problem": "360195828013",
    "return__return_question__how_do_i_return_": "27331002",
    "CS – Unsubscribe: Agatha": "1260805443029"
}

def get_dataset():
    tickets = mongo_org_collection.find({
        'doc_type': 'ticket',
        'original_item.via.channel': {'$in':['web','email']},
        'original_item.created_at': {'$gte': start, '$lte': end}
    })
    print(tickets.count())
    file_path = os.path.expanduser('~/Downloads/ug_field_28758427.txt')
    with open(file_path, 'w') as f:
        count = 0
        for ticket in tickets:
            v = None
            for field in ticket['original_item']['custom_fields']:
                if field['id'] == 28758427: 
                    v = target_macros.get(field['value'])
                    break
            if v != None:
                j = {
                    'ticket_id': ticket['original_item']['id'],
                    'created_at': ticket['original_item']['created_at'],
                    'subject': ticket['original_item']['subject'].replace('"', "'").replace('\n', ' '),
                    'description': ticket['original_item']['description'].replace('"', "'").replace('\n', ' '),
                    'macro_id': v
                }
                json.dump(j, f)
                _ = f.write('\n')
                count += 1
                if count % 100 == 0:
                    print(count)
    print("total: ", count)


get_dataset()