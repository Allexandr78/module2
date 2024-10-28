from game.exceptions import GameOver, EnemyDown
from game.models import Enemy
from game.score import ScoreHandler
from game.settings import POINTS_FOR_KILLING, ATTACK_PAIRS_OUTCOME, POINTS_FOR_FIGHT, SCORE_FILE, WIN, LOSE, DRAW


class Game:
    def __init__(self, player, mode):
        self.enemy = None
        self.player = player
        self.mode = mode
        self.create_enemy()

    def create_enemy(self):
        """Create a new enemy with an increased level."""
        level = self.enemy.level + 1 if self.enemy is not None else 1
        self.enemy = Enemy(level, self.mode)

    def play(self):
        """Play the game in a loop until GameOver or EnemyDown."""
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
        """Execute one fight round between player and enemy."""
        player_attack = self.player.select_attack()
        enemy_attack = self.enemy.select_attack()
        return ATTACK_PAIRS_OUTCOME[(player_attack, enemy_attack)]

    def handle_fight_result(self, result):
        """Handles the result of each round."""
        if result == WIN:
            print("Вы выиграли этот ход!")
            self.enemy.decrease_lives()  # Уменьшение жизней противника
            self.player.add_score(POINTS_FOR_FIGHT)  # Добавление очков за победу в ходу
        elif result == LOSE:
            print("Вы проиграли этот ход!")
            self.player.decrease_lives()  # Уменьшение жизней игрока
        elif result == DRAW:
            print("Ничья!")

    def save_score(self):
        """Сохранение очков после окончания игры"""
        player_name = self.player.name
        mode = self.mode  # должно быть 'Normal' или 'Hard'
        score = self.player.score
        ScoreHandler(SCORE_FILE).save(player_name, mode, score)
