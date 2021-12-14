class Spielerview:
    """View für Spieler """

    def prompt_for_spieler(self):
        """Namen erfragen"""
        name = input("Wer bist Du? : ")
        if not name:
            return None
        return name

    def prompt_for_neues_spiel(self):
        """nochmal ?"""
        print("Geht noch eins? ")
        choice = input("y/n: ")
        if choice == "n":
            return False
        return True

    def prompt_for_wuerfeln(self):
        """Aufforderung zum Würfeln."""
        print()
        input("Würfeln Sie jetzt")
        return True    