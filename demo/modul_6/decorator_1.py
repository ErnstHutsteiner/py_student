# intro in Decorators - Property

class Mensch:
    """
    Erstellt das Objekt Mensch
    """
    def __init__(self, name, color, gender, groesse):
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
        self.__groesse = groesse


    def get_size(self):
        return self.__groesse

    def set_size(self, new_groesse):
        """
        aendere die Farbe
        """
        self.__color = new_groesse


hannes = Mensch("Hannes", "black", "m", 187 )

# die getter und setter sehen wir als Methode
# hannes.
# goto decorator_2