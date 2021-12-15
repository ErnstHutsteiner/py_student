# was bietet mir pydoc
python  -m pydoc

# Dokumentation einer Klasse oder Funktion
# im Gegensatz zu help muss die Klasse nicht geladen sein
python -m pydoc tuple 

# suche nach Schlüsselwörtern
python -m pydoc -k json


# http server starten
python3 -m pydoc -p 54123

# ... oder die Abkürzung
python -m pydoc -b

# ... wir erzeugen ein Html
python -m pydoc -w docstring_2