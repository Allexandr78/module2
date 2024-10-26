# main.py
from game.game import Game
from game.models import Player
from game.score import ScoreHandler
from game.settings import MODE_HARD, MODE_NORMAL


def create_player():
    name = input("Enter your name: ")
    difficulty = input("Select mode (1 - Normal, 2 - Hard): ")
    mode = MODE_HARD if difficulty == '2' else MODE_NORMAL
    return Player(name), mode

def play_game():
    player, mode = create_player()
    game = Game(player, mode)
    game.play()

def show_scores():
    ScoreHandler().display()

def main():
    while True:
        choice = input("Choose an option:\n1. Play Game\n2. Show Scores\n3. Exit\n")
        if choice == '1':
            play_game()
        elif choice == '2':
            show_scores()
        elif choice == '3':
            print("Exiting game...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
