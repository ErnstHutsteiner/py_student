# Behandlung zunächst wie alle text-basierenden Dateien.
# Teil 3
# machen wir es gleich richtig

pfad = "personen.csv"
dataset = [line.strip().split(';') for line in open(pfad)]

print(dataset[0])
print(dataset[1])
# wow! Jede Zeile ist jetzt eine Liste mit Daten
# Aaaber, alle sind Strings
# hier endet die Macht der normalen Verarbeitung
# mit Text