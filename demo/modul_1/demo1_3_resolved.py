# einfache Benutzerinteraktion
print('Geben Sie bitte eine ganze Zahl ein:') 
# my_integer = input()
my_integer = eval(input())
print(type(my_integer)) #mit type() können wir den Datentyp ermitteln
my_integer = my_integer*3
print('dreifacher Wert: ', my_integer)

