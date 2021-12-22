# Beispiel 1 - die ersten 100 ints im Quadrat

# erstmal als Liste
quadrate = []
for i in range(1, 101):
    quadrate.append(i**2)

print(quadrate)

# jetzt das Selbe als List Comprehension:
comp_quadrate = [i**2 for i in range(1, 101)]
print(comp_quadrate)