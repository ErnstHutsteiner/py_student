# Aliasing

def division(x,y):
    return x/y

try:
    print(division(2,0))
except (ZeroDivisionError) as e:
    print('Exception mit der Meldung {0}'.format(e.args))

# In der Klammer können mehrere Exceptions stehen
# Wenn nur eine Exception (wie hier), dann ist die 
# Klammer optional

