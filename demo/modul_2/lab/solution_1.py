

liste_1 = ["Becker", "Müller", "Adam", "Zorro", "Hannsen"]
liste_2 = ["Zorro", "Becker", "Hannsen", "Müller", "Adam"]

# 1.
# einzeln
print(liste_1[1])
print(liste_1[2])
print(liste_1[3])

# oder so:
print(liste_1[1:4])

# 2. 
meine_liste = liste_2.copy()
print(meine_liste)

# 3.
meine_liste = meine_liste + ["Gebhardt"]
print(meine_liste)

# 4. 
# gibt es den Eintrag?
return_value = "Gebhardt" in meine_liste
print(return_value)

# Indexausgabe
print(meine_liste.index("Gebhardt"))

# 5.
# zunächst müssen wir die Listen sortieren
liste_1.sort()
liste_2.sort()

# jetzt der Vergleich
return_value = liste_1 == liste_2
print(return_value)

