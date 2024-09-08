# Author: Alex
# Date: September 2024
# Description: Chapter 2
def navigate_ruins():
    print("You make your way through the ruins, avoiding hazards and pitfalls.")
    path = input("Do you take the safe route or the shortcut? (Type 'safe' or 'shortcut'): ")
    if path == 'safe':
        print("You choose the safe route, progressing without issue.")
    elif path == 'shortcut':
        print("You encounter some hazards along the way.")
    else:
        print("Invalid choice. Please try again.")
        return navigate_ruins()

def scavenge_for_resources():
    resources_found = False
    while not resources_found:
        print("You search for valuable resources in the ruins.")
        found = input("Did you find enough resources? (y/n): ")
        if found == 'y':
            resources_found = True
        else:
            print("You continue scavenging.")
    print("You have gathered enough resources.")

def interact_with_survivors():
    decision = input("Do you trust the survivors or defend yourself? (Type 'trust' or 'defend'): ")
    if decision == 'trust':
        print("You decide to trust the survivors and form an alliance.")
    elif decision == 'defend':
        print("You decide to defend yourself, leading to a conflict.")
    else:
        print("Invalid choice. Please try again.")
        return interact_with_survivors()

def discover_hidden_bunker():
    action = input("You discover a hidden bunker. Do you enter the bunker or continue scavenging? (Type 'enter' or 'scavenge'): ")
    if action == 'enter':
        print("You enter the bunker and proceed to Chapter 3.")
        return 'enter_bunker'
    elif action == 'scavenge':
        print("You decide to continue scavenging.")
        scavenge_for_resources()
    else:
        print("Invalid choice. Please try again.")
        return discover_hidden_bunker()