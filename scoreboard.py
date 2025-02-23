import pygame.font
from pygame.sprite import Group

class Scoreboard:
    """A class to report scoring information"""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #Font settings for scoring information
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 100)

        #Prepare the inital score image
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image"""
        rounded_score = round(self.stats.score)
        score_str = f"{rounded_score}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        #Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw score to screen"""
        self.screen.blit(self.score_image, self.score_rect)