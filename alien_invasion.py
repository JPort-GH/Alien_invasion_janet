# Name: Janet Portillo
# GitHub: JPort-GH
# Date: 07.13.2026

import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        pygame.display.set_caption(self.settings.name)

        self.bg_image = pygame.image.load(self.settings.bg_file)

        self.ship = Ship(self)

        self.running = True
        self.clock = pygame.time.Clock()

    def run_game(self) -> None:
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            self.screen.blit(self.bg_image, (0, 0))
            self.ship.blitme()
            pygame.display.flip()
            self.clock.tick(self.settings.FPS)

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
