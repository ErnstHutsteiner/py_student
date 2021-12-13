# Sets
my_bike_1 = {"MTB", "Cube", "Kette", "Disk", 28}

# vollständige Ausgabe
print(my_bike_1)

# Datentyp
print(type(my_bike_1))

# Sets mit set Konstruktor erstellen
my_bike_2 = set(("Ebike", "Hai", "Kette", "Disk", 29))
print(my_bike_2)

# hinzufügen eines Item
my_bike_2.add("blau")
print(my_bike_2)

# löschen eines Item
my_bike_2.remove("Kette")
print(my_bike_2)