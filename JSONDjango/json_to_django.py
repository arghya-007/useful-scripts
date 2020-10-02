import json
import copy

with open('mcgill_grades.json') as dataf, open('output.json', 'w') as out:
    data = json.load(dataf)
    newdata = []
    for i, block in enumerate(data):
        new = dict(model="website.Course", pk=(i+1))
        new['fields'] = dict(average=block['average'],
                             course=block['course'],
                             num_average=block['num_average'],
                             num_credit=block['num_credit'],
                             term=block['term'])
        newdata.append(copy.deepcopy(new))
    json.dump(newdata, out, indent=2)