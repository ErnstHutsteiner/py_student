
def guten_tag():
    print("Guten Tag")

def servus():
    print("Servus")
    print('Scope von Servus : ', __name__)

def moin():
    print("Moin")

# wir führen es in der Konsole aus und stellen fest, 
# es passiert erstmal nichts

# jetzt mit Funktion
guten_tag()
# und zusätzlich mit dem Kontext
print('Scope des Aufrufs : ', __name__)