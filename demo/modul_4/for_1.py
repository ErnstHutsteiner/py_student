# for
rad_liste = ["vsf T-300", "Cube Agressor", "Scott Racer", "Stevens CX", "R&M Custom"]
for item in rad_liste:
    print(item)

# break & continue wie bei while => no demo here

# range() -- zählt von 0 bis 5, default Start = 0
for item in range(6):
    print(item)

# range mit Start bei 2

for item in range(2, 6):
    print(item)

# pass - vermeidet Fehler, wenn die Loop leer sein sollte
for item in [0, 1, 2]:
    pass