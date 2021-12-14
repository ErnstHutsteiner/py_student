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

    @property
    def groesse(self):
        return self.__groesse

    @groesse.setter
    def groesse(self, new_groesse):
        self.__groesse = new_groesse

    @groesse.deleter
    def groesse(self):
        del self.__groesse    


hannes = Mensch("Hannes", "black", "m", 187 )
print(hannes.groesse)
hannes.groesse = 185
print(hannes.groesse)
del hannes.groesse

# groesse wird nun wie eine Property verwendet