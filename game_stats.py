class GameStats:
    """Track statistics for Alien"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics tahtcna change during the game"""
        self.score = 0