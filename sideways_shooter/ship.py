import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialise the ship and set it's starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get it's rect.
        self.image = pygame.image.load("images/rocket_small.png")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom centre of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Store a float for the ship's exact horizontal position.
        self.y = float(self.rect.y)

        # Movement flag; start with a ship that's not moving
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at it's current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Centre the ship on the screen."""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
