# Author: Alex
# Date: September 2024
# Description: Chapter 4
def navigate_forest():
    path_blocked = False
    while not path_blocked:
        print("You attempt to navigate the mutated forest.")
        blocked = input("Is the path blocked? (y/n): ")
        if blocked == 'n':
            print("You successfully navigate the forest.")
            path_blocked = True
        else:
            print("The path is blocked. Try another route.")

def gather_samples():
    samples_collected = False
    while not samples_collected:
        print("You collect samples from the forest.")
        collected = input("Did you collect enough samples? (y/n): ")
        if collected == 'y':
            samples_collected = True
        else:
            print("You need to gather more samples.")

def communicate_with_mutated_survivors():
    decision = input("Do you ally with the mutated survivors or avoid them? (Type 'ally' or 'avoid'): ")
    if decision == 'ally':
        print("You ally with the survivors and gain valuable information.")
    elif decision == 'avoid':
        print("You avoid the survivors and bypass potential threats.")
    else:
        print("Invalid choice. Please try again.")
        return communicate_with_mutated_survivors()

def locate_ancient_temple():
    action = input("You locate the ancient temple. Do you enter now or prepare more? (Type 'enter' or 'prepare'): ")
    if action == 'enter':
        print("You enter the temple and proceed to Chapter 5.")
        return 'enter_temple'
    elif action == 'prepare':
        print("You decide to prepare more by gathering samples or communicating with survivors.")
        gather_samples()
    else:
        print("Invalid choice. Please try again.")
        return locate_ancient_temple()