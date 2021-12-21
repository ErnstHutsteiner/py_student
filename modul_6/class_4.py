
# importing the random module
import random

class Machine_state:
    """
    Erstellt das Objekt für Maschinenstatus
    """
    def __init__(self):
        """
        Initialisierung der Maschine
        Argumente:
        * drehzahl (int) : Drehzahl der Maschine
        * color (string) : Hautfarbe des Menschen
        * gender (string): Geschlecht des Menschen
        """
        self.drehzahl = None
        self.__verschleiss = None
        self.set_drehzahl()
        self.__verschleiss_faktor()


    def set_drehzahl(self):
        self.drehzahl = random.randint(0,4000)

    def __verschleiss_faktor(self):
        self.__verschleiss = random.randint(0,9) 


my_maschine = Machine_state()

print(my_maschine.drehzahl)

