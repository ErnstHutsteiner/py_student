# Wir haben es bereits kennen gelernt
# mit for können wir einfach über Sequenzen iterieren
# Sequenzen sind interierbar und geordnet
# listen, tuple, strings, etc sind Sequenzen

# hier noch ein paar Beispiele

# tupel
for inhalte in ('Max', 'Mary', 'Lilly'):
    print(inhalte)

# string
for buchstabe in 'Wort':
    print(buchstabe)

# binär
for byte in b'binaer':
    print(byte)

# integer geht nicht, keine Sequenz
# for stelle in 9876543:
  #  print(stelle

# also muss ich mir ein iterierbares Objekt bauen

my_int = 9876543
stellen = [int(stelle) for stelle in str(my_int)]

for x in stellen:
    print(x)

# das geht
# aber was macht ein Objekt iterierbar (iterable)?
# next slide in PPT
# then goto: iterable_2.py