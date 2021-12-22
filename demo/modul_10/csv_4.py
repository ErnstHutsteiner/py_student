# jetzt mit dem csv-Modul
import csv

pfad = "personen.csv"
file = open(pfad, newline='')
# newline wurde hier mit leerem String übergeben, 
# da eine neue Zeile mit CR, new line oder beidem 
# beginnen kann

csv_reader = csv.reader(file, delimiter = ';')

csv_header = next(csv_reader) # die erste Zeile ist der Header
csv_data = [zeile for zeile in csv_reader] # lese den Rest

# check:
print(csv_reader.line_num)
print(csv_header)
print(csv_data[0])
# prima
# Das Problem, dass alle String ist besteht noch immer
# BusinessEntityID und EmailPromotion sind nämlich Integer
# also nochmal (fast) von vorne => csv_5.py
