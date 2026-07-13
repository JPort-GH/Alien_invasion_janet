# Name: Janet Portillo
# GitHub: JPort-GH
# Date: 07.13.2026

from pathlib import Path

class Settings:
    """Store all game settings."""

    def __init__(self) -> None:
        self.name = "Alien Invasion"
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / "Assets" / "images" / "Starbasesnow.png"
