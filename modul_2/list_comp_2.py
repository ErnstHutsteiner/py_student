currencies = [
"Emirati Dirham","Afghani","Lek","Armenian Dram","Netherlands Antillian Guilder","Kwanza","Argentine Peso","Shilling","Australian Dollar",
"Aruban Guilder","Azerbaijanian Manat","Barbados Dollar","Taka","Belgian Franc","Bulgarian Lev",
"Bahraini Dinar","Brunei Dollar","Boliviano","Brazilian Real","Bahamian Dollar",
"Ngultrum","Canadian Dollar"]

# mit for loop
my_currencies = []
for cur_name in currencies:
    if cur_name.startswith("C"):
        my_currencies.append(cur_name)

print(my_currencies)

# als List Comprehension
my_currencies2 = [cur_name for cur_name in currencies if cur_name.startswith("C") ]
print(my_currencies2)


