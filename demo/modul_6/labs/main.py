from baseclass import BaseClass

test = BaseClass(True, 100, -20,  "gruen", 2 )

test.set_is_on(False)
test.set_liquid(98)
test.set_temp(9)
print(test.get_alert_state())
print(test.get_is_on())
print(test.get_liquid())
print(test.get_temp())
