import itertools

def get_this_item(this_item):
    return this_item['Color']

# Liste aus Dictionaries
my_items = [{"Name":"LL Crankarm","ProductNumber":"CA-5965","Color":"Black"},{"Name":"ML Crankarm","ProductNumber":"CA-6738","Color":"Black"},{"Name":"HL Crankarm","ProductNumber":"CA-7457","Color":"Black"},{"Name":"Chainring Bolts","ProductNumber":"CB-2903","Color":"Silver"},{"Name":"Chainring Nut","ProductNumber":"CN-6137","Color":"Silver"},{"Name":"Chainring","ProductNumber":"CR-7833","Color":"Black"},{"Name":"Freewheel","ProductNumber":"FH-2981","Color":"Silver"},{"Name":"Front Derailleur Cage","ProductNumber":"FC-3982","Color":"Silver"},{"Name":"Front Derailleur Linkage","ProductNumber":"FL-2301","Color":"Silver"},{"Name":"Lock Ring","ProductNumber":"LR-2398","Color":"Silver"}]
my_items.sort()

gruppen = itertools.groupby(my_items , get_this_item)

# for key, group in gruppen:
  #  print(key, group)

for key, group in gruppen:
  print(key, len(list(group)))

for key, group in gruppen:
    print(key)
    for this_item in group:
        print(this_item)
    print()