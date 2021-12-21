
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
        """
        self.name = name
        self.__color = color
        self.gender = gender

    def get_color(self):
        return self.__color

    def set_color(self, new_color):
        """
        aendere die Farbe
        """
        self.__color = new_color



tim2 = Mensch2("tim", "weiss", "m")
print(tim2.get_color())
tim2.set_color("blau")
print(tim2.get_color())