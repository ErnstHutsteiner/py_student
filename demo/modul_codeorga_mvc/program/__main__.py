import os, sys

from program.controller.base import Controller

from program.view.base import Views
from program.view.spieler import Spielerview


def main(args=None):
    """The main routine."""
    active_view = Spielerview()
    passive_view = (active_view)
    views = Views(active_view, passive_view)

    spiel = Controller(views)
    spiel.run()


if __name__ == "__main__":
    main()