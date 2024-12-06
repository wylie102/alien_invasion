import sys

import pygame

from settings import Settings
from raindrop import Raindrop
from random import randint

class RaindropGame:
    """Class for Raindrops game"""

    def __init__(self):
        """Initialise the game and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Raindrops")

        self.raindrops = pygame.sprite.Group()

        self._create_rain()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_raindrops()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    sys.exit()

    def _update_raindrops(self):
        """Respond appropriately if any raindrops disappear off the screen."""
        self._check_raindrop_edges()
        self.raindrops.update()

    def _create_rain(self):
        """Creates a shower of raindrops."""
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size

        num_raindrops_x = self.settings.screen_width // (2 * raindrop_width)
        num_rows = self.settings.screen_height // (2 * raindrop_height)

        print(f"Screen width: {self.settings.screen_width}, Screen height: {self.settings.screen_height}")
        print(f"Number of raindrops per row: {num_raindrops_x}")
        print(f"Number of rows: {num_rows}")

        for row in range(num_rows):
            for col in range(num_raindrops_x):
                x_position = col * 2 * raindrop_width
                y_position = row * 2 * raindrop_height
                self._create_raindrop(x_position + randint(-10,10), y_position + randint(-10, 10))

    def _create_raindrop(self, x_position, y_position):
        """Create a raindrop and place it in the shower."""
        new_raindrop = Raindrop(self)
        new_raindrop.rect.x = x_position
        new_raindrop.rect.y = y_position
        new_raindrop.y = float(y_position)
        self.raindrops.add(new_raindrop)

    def _check_raindrop_edges(self):
        """Reset raindrops that have moved off the bottom of the screen."""
        for raindrop in self.raindrops.sprites():
            if raindrop.check_edges():
                raindrop.y = -raindrop.rect.height
                
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    rg = RaindropGame()
    rg.run_game()