import sys

import pygame

from settings import Settings
from star import Star
from random import randint

class Stars:
    """Class for Stars game"""

    def __init__(self):
        """Initialise the game and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Stars")

        self.stars = pygame.sprite.Group()

        self._create_constellation()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
    
    def _create_constellation(self):
        """Creates a constellation of stars."""
        # Create a star and keep adding stars until there's no room left.
        # Spacing between stars is one star width and one star height.
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x, current_y = star_width, star_height
        num_stars_x = (
            self.settings.screen_width) // (2 * star_width)
        num_rows = (
            self.settings.screen_height) // (2 * star_height)
        
        for row in range(num_rows):
            for col in range(num_stars_x):
                self._create_star(col * 2 * star_width, row * 2 * star_height)

    def _create_star(self, x_position, y_position):
        """Create a star and place it in the constellation."""
        new_star = Star(self)
        x_position += randint(-10, 10)
        new_star.x = x_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position + randint(-10, 10)
        self.stars.add(new_star)
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    s = Stars()
    s.run_game()