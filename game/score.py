from game.settings import SCORE_FILE, MAX_RECORDS_NUMBER


class ScoreHandler:
    def __init__(self, file_name=SCORE_FILE):
        self.file_name = file_name
        self.game_record = GameRecord()
        self.read()

    def read(self):
        """Read scores from file."""
        try:
            with open(self.file_name, 'r') as file:
                for line in file.readlines()[1:]:
                    name, mode, score = line.strip().split()
                    self.game_record.add_record(PlayerRecord(name, mode, int(score)))
        except FileNotFoundError:
            pass

    def save(self, player_name, mode, score):
        """Сохраняет результаты игры в файл"""
        new_record = PlayerRecord(player_name, mode, score)
        self.game_record.add_record(new_record)
        self.game_record.prepare_records()

        with open(self.file_name, 'w') as file:
            file.write("Name\tMode\tScore\n")
            for record in self.game_record.records:
                file.write(f"{record.name}\t{record.mode}\t{record.score}\n")

        with open(self.file_name, 'w') as file:
            file.write("Name\tMode\tScore\n")
            for record in self.game_record.records:
                file.write(f"{record.name}\t{record.mode}\t{record.score}\n")

    def display(self):
        """Отображает список очков в виде таблицы."""
        # Подготавливаем и сортируем записи
        self.game_record.prepare_records()
        print("Name\tMode\tScore")  # Заголовок таблицы
        for record in self.game_record.records:
            print(record)

class GameRecord:
    def __init__(self):
        self.records = []

    def add_record(self, new_record):
        """Add a new record, updating if player already exists with lower score."""
        for record in self.records:
            if record == new_record and record.score < new_record.score:
                self.records.remove(record)
                break
        self.records.append(new_record)

    def prepare_records(self):
        """Sort and trim records to max allowed."""
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
