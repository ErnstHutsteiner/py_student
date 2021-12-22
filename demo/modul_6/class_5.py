# Klassenvariablen

class Schraube:
    """
    Objekt für Schrauben
    """
    count = 0
    def __init__(self, gewinde, laenge):
        """
        initialisieren der Schraube
        """
        self.gewinde = gewinde
        self.laenge = laenge

        Schraube.count += 1

    def __del__(self):
        """
        Schraube entfernen
        """
        Schraube.count -= 1


print(Schraube.count)
screw1 = Schraube("M6", 30)
print(Schraube.count)
screw2 = Schraube("M6", 30)
print(Schraube.count)
del screw1
print(Schraube.count)
