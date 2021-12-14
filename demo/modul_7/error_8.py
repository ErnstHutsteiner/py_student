# Eigene Exceptions

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class Nichtgefunden(Error):
    def __init__(self, error_code):
        self.error_code = error_code
        self.message = "nicht gefunden"


class IstUngerade(Error):
    def __init__(self, error_code):
        self.error_code = error_code
        self.message = "ungerade"

def send_error(e):
    print(e.error_code)
    print(e.message)


liste_1 = [1, 2, 3]

try:
    if liste_1[1] % 2 != 0:
        raise IstUngerade(1234)
    elif 5 in liste_1:
        print("all good")
    else:
        raise Nichtgefunden(4711)   
except Nichtgefunden as e:
    send_error(e)
except IstUngerade as e:
    send_error(e)    