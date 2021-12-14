# einfaches try ... except
# jetzt NOCH spezifischer

def division(x,y):
    return x/y

try:
    print(division(2,'0'))
except ZeroDivisionError:
    print("Division durch Null")
except TypeError:
    print("Datentyp stimmt nicht")

