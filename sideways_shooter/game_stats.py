class GameStats:
    """Track statistics for Sideways shooter."""

    def __init__(self, ss_game):
        """Initialise statistics."""
        self.settings = ss_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialise statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
