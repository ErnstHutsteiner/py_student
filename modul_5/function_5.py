# return

# einfaches Beispiel
def value_return_function():
    if 0 == 0:
        return True
    else:
        return False

ret_val = value_return_function()
print(ret_val)

# AABER - Python kann auch multiple Werte zurück geben:

def my_divider(nenner):
    zaehler = 100
    error = "no"
    try:
        division_result = zaehler / nenner
        return division_result, error
    except:
        error = "yes"
        return "AUA!", error

ergebnis = my_divider(10)
print(ergebnis)
print(type(ergebnis))

ergebnis = my_divider(0)
print(ergebnis)      

# oder so:
ergebnis, fehler = my_divider(0)
print(ergebnis) 
print(fehler)     