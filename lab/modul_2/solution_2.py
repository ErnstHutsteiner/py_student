# Dictionaries

"""
1.
"Erforschen" Sie die folgenden Methoden eines Dictionary:
get(), update(), pop(), copy(), clear()

2. Fügen Sie ein neues Element "Farbe" hinzu
"""

my_bike_1 = {
    "Art" : "MTB", 
    "Marke" : "Cube", 
    "Schaltung" : "Kette", 
    "Bremse" : "Disk", 
    "Laufrad": 28
}

# 1. 

print(my_bike_1.get("Marke"))

my_bike_1.update({"Bremse": "Felge"})
print(my_bike_1)

my_bike_1.pop("Marke")
print(my_bike_1)

copy_dict = my_bike_1.copy()
print(copy_dict)

my_bike_1.clear()
print(my_bike_1)

# 2.
# 2. 
my_bike_1["Farbe"]=  "Grün"
print(my_bike_1)