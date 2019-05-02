class Gamestats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Alien Incasion in an inactive state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = int(open('high_score.txt').read())

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
