
from typing import List

from program.model.wuerfel import Wuerfel
from program.model.spieler import Spieler

class Controller:
    """Haupt Controller"""

    def __init__(self, view):
        """Spiele und Würfel"""

        # model
        self.spieler: List[Spieler] = []

        # view
        self.view = view

    def get_spieler(self):
        while len(self.spieler) < 3:
            name = self.view.prompt_for_spieler()
            if not name:
                return
            player = Spieler(name)
            self.spieler.append(player)

    def starte_spiel(self):
        for spieler in self.spieler:
            spieler.points = Wuerfel().wuerfeln()
            print(spieler.name, spieler.points)


    def run(self):
        self.get_spieler()

        is_running = True
        while is_running:

            self.starte_spiel()

            is_running = self.view.prompt_for_neues_spiel()