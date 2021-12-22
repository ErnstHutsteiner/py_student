from kreis import kreis_flaeche

radien = [3, 0, -5, True, False, "sepp"]
message = "Fläche mit Radius = {radius} ist {flaeche}."

for r in radien:
    A = kreis_flaeche(r)
    print(message.format(radius= r, flaeche = A))