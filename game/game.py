# game.py
from models import  Enemy, select_attack
from settings import  POINTS_FOR_FIGHT, POINTS_FOR_KILLING, ATTACK_PAIRS_OUTCOME
from score import ScoreHandler
from exceptios import GameOver, EnemyDown

class Game:
    def __init__(self, player, mode):
        self.enemy = None
        self.player = player
        self.mode = mode
        self.create_enemy()

    def create_enemy(self):
        level = self.enemy.level + 1 if hasattr(self, 'enemy') else 1
        self.enemy = Enemy(level, self.mode)

    def play(self):
        try:
            while True:
                result = self.fight()
                self.handle_fight_result(result)
        except GameOver:
            print("Game Over! Saving your score...")
            self.save_score()
        except EnemyDown:
            print("Enemy defeated! New enemy incoming.")
            self.player.add_score(POINTS_FOR_KILLING)
            self.create_enemy()

    def fight(self):
        player_attack = self.player.select_attack()
        enemy_attack = select_attack()
        return ATTACK_PAIRS_OUTCOME[(player_attack, enemy_attack)]

    def handle_fight_result(self, result):
        if result == 1:
            self.enemy.decrease_lives()
            self.player.add_score(POINTS_FOR_FIGHT)
        elif result == -1:
            self.player.decrease_lives()

    def save_score(self):
        ScoreHandler("scores.txt").save(self.player)
