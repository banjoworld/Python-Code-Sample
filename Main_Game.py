# Author: Alex
# Date: September 2024
# Description: Main Game
import Chapter1
import Chapter2
import Chapter3
import Chapter4
import Chapter5

def start_game():
    # Chapter 1
    Chapter1.introduction_scene()
    Chapter1.assess_or_gather()
    Chapter1.search_wreckage()
    Chapter1.establish_temporary_base()
    Chapter1.rest_or_explore()

    # Chapter 2
    Chapter2.navigate_ruins()
    Chapter2.scavenge_for_resources()
    Chapter2.interact_with_survivors()
    Chapter2.discover_hidden_bunker()

    # Chapter 3
    Chapter3.investigate_bunker()
    Chapter3.solve_security_puzzles()
    Chapter3.repair_systems()
    Chapter3.hack_terminal()

    # Chapter 4
    Chapter4.navigate_forest()
    Chapter4.gather_samples()
    Chapter4.communicate_with_mutated_survivors()
    Chapter4.locate_ancient_temple()

    # Chapter 5
    Chapter5.enter_temple()

if __name__ == "__main__":
    start_game()