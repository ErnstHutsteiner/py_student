# Fahrräder mit Art, Marke, Schaltung, Bremsentyp, Reifengrösse
my_bike_1 = ["MTB", "Cube", "Kette", "Disk", 28]
# vollständige Ausgabe
print("vollständige Ausgabe:")
print(my_bike_1)

# Ausgabe einzelner Werte
print("Ausgabe einzelner Werte:")
print(my_bike_1[0])
print(my_bike_1[1])
print(my_bike_1[4])
# ... usw ...

# Ausgabe von Bereichen
print("Ausgabe von Bereichen:")
print(my_bike_1[1:4])
print(my_bike_1[1:])
print(my_bike_1[:1])
print(my_bike_1[:])
print(my_bike_1[1:1])

# Ausgabe von hinten beginnend
print("Ausgabe von hinten beginnend:")
print(my_bike_1[-1])

# Ausgabe out of range
print("out of range:")
print(my_bike_1[7])