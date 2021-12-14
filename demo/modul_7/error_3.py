# einfaches try ... except
# jetzt spezifischer

def division(x,y):
    return x/y

try:
    print(division(2,0))
except ZeroDivisionError:
    print("Division durch Null")

# Division /0 - > wunderbar, aber was bei falschem 
# Datentyp?    
