
from settings import SCORE_FILE, MAX_RECORDS_NUMBER


class ScoreHandler:
    def __init__(self, file_name=SCORE_FILE):
        self.mode = None
        self.file_name = file_name
        self.game_record = GameRecord()
        self.read()

    def read(self):
        try:
            with open(self.file_name, 'r') as file:
                for line in file.readlines()[1:]:
                    name, mode, score = line.strip().split()
                    self.game_record.add_record(PlayerRecord(name, mode, int(score)))
        except FileNotFoundError:
            pass

    def save(self, player):
        self.game_record.add_record(PlayerRecord(player.name, self.mode, player.score))
        self.game_record.prepare_records()
        with open(self.file_name, 'w') as file:
            file.write("Name\tMode\tScore\n")
            for record in self.game_record.records:
                file.write(f"{record}\n")

    def display(self):
        """Отображает список очков в виде таблицы."""

        self.game_record.prepare_records()
        print("Name\tMode\tScore")
        for record in self.game_record.records:
            print(record)

class GameRecord:
    def __init__(self):
        self.records = []

    def add_record(self, new_record):
        for record in self.records:
            if record == new_record and record.score < new_record.score:
                self.records.remove(record)
                break
        self.records.append(new_record)

    def prepare_records(self):
        self.records.sort(reverse=True)
        self.records = self.records[:MAX_RECORDS_NUMBER]

class PlayerRecord:
    def __init__(self, name, mode, score):
        self.name = name
        self.mode = mode
        self.score = score

    def __gt__(self, other):
        return self.score > other.score

    def __str__(self):
        return f"{self.name}\t{self.mode}\t{self.score}"
