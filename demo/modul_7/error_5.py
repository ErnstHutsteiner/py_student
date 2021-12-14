# einfaches try ... except
# mit else und finally

def division(x,y):
    return x/y

try:
    result = division(2, 1)
except:
    print("es ist ein Fehler aufgetreten")
else:
    print("Ergebnis = ", result)
finally:
    print("die Operation ist abgeschlossen")

