# Argumente (args) können an Funktionen übergeben werden
# es können 1 bis n Argumente sein

def hallo_mit_name(vorname):
    print("Willkommen " + vorname)

hallo_mit_name("Joe")

# jetzt mir 2 Argumenten:

def hallo_mit_name2(vorname, nachname):
    print("Willkommen " + vorname + " " + nachname)

hallo_mit_name2("Joe", "Mayer")
