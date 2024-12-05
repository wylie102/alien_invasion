import sys

import pygame

from ship import Ship

class BlueSky:
    """A simple game with a blue background and a single player object."""
    def __init__(self):
        """Initialises the game attributes."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Blue Sky")

        self.ship = Ship(self)

        # Set the background color.
        self.bg_color = (0, 0, 255)
    
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)
            self.ship.blitme()

            # Make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Make a game instance and run the game.
    bs = BlueSky()
    bs.run_game()