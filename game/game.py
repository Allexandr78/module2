"""Main game class"""

from game.exceptions import GameOver, EnemyDown
from game.models import Enemy
from game.score import ScoreHandler, PlayerRecord
from game.settings import ATTACK_PAIRS_OUTCOME, POINTS_FOR_FIGHT, WIN, LOSE, HARD_MODE_MULTIPLIER, MODES, SCORE_FILE


class Game:
    """Main class"""

    def __init__(self, player, mode) -> None:
        """Player object and difficulty level, creates first opponent"""
        self.player = player
        self.mode = mode
        self.mode_multiplier = HARD_MODE_MULTIPLIER if mode == MODES['2'] else 1
        self.enemy = self.create_enemy()

    def create_enemy(self) -> Enemy:
        """Create a new enemy with an increased level."""
        return Enemy(level=self.enemy.level + 1 if hasattr(self, 'enemy') else 1, mode_multiplier=self.mode_multiplier)

    def play(self) -> None:
        """Play the game in a loop until GameOver or EnemyDown."""
        try:
            while True:
                self.fight()
        except GameOver:
            print("Game Over!")
            self.save_score()
        except EnemyDown:
            print("Enemy defeated! A new, stronger enemy appears.")
            self.save_score()
            self.enemy = self.create_enemy()
        except KeyboardInterrupt:
            print("Game interrupted.")

    def fight(self):
        """Execute one fight round between player and enemy."""
        player_attack = self.player.select_attack()
        enemy_attack = self.enemy.select_attack()
        result = ATTACK_PAIRS_OUTCOME[(player_attack, enemy_attack)]
        self.handle_fight_result(result)

    def handle_fight_result(self, result) -> None:
        """Handles the result of each round."""
        if result == WIN:
            print("You WIN this move!")
            self.player.add_score(POINTS_FOR_FIGHT)
            self.enemy.decrease_lives()
        elif result == LOSE:
            print("You lost this move!")
            self.player.decrease_lives()
        else:
            print("It's a draw!")

        print(f"Player lives: {self.player.lives}, Score: {self.player.score}")
        print(f"Enemy lives: {self.enemy.lives}")

    def save_score(self):
        """Saving points after the game ends"""
        handler = ScoreHandler(SCORE_FILE)
        handler.read()
        handler.game_record.add_record(PlayerRecord(self.player.name, self.mode, self.player.score))
        handler.save()
