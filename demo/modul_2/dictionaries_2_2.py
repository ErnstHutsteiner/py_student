my_bike_1 = {
    "Art" : "MTB", 
    "Marke" : "Cube", 
    "Schaltung" : "Kette", 
    "Bremse" : "Disk", 
    "Laufrad": 28
}

# 1.
my_bike_1.get("Marke")
my_bike_1.update({"Bremse": "Felge"})
my_bike_1.pop("Marke")
copy_dict = my_bike_1.copy()
my_bike_1.clear()

# 2. 
my_bike_1["Farbe"]=  "Grün"


