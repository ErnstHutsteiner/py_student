# ein einfaches Map-Beispiel
# wir bekommen eine Liste mit Kursen in USD
# und wollen in EUR umrechnen

Kurse = [("Tolle AG", 2.1),("My Corp", 8.9),("Star Enterprises", 7.5)]

us_in_eur = lambda data: (data[0], 1.13*data[1])

euro_list = list(map(us_in_eur, Kurse))
print(euro_list)

