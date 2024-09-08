# Author: Alex
# Date: September 2024
# Description: Chapter 3
def investigate_bunker():
    clues_found = False
    while not clues_found:
        print("You search the bunker for clues.")
        found = input("Did you find all the clues? (y/n): ")
        if found == 'y':
            clues_found = True
        else:
            print("You continue investigating the bunker.")

def solve_security_puzzles():
    puzzle_solved = False
    while not puzzle_solved:
        print("You attempt to solve a security puzzle.")
        solved = input("Did you solve the puzzle? (y/n): ")
        if solved == 'y':
            puzzle_solved = True
        else:
            print("You failed the puzzle. Try again.")

def repair_systems():
    repair_successful = False
    while not repair_successful:
        print("You attempt to repair the bunker systems.")
        repair = input("Did you repair the systems successfully? (y/n): ")
        if repair == 'y':
            repair_successful = True
        else:
            print("You failed to repair the systems. Try again.")

def hack_terminal():
    action = input("Do you want to proceed or investigate more? (Type 'proceed' or 'investigate'): ")
    if action == 'proceed':
        print("You proceed to the next chapter.")
        return 'proceed'
    elif action == 'investigate':
        print("You decide to investigate the bunker more.")
        investigate_bunker()
    else:
        print("Invalid choice. Please try again.")
        return hack_terminal()