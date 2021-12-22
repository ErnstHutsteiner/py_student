# compress
# eine andere Art Filter
import itertools

zahlen = [0, 1, 2]
buchstaben = ['a', 'b', 'c', 'd']
bikes = ['Cube', 'Simplon']

selectors = [True, False, True, False]

# buchstaben korrespondiert jetzt mit selectors
result = itertools.compress(buchstaben, selectors)

for item in result:
    print(item)
