
import json

# ein einfaches JSON
my_json = '{ "name":"Sepp", "alter":38, "stadt":"Hamburg"}'

# wir machen ein Dictionary daraus
my_dict = json.loads(my_json)

print(my_dict["alter"])

# jetzt andersrum wir konvertieren ein
# Dictionary nach JSON

this_dict = {
    'name': 'Sepp', 
    'alter': 38, 
    'stadt': 'Hamburg'
}

# und jetzt nach JSON

this_JSON = json.dumps(this_dict)

print(this_JSON)

# und jetzt ein komplexes Python-Objekt
# mit verschiedenen Datentypen

complex_obj = {
  "name": "Sepp",
  "alter": 38,
  "verheiratet": True,
  "geschieden": False,
  "kinder": ("Lili","Billy"),
  "haustiere": None,
  "raeder": [
    {"model": "Cube", "groesse": 27.5},
    {"model": "Rennstahl", "groesse": 29.0}
  ]
}

print(json.dumps(complex_obj))