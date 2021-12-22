# cycle
import itertools


zaehler = itertools.cycle(["A", "B", "C"])

# einen nach den anderen
print(next(zaehler))
print(next(zaehler))
print(next(zaehler))

print(next(zaehler))
print(next(zaehler))
print(next(zaehler))

