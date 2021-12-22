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
        is_valid = has_valid_keys(item)
        if is_valid:
            print(item)
        else:
            print("bad record found")
            write_dict_to_file(item)
            
        # print(type(item))
        # this_keys = item.keys()
        # print(this_keys)
        # this_values = item.values()
        # print(this_values)


def has_valid_keys(this_item):
    must_have = {'Vorname': '', 
               'Nachname': '',
               'PLZ': '',
               'Ort':''}  
    is_good_data = True

    for key in must_have:
        if not key in this_item:
            is_good_data = False  
 
    return is_good_data    

def write_dict_to_file(this_dict):
    with open('./demo/modul_5/labs/outfile.txt', 'w') as file:
        file.write(json.dumps(this_dict))    

has_content = file_has_content(data)
if has_content:
    iterate_each_item(data)


   