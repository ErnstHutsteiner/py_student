# @classmethod
from datetime import date

class Mensch:
    """
    Erstellt das Objekt Mensch
    """
    def __init__(self, name, gender, alter):
        self.name = name
        self.gender = gender
        self.alter = alter

    @staticmethod
    def make_me_upper(inputstring):
        print(inputstring.upper())
 
# so
hannes = Mensch("Hannes", "m", 18 )
hannes.make_me_upper("to low for you")
# oder so
Mensch.make_me_upper("again to lower")