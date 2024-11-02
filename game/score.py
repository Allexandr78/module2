"""Tracking points and records"""

from game.settings import SCORE_FILE, MAX_RECORDS_NUMBER


class GameRecord:
    """Class containing records about players"""

    def __init__(self) -> None:
        """"""
        self.records = []

    def add_record(self, player_record):
        """Add a new record, updating if player already exists with lower score."""
        for record in self.records:
            if record.name == player_record.name and record.mode == player_record.mode:
                # Если запись уже существует, обновляем её
                record.score = player_record.score
                return
        self.records.append(player_record)

    def prepare_records(self):
        """Sort and trim records to max allowed."""
        self.records.sort(reverse=True)
        self.records = self.records[:MAX_RECORDS_NUMBER]


class PlayerRecord:
    """Class for storing a record of one player"""

    def __init__(self, name, mode, score):
        self.name = name
        self.mode = mode
        self.score = score

    def __gt__(self, other):
        return self.score > other.score

    def __str__(self):
        return f"{self.name}\t{self.mode}\t{self.score}"


class ScoreHandler:
    """Glasses Processing Class"""

    def __init__(self, file_name=SCORE_FILE) -> None:
        """"""
        self.file_name = file_name
        self.game_record = GameRecord()
        self.read()

    def read(self):
        """Read scores from file."""
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    if line.strip():  # Пропускаем пустые строки
                        name, mode, score = line.strip().split('\t')
                        record = PlayerRecord(name, mode, int(score))
                        self.game_record.add_record(record)

        except FileNotFoundError:
            print("Score file not found, no previous records to load.")

    def save_score(self, player):
        score_handler = ScoreHandler(SCORE_FILE)
        score_handler.game_record.add_record(PlayerRecord(self.player.name, self.mode, self.player.score))
        score_handler.save()

    def save(self):
        """Saves the game results to a file"""
        with open(self.file_name, 'w') as f:
            for record in self.game_record.records:
                f.write(f"{record.name}\t{record.mode}\t{record.score}\n")

    def display(self) -> None:
        """Displays a list of points in a table."""
        if not self.game_record.records:
            print("No records to display.")
        else:
            print("Name\tMode\tScore")
            for idx, record in enumerate(self.game_record.records, start=1):
                print(f"{idx}. {record}")
