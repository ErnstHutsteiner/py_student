# ich bin ein Kommentar

# erste Ausgabe mit doppelten Anführungszeichen
print("Das ist ein MegaEvent")


# zweite Ausgabe mit einfachen Anführungszeichen
print('Das ist ein MegaEvent')

# => das macht für Python keinen Unterschied

# jetzt maskieren wir MegaEvent
# so nicht:
print("Das ist ein "MegaEvent"")
# dann so:
print('Das ist ein "MegaEvent"')

# Python verwendet Einrückung (Indentation)
if 5 > 2:
    print("das ist richtig")

# hier würde es zu einem Syntax Fehler kommen:
if 5 > 2:
print("das ist richtig")

