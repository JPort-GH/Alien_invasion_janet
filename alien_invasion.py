# Name: Janet Portillo
# GitHub: JPort-GH
# Date: 07.13.2026
# Origin (0,0) is the top-left of the screen. X increases to the right, Y increases downward.

import pygame
from settings import Settings

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        pygame.init()  # Initialize all pygame modules
        self.settings = Settings()

        # Create the game window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Fill the screen with background color
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()  # Update the display each loop

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
