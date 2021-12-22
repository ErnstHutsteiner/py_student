# Experiment mit reStructuredText
class Goodclass:
    """
    Diese Klasse ist eine *gute* Klasse. Sie tut **nichts**.

    Attribute:
        name (string): Der Name einer Person
        weight (int): Gewicht in kg 
    """
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

# jetzt mal sehen, was uns die Klasse an bietet:
Goodclass()
help(Goodclass)
