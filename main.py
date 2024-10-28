from game.game import Game
from game.models import Player
from game.score import ScoreHandler
from game.settings import MODE_NORMAL, MODE_HARD


def create_player():
    """Создает объект игрока и выбирает сложность"""
    player_name = input("Введите ваше имя: ")
    difficulty_choice = input("Выберите уровень сложности: 1 - Normal, 2 - Hard: ")
    if difficulty_choice == '1':
        mode = MODE_NORMAL
    elif difficulty_choice == '2':
        mode = MODE_HARD
    else:
        print("Неверный выбор, установлен режим по умолчанию: Normal")
        mode = MODE_NORMAL
    return Player(player_name), mode


def play_game():
    player, mode = create_player()
    game = Game(player, mode)
    game.play()


def show_scores():
    ScoreHandler().display()


def main():
    while True:
        print("1. Start Game")
        print("2. Show Scores")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            show_scores()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
