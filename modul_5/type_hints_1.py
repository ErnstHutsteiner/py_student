# type hinting - PEP 484
# eingeführt in Python 3.5
# Legt einen Datentypen statsich fest:

def meine_recursion(recursion_counter: int) -> int:
    if(recursion_counter > 0):
        ergebnis = recursion_counter + meine_recursion(recursion_counter - 1)
        print(ergebnis)
    else:
        ergebnis = 0
    return ergebnis

print("\n\nRecursion Example Results")
meine_recursion(6)