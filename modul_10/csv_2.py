# Behandlung zunächst wie alle text-basierenden Dateien.
# Teil 2
# 

pfad = "personen.csv"
my_csv = open(pfad)

# wie bauen uns eine Liste aus Zeilen
zeilen =  [line for line in open(pfad)]

# sehen wir uns die ersten Zeilen an
print(zeilen[0])
print(zeilen[1])
# jede Zeile ist nun ein String für sich

# mit stip können wir alle vor- und hintenangestellen Leerzeichen entfernen
print(zeilen[0].strip())

# mit split können wir den String in kleinere Stück hacken
print(zeilen[0].strip().split(';'))

