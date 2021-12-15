# Behandlung zunächst wie alle text-basierenden Dateien.

pfad = "personen.csv"
my_csv = open(pfad)

for zeile in my_csv:
    print(zeile)