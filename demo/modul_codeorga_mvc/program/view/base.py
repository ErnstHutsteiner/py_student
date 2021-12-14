class Views:
    """Implementiere die anderen Views"""

    def __init__(self, active_view, views):
        """Init the active view and the passives views."""
        self.active_view = active_view
        self.views = views

    def prompt_for_spieler(self):
        """Call the active view."""
        return self.active_view.prompt_for_spieler()

    def prompt_for_wuerfeln(self):
        """Call the active view."""
        return self.active_view.prompt_for_wurfeln()

    def show_winner(self, name):
        """Call the passive views."""
        for view in self.views:
            view.show_winner(name)

    def prompt_for_neues_spiel(self):
        """Call the active view."""
        return self.active_view.prompt_for_neues_spiel()