from A10_Adventure.Pacman import pacman
from A10_Adventure.Pacman import pacman_level2
from A10_Adventure.Pacman import pacman_level3

def advance_to_next_level(current_level, next_level):
    if current_level.is_game_won():
        print(f"Congratulations! You won level {current_level.level_number}!")
        print("Advancing to the next level...")
        next_level.play_game()  # Assuming play_game() is the function to start the next level

def main():
    # Assuming you create instances of each level
    level1 = pacman()

    level1.play_game()  # Start with the first level


if __name__ == "__main__":
    main()


