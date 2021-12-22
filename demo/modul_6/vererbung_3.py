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


# jetzt mit der super() Funktion
class Musiker(Mensch):
  # von nun an wird Musiker (unser child) nicht mehr von Mensch (parent), erben
  def __init__(self, name, color, gender, instrument):
    # vorher:
    # Mensch.__init__(self, name, color, gender)
    # jetzt:
    super().__init__(name, color, gender) # hier kein "self"
    # und nun die Spezifika des Musikers
    self.instrument = "Jazztrompete"
      


Trompeter = Musiker("Josef", "gruen", "m", "Oboe")
print(Trompeter.name)
print(Trompeter.instrument)

