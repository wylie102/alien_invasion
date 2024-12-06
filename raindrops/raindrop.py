import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to represent a single raindrop in a rainstorm."""

    def __init__(self, rg_game):
        """Initialise the raindrop and set it's starting position."""
        super().__init__()
        self.screen = rg_game.screen
        self.settings = rg_game.settings

        #Load the raindrop image and set it's attribute.
        self.image = pygame.image.load('images/raindrop.png')
        self.rect = self.image.get_rect()

        #Start each new raindrop near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the raindrop's exact vertical position.
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if the raindrop has moved off the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        return self.rect.top >= screen_rect.bottom

    def update(self):
        """Move the raindrop downwards."""
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y