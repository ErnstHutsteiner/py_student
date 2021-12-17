import json

with open('./demo/modul_5/labs/people.json') as json_file:
    data = json.load(json_file)

def file_has_content(this_data):
    if len(this_data) > 0:
        return True
    else:
        return False    


def iterate_each_item(this_data):
    for item in this_data:
        print(item)
        print(type(item))
        this_keys = item.keys()
        print(this_keys)
        this_values = item.values()
        print(this_values)
        

has_content = file_has_content(data)
print(has_content)
if has_content:
    iterate_each_item(data)


   