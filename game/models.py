"""Game models"""

import random

from game.exceptions import GameOver, EnemyDown
from game.settings import PLAYER_LIVES, ALLOWED_ATTACKS, MODE_HARD, HARD_MODE_MULTIPLIER


class Player:
    def __init__(self, name) -> None:
        """Player initialization"""
        self.name = name
        self.lives = PLAYER_LIVES
        self.score = 0

    def select_attack(self):
        """Player selects an attack option."""
        while True:
            choice = input(f"Choose your attack: {', '.join([f'{k}: {v}' for k, v in ALLOWED_ATTACKS.items()])}\n")
            if choice in ALLOWED_ATTACKS:
                return ALLOWED_ATTACKS[choice]
            print("Invalid choice. Try again.")

    def decrease_lives(self):
        """Decrease player's lives and check for game over."""
        self.lives -= 1
        if self.lives <= 0:
            raise GameOver(f"{self.name} has lost all lives!")

    def add_score(self, points):
        """Add score to the player."""
        self.score += points


class Enemy:

    def __init__(self, level, mode_multiplier=1):
        """Enemy Initialization"""
        self.level = level
        self.lives = level * mode_multiplier

    def select_attack(self):
        """Enemy randomly selects an attack option."""
        return random.choice(list(ALLOWED_ATTACKS.values()))

    def decrease_lives(self):
        """Decrease enemy's lives and check for EnemyDown."""
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown()
