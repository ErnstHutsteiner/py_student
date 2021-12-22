# now we gonna load us a json

# let's import the module first
import json

# now we can open and process it
with open('./demo/modul_2/bicycles.json') as json_file:
    data = json.load(json_file)

    print("Type:", type(data))

    for nodes in data:
        print(data[nodes])