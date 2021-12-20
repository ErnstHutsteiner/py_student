# Fahrräder mit Art, Marke, Schaltung, Bremsentyp, Reifengrösse
my_bike_1 = ["MTB", "Cube", "Kette", "Disk", 28]
my_bike_2 = ["Trekking", "vsf", "Kette", "Felge", 28]
my_bike_3 = ["Ebike", "R&M", "Rohloff", "Disk", 29]

# tabellarische Strukturen mit Listen
all_my_bikes = [my_bike_1, my_bike_2, my_bike_3]

print("----------")
print(all_my_bikes)
print("----------")
print(all_my_bikes[0][0])
print("----------")
print(all_my_bikes[1][0])
print("----------")
print(all_my_bikes[2][1:3])
print("----------")
print(all_my_bikes[1])