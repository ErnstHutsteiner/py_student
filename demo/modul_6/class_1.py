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


joe = Mensch("Joe", "weiss", "m")
mary = Mensch("Mary", "schwarz", "w")
sepp = Mensch()

print(joe.name)
print(mary.gender)
