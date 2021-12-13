# jetzt mal mit mit __iter__ und __next__

freunde = ('Max', 'Mary', 'Lilly')


schleife = freunde.__iter__()
print(type(schleife))

# jetzt gehen wir mit __next__ durch

print(schleife.__next__())
print(schleife.__next__())
print(schleife.__next__())
print(schleife.__next__())
