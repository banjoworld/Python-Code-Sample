# Author: Alex
# Date: September 2024
# Description: Chapter 5
def enter_temple():
    print("You enter the ancient temple, filled with puzzles and mysteries.")
    puzzles_solved = False
    while not puzzles_solved:
        solved = input("Did you solve all the puzzles? (y/n): ")
        if solved == 'y':
            puzzles_solved = True
        else:
            print("You failed the puzzle. Try again.")