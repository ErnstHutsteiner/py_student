class Mensch:
    """
    Erstellt das Objekt Mensch
    """
    def __init__(self, name, color, gender):
        """
        Initialisierung eines Menschen.

        Argumente:
        * name (string) : Name des Menschen
        * color (string) : Hautfarbe des Menschen
        * gender (string): Geschlecht des Menschen

        """
        self.name = name
        self.color = color
        self.gender = gender

    def gehen(self, start_stop):
        """
        Lass den Menschen gehen.
        
        Argumente:
        * start_stop (boolean) : true gehen, false stoppen

        """
        pass    


