# zip
names_1 = ["Becker", "Müller", "Adam", "Zorro", "Hannsen"]
names_2 = ["Lilli", "Lisa", "Robert", "Jose", "Soeren"]

my_names = zip(names_1, names_2)
print(my_names)
 # returns <zip object at 0x103201200>

print(list(my_names))