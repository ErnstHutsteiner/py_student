# jetzt mit dem csv-Modul
import csv

pfad = "personen.csv"
file = open(pfad, newline='')

csv_reader = csv.reader(file, delimiter = ';')

csv_header = next(csv_reader) # die erste Zeile ist der Header
csv_data = [] # lese den Rest
for zeile in csv_reader:
    BusinessEntityID = int(zeile[0])
    Title = str(zeile[1])
    FirstName = str(zeile[2])
    MiddleName = str(zeile[3])
    LastName = str(zeile[4])
    EmailPromotion = int(zeile[5])

    csv_data.append ([BusinessEntityID, Title, FirstName, MiddleName, LastName, EmailPromotion])

print(csv_data[0])

# phewwww, jetzt passen unsere Datentypen

# wir wollen nun die Vor- und Nachnamen derer 
# mit EmailPromotion = 2 
# in ein Extra-csv schreiben

new_pfad = "promo_2.csv"
file = open(new_pfad, 'w')
csv_writer = csv.writer(file, delimiter = ';')
# jetzt der Header
csv_writer.writerow(["Vorname", "Nachname"])

for item in range(len(csv_data) -1):
    this_row = csv_data[item]
    vorname = this_row[2]
    nachname = this_row[4]
    promotion = this_row[5]

    if promotion == 2:
        csv_writer.writerow([vorname, nachname])
