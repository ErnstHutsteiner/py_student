# jetzt mit append
my_file = open("demo.txt", "a")
my_file.write("nun doch mehr Inhalt")
my_file.close()

my_file = open("demo.txt")
print(my_file.read())

# und mit write
my_file = open("demo2.txt", "a")
my_file.write("Hallo, ich bin's")
my_file.close()

my_file = open("demo2.txt")
print(my_file.read())

# neue Datei mit x erstellen
my_file = open("demo3.txt", "w")

#schreiben mehrerer Zeilen
zeilen = ["Hallo Du.\n", "Willkommen beim Test.\n", "mit 3 Zeilen.\n"]
my_file.writelines(zeilen)

my_file.close

my_file = open("demo3.txt")

# zeilenweises lesen
for zeile in my_file:
    print(zeile)



# löschen von Dateien
# benötigt os
import os

# mit check
if os.path.exists("demo2.txt"):
    os.remove("demo2.txt")
if os.path.exists("demo3.txt"):    
    os.remove("demo3.txt")