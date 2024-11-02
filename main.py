"""Main module."""

from game.game import Game
from game.models import Player
from game.score import ScoreHandler
from game.settings import MODES


def play_game() -> None:
    """Play game"""
    name = input("Enter your name: ")
    mode = input("Choose difficulty (1 for Normal, 2 for Hard): ")
    player = Player(name)
    game = Game(player, MODES[mode])
    game.play()


def show_scores() -> None:
    """Displays scores"""
    ScoreHandler().display()


def exit_game() -> None:
    """Exits the game"""
    print("Exiting game.")
    exit()


def main() -> None:
    """Main menu"""
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
            exit_game()
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
