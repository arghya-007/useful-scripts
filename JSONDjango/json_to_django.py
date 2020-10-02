# Script to create a 

import json
import copy

print("Enter JSON file (Make sure script is located in same folder)")
filename = input()

with open(filename) as dataf, open('output.json', 'w') as out:
    data = json.load(dataf)
    newdata = []
    for i, block in enumerate(data):
        new = dict(model="/PATH/TO/MODEL", pk=(i+1))
        
        # enter JSON fields in dict as follows: field_name=block['filed_name']
        new['fields'] = dict(EXAMPLE1=block['EXAMPLE1'],
                             EXAMPLE2=block['EXAMPLE2'])
        newdata.append(copy.deepcopy(new))
    json.dump(newdata, out, indent=2)
