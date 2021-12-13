# combinations
# baut alle möglichen Kombinationen, unabhängig von der Sortierung
import itertools

buchstaben = ['a', 'b', 'c']

my_combi = itertools.combinations(buchstaben, 2)

for item in my_combi:
    print(item)
