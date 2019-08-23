class Gamestats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Alien Incasion in an inactive state.
        self.game_active = False

        # High score should never be reset.
        read_only = open("high_score.txt","r").read()
        self.valid = True
        self.high_score = 0
        try:
            self.high_score = round(int(read_only), -1)
        except ValueError:
            self.valid = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
