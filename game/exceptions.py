class GameOver(Exception):
    def __init__(self, player_name):
        self.player_name = player_name


class EnemyDown(Exception):
    pass
