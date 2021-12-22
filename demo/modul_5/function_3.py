# Arbitrary Arguments, *args

def meine_bikes(*bike):
    print("Das erste Bike ist ein " + bike[0])

meine_bikes("Cube", "vsf", "Kalkhoff")

# übergabe von Key/Value-Pärchen

def meine_bikes2(bike_1, bike_2):
    print(bike_1 + " " + bike_2)

meine_bikes2(bike_1 = "Cube", bike_2 = "vsf")

# key Value, wenn die Azahl unbekannt mit **

def meine_bikes2(**bikes):
    print(bikes["trekking"])

meine_bikes2(mtb = "Cube", trekking = "vsf")

