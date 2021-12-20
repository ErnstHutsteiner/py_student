# Listen Methoden - Beispiele

my_bike_1 = []

# append
my_bike_1.append('Rennrad')
print(my_bike_1)
my_bike_1.append('Cannondale')
print(my_bike_1)

# extend
my_bike_1.extend(['Kette','Felge'])
print(my_bike_1)

# einfügen an einer bestimmten Stelle
my_bike_1.insert(3, "Alu")
print(my_bike_1)

# index eines Elements holen
print(my_bike_1.index('Alu'))

# prüfen, ob ein Element vorhanden ist
return_value = 'Alu' in my_bike_1
print(return_value)

# Grösse der Liste
print(len(my_bike_1))


# Element löschen - basierend auf dem Index
my_bike_1.pop(0)
print(my_bike_1)



# clear
my_bike_1.clear()
print(my_bike_1)

# Objektid erhalten
id(my_bike_1)
print(id(my_bike_1))

