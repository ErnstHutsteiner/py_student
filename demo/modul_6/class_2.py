class Mensch:
    """
    Erstellt das Objekt Mensch
    """
    def __init__(self, name, color, gender):
        """
        Initialisierung eines Menschen,
        Argumente:
        * name (string) : Name des Menschen
        * color (string) : Hautfarbe des Menschen
        * gender (string): Geschlecht des Menschen
        """
        self.name = name
        self.color = color
        self.gender = gender

tim = Mensch("tim", "weiss", "m")
# erste Ausgabe
print(tim.color)
# jetzt manipulation
tim.color = "schwarz"
# zweite Ausgabe
print(tim.color)

# jetzt schützen wir die Farbe

class Mensch2:
    """
    Erstellt das Objekt Mensch
    """
    def __init__(self, name, color, gender):
        """
        Initialisierung eines Menschen,
        Argumente:
        * name (string) : Name des Menschen
        * color (string) : Hautfarbe des Menschen
        * gender (string): Geschlecht des Menschen
        * gehalt (int) : Gehalt des Menschen
        """
        self.name = name # public
        self.__color = color # private
        self.gender = gender
        self._gehalt = 2000 # protected

tim2 = Mensch2("tim", "weiss", "m")
# erste Ausgabe
# print(tim2.color)
# ... okay - geht das?:
print(tim2._gehalt)
print(tim2.__color)
