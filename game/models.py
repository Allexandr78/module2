"""Файл с описанием моделей"""
import random
from settings import PLAYER_LIVES, ALLOWED_ATTACKS, ATTACK_PAIRS_OUTCOME
from exceptios import GameOver, EnemyDown


def select_attack()->str:
    while True:
        choice = input("Choose your attack (1 - Paper, 2 - Stone, 3 - Scissors): ")
        if choice in ALLOWED_ATTACKS:
            return ALLOWED_ATTACKS[choice]
        print("Invalid choice. Try again.")


class Player:
    def __init__(self, name):
        self.name = name
        self.lives = PLAYER_LIVES
        self.score = 0

    def decrease_lives(self):
        self.lives -= 1
        if self.lives <= 0:
            raise GameOver(self.name)

    def add_score(self, points):
        self.score += points


def select_attack():
    return random.choice(list(ALLOWED_ATTACKS.values()))


class Enemy:
    def __init__(self, level, mode):
        self.level = level
        self.lives = PLAYER_LIVES * mode * self.level

    def decrease_lives(self):
        self.lives -= 1
        if self.lives <= 0:
            raise EnemyDown()
