# wir definieren ein Tupel
my_bike_1 = "MTB", "Cube", "Kette", "Disk", 28

# Datentyp ausgeben: 
print(type(my_bike_1))

# Zugriff auf Daten erfolgt im Prinzip wie bei Listen
print(my_bike_1[2])

# versuch Daten zu ändern
my_bike_1[2] = "Pinion"

# Wert hinzufügen geht
Farbe = "blau", # man beachte das Komma!
my_bike_1 = my_bike_1 + Farbe

# Tupel können mit der Tupel Methode erstellt werden
other_bikes =tuple(("Trekking", "Boettcher", "Rohloff", 26))
Print(other_bikes)

# Tupel mit einem Listenelement
my_bike_2 = "MTB", "Cube", "Kette", "Disk", [28]
my_bike_2[4][0] = 26
print(my_bike_2)
