# Product
# bildet das karthesische Produkt
import itertools

zahlen = [0, 1, 2]

my_product = itertools.product(zahlen, repeat=3)

for item in my_product:
    print(item)
