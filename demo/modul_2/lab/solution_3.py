


all_shops = [('Finished Parts Shop', 'Frankreich'), ('Aussi Cycles', 'Deutschland'), ('Sepps Handel', 'Australien'), ('Finished Parts Shop', 'Frankreich'), ('Aussi Cycles', 'USA'), ('Sepps Handel', 'Australien'), ('Paris Velo', 'Deutschland'), ('Sepps Handel', 'Frankreich'), ('Sepps Handel', 'Australien'), ('Aussi Cycles', 'USA'), ('Aussi Cycles', 'Australien'), ('Finished Parts Shop', 'USA'), ('Sepps Handel', 'USA'), ('Sepps Handel', 'Frankreich'), ('Aussi Cycles', 'Australien'), ('Paris Velo', 'Deutschland'), ('Sepps Handel', 'Frankreich'), ('Finished Parts Shop', 'Frankreich'), ('Finished Parts Shop', 'Deutschland'), ('Aussi Cycles', 'Deutschland'), ('Finished Parts Shop', 'Deutschland'), ('Finished Parts Shop', 'Frankreich'), ('Paris Velo', 'USA'), ('Aussi Cycles', 'Australien'), ('Finished Parts Shop', 'Frankreich'), ('Paris Velo', 'Australien'), ('Aussi Cycles', 'Deutschland'), ('Aussi Cycles', 'USA'), ('Aussi Cycles', 'Australien'), ('Paris Velo', 'Deutschland')]

german_shops = [name for (name, country) in all_shops if country == "Deutschland" and name == "Aussi Cycles"]
print(german_shops)

