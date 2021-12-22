# if..else

mtb_bike = "cube"

if mtb_bike == "cube":
    print("jippi!")

if mtb_bike != "Pegasus":
    print("aua!")    

# mit boolscher Variable
if 0 == 0:
    my_bool = True

if my_bool:
    print("true")
else:
    print("false")        

# jetzt mit elif (wie else if)
# Achtung Python kennt kein Switch oder Case

test_integer = 3

if test_integer == 1:
    print("1")
elif test_integer == 2:
    print("2")
elif test_integer == 3:
    print("3")
else:
    print("error")
