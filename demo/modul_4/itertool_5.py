# Permuntationen
# baut alle möglichen Permutationen, die Sortierung spielt eine Rolle
import itertools

buchstaben = ['a', 'b', 'c']

my_combi = itertools.permutations(buchstaben, 2)

for item in my_combi:
    print(item)
