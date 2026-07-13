# Name: Janet Portillo
# GitHub: JPort-GH
# Date: 07.13.2026
# Origin (0,0) is the top-left of the screen. X increases to the right, Y increases downward.

import sys
import pygame
from settings import Settings

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()

        # Create the game window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        pygame.display.set_caption(self.settings.name)

        # Load background image
        self.bg_image = pygame.image.load(self.settings.bg_file)

        self.running = True
        self.clock = pygame.time.Clock()

    def run_game(self) -> None:
        """Start the main loop for the game."""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            # Draw background
            self.screen.blit(self.bg_image, (0, 0))
            pygame.display.flip()
            self.clock.tick(self.settings.FPS)

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
