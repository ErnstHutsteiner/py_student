# raise
try:
    try:
        entered_value = int(input('Geben Sie eine Zahl bis 100 ein: '))
    except ValueError:
        print("ungültige Eingabe")

    if entered_value > 100:
        raise ValueError(entered_value)      
except ValueError:
   print(entered_value, " ist ausserhalb des gültigen Bereichs")
except:
    print("generischer Fehler")          
else:
    print(entered_value, " ist eine gute Wahl")
finally:
    print("die Operation ist abgeschlossen")

