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

    @classmethod
    def ab_geburt(cls, name , gender, geburtsjahr):
        return cls(name, gender, date.today().year - geburtsjahr)    

 

hannes = Mensch("Hannes", "m", 18 )
print(hannes.alter)
lisa = Mensch.ab_geburt("Lisa", "w", 1985)
print(lisa.alter)
