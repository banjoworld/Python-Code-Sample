# Author: Alex
# Date: September 2024
# Description: Chapter 1
def introduction_scene():
    print("You wake up amidst the wreckage of your spacecraft, dazed and confused.")
    print("The AI voice crackles to life, 'Captain, are you operational?'")

def interact_with_ai():
    responses = ["Assessing damage...", "Gathering data...", "Do you want to assess the damage or gather supplies?"]
    print("AI: ", responses[0])
    print("AI: ", responses[1])
    action = input("AI: " + responses[2] + " (Type 'assess' or 'gather'): ")
    return action

def assess_or_gather():
    action = interact_with_ai()
    if action == 'assess':
        print("You begin assessing the damage to the ship.")
        return 'assess'
    elif action == 'gather':
        print("You decide to gather supplies from the wreckage.")
        return 'gather'
    else:
        print("Invalid choice. Please try again.")
        return assess_or_gather()

def search_wreckage():
    supplies_found = False
    while not supplies_found:
        print("You search through the wreckage for supplies...")
        found = input("Did you find enough supplies? (y/n): ")
        if found == 'y':
            supplies_found = True
        else:
            print("You continue searching the wreckage.")
    print("You have gathered enough supplies.")

def establish_temporary_base():
    print("You set up a temporary base near the wreckage.")
    print("You now have shelter and some basic supplies.")

def rest_or_explore():
    action = input("Do you want to rest or explore further? (Type 'rest' or 'explore'): ")
    if action == 'rest':
        print("You decide to rest for a while.")
    elif action == 'explore':
        print("You decide to explore the surrounding area.")
        explore_surroundings()
    else:
        print("Invalid choice. Please try again.")
        return rest_or_explore()

def explore_surroundings():
    print("You venture out from your temporary base, searching the surrounding area.")
    map_found = False
    while not map_found:
        found = input("Did you find a map? (y/n): ")
        if found == 'y':
            map_found = True
        else:
            print("You continue exploring the surroundings.")
    print("You have found a map.")