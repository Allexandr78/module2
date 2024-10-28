import random

from game.exceptions import GameOver, EnemyDown
from game.settings import PLAYER_LIVES, ALLOWED_ATTACKS, MODE_HARD, HARD_MODE_MULTIPLIER


class Player:
    def __init__(self, name):
        self.name = name
        self.lives = PLAYER_LIVES
        self.score = 0

    @staticmethod
    def select_attack():
        """Player selects an attack option."""
        while True:
            choice = input("Choose your attack (1 - Paper, 2 - Stone, 3 - Scissors): ")
            if choice in ALLOWED_ATTACKS:
                return ALLOWED_ATTACKS[choice]
            print("Invalid choice. Try again.")

    def decrease_lives(self):
        """Decrease player's lives and check for game over."""
        self.lives -= 1
        if self.lives <= 0:
            raise GameOver(self.name)

    def add_score(self, points):
        """Add score to the player."""
        self.score += points


class Enemy:

    def __init__(self, level, difficulty):
        """Инициализация противника"""
        self.level = level
        # Устанавливаем количество жизней в зависимости от уровня сложности
        if difficulty == MODE_HARD:
            self.lives = level * HARD_MODE_MULTIPLIER
        else:
            self.lives = level

    @staticmethod
    def select_attack():
        """Enemy randomly selects an attack option."""
        return random.choice(list(ALLOWED_ATTACKS.values()))

    def decrease_lives(self):
        """Decrease enemy's lives and check for EnemyDown."""
        self.lives -= 1
        if self.lives <= 0:
            raise EnemyDown()
