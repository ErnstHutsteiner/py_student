# Fahrräder mit Art, Marke, Schaltung, Bremsentyp, Reifengrösse
my_bike_1 = ["MTB", "Cube", "Kette", "Disk", 28]
my_bike_2 = ["Trekking", "vsf", "Kette", "Felge", 28]

# Werte Manipulieren
print("Werte manipulieren:")
my_bike_2[4] = 26
print(my_bike_2)

# Aneinanderhängen von Listen
print(my_bike_1 + my_bike_2)
print(my_bike_2*3)

# Neue Liste aus Liste
print("Neue Liste:")
my_new_list = my_bike_2[1:3]
print(my_new_list)

# Neues Element an Liste anhängen
print("Neues Element an Liste anhängen:")
my_bike_2 = my_bike_2 + ["Trapez"]
print(my_bike_2)