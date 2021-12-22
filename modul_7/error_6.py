# raise

try:
    entered_value = input("Geben Sie eine Zahl bis 100 ein:")
    entered_value = int(entered_value)
    if entered_value > 100:
        raise ValueError(entered_value)
except ValueError:
    print("Ungültiger Wert:", entered_value)
else:
    print(entered_value, "ist eine gute Wahl.")
finally:
    print("Die Operation ist abgeschlossen.")
