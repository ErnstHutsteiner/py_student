# pass und Rekursion

# falls eine Funktion mal leer bleiben sollte...
def my_empty_function():
    pass

# Python erlaubt Rekursionen, kann also sich selbst aufrufen
# WARNUNG: Aufpassen! Im dümmsten Fall kommt die Funktion nie zu einem Ende

def meine_recursion(recursion_counter):
    if(recursion_counter > 0):
        ergebnis = recursion_counter + meine_recursion(recursion_counter - 1)
        print(ergebnis)
    else:
        ergebnis = 0
    return ergebnis

print("\n\nRecursion Example Results")
meine_recursion(6)     
