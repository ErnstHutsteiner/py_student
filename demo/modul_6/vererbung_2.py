# Vererbung (Inheritance)

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


# jetzt mit __init__()
class Musiker(Mensch):
  # von nun an wird Musiker (unser child) nicht mehr von Mensch (parent), erben
  def __init__(self, name, color, gender, instrument):
    # deshalb:
    Mensch.__init__(self, name, color, gender)
    # und nun die spezifika des Musikerts
    self.instrument = instrument
      


Trompeter = Musiker("Josef", "gruen", "m", "Oboe")
print(Trompeter.name)
print(Trompeter.instrument)

