import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """A class to represent a single star in a constellation."""

    def __init__(self, s_game):
        """Initialise the star and set it's starting position."""
        super().__init__()
        self.screen = s_game.screen

        # Load the star image and set it's attribute.
        self.image = pygame.image.load("images/star.png")
        self.rect = self.image.get_rect()

        # Start each new star near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.x = self.rect.height

        # Store the star's exact horizontal position.
        self.x = float(self.rect.x)
