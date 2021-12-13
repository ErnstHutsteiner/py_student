# count
import itertools

zaehler = itertools.count()

# das wäre eine infinite loop
# for zahl in zaehler:
  #  print(zahl)

# einen nach den anderen
print(next(zaehler))
print(next(zaehler))
print(next(zaehler))

# In diesem Beispiel nutzen wir .count()
# um einen Index zu bauen
input = ["A", "B", "C", "D", "E"]
output = list(zip(itertools.count(), input))
print(output)

# wir können auch den Startwert und die Schrittlänge festlegen
zaehler = itertools.count(start=4, step=2)

# das wäre eine infinite loop
# for zahl in zaehler:
  #  print(zahl)

# einen nach den anderen
print(next(zaehler))
print(next(zaehler))
print(next(zaehler))