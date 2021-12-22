# Lambda

x = lambda a : a + 10
print(x(5))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Lambdas eignen sich gut in Funktionen:
import math
def der_cosinus(a):
    return lambda a : math.cos(a*math.pi)

my_cos = der_cosinus(1)
print(my_cos)    

