# chain
# wir "verketten"
import itertools

zahlen = [0, 1, 2]
buchstaben = ['a', 'b', 'c']
bikes = ['Cube', 'Simplon']

my_combi = itertools.chain(zahlen, buchstaben, bikes)

for item in my_combi:
    print(item)
