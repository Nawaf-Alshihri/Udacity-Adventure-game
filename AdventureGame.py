import time
import random


# Print text to the console and wait a specified number of seconds.
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


# Print text to the consol at the start of the game.
def intro(items, monster, weapon):
    print_pause("You find yourself standing in an open field, filled with"
                " grass and yellow wildflowers.\n")
    print_pause(f"Rumor has it that a {monster} is somewhere around here, "
                "and has been terrifying the nearby village.\n")
    print_pause("In front of you is a house.\n")
    print_pause("To your right is a dark cave.\n")
    print_pause("To your left is a village at a distance.\n")
    print_pause("In your hand you hold your trusty"
                " (but not very effective) dagger.\n")


# text displied to select path.
def choose_path(items, monster, weapon):
    print_pause("Enter 1 to knock on the door of the house.\n")
    print_pause("Enter 2 to peer into the cave.\n")
    print_pause("Enter 3 to go to the village.\n")
    print_pause("What would you like to do?")
    path = input("1 , 2 or 3\n")
    if path == '1':
        house(items, monster, weapon)
    elif path == '2':
        cave(items, monster, weapon)
    elif path == '3':
        village(items, monster, weapon)
    else:
        choose_path(items, monster, weapon)


# text displied when you select path to the cave.
def cave(items, monster, weapon):
    print_pause("You peer cautiously into the cave.")
    if len(items) != 0:
        print_pause("You've been here before, and gotten "
                    "all the good stuff. It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause(f"You have found the magical {weapon} of Ogoroth!")
        print_pause(f"You discard your silly old dagger"
                    " and take the {weapon} with you.")
        items.append(weapon)
    print_pause("You walk back out to the field.")
    choose_path(items, monster, weapon)


# text displied when you select path to the house.
def house(items, monster, weapon):
    print_pause("You approach the door of the house.\n")
    print_pause(f"You are about to knock when the door"
                f" opens and out steps a {monster}.\n")
    print_pause(f"Eep! This is the {monster}'s house!\n")
    print_pause(f"The {monster} attacks you!\n")
    if len(items) == 0:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.\n")
    while True:
        choice = input("Would you like to (1) fight or (2) run away?\n")
        if choice == "1":
            if len(items) > 0:
                print_pause(f"As the {monster} moves to attack, you "
                            f"unsheath your new {monster}.\n")
                print_pause(f"The {weapon} of Ogoroth shines brightly in"
                            " your hand as you brace yourself"
                            " for the attack.\n")
                print_pause(f"But the {monster} takes one look at your "
                            "shiny new toy and runs away!\n")
                print_pause(f"You have rid the town of the {monster}"
                            ". You are victorious!\n")
            else:
                print_pause("You do your best...\n")
                print_pause(f"but your dagger is no match for the "
                            f"{monster}.\n")
                print_pause("You have been defeated!\n")
            play_again()
            break
        if choice == "2":
            print_pause("You run back into the field. Luckily, "
                        "you don't seem to have been followed.\n")
            choose_path(items, monster, weapon)
            break
        choose_path(items, monster, weapon)


#  text displied when you select path to the village
def village(items, monster, weapon):
    print_pause("You enter the empty village and walk between the farmhouses.")
    print_pause("the doors are closed and the windows are boarded up.")
    print_pause("No one is walking outside , event the farm animal "
                "are kept inside their barns.")
    print_pause(f"You knock on the nearest door , a scared voice ansewrs"
                f" : go away, it is not safe for you here. "
                f"there is a {monster} raoming at night.")
    print_pause("You walk back out to the field.")
    choose_path(items, monster, weapon)


# text displied to select if the palyer wants to paly again.
def play_again():
    while True:
        answer = input("Would you like to play again? (y/n)\n")
        if answer == "y":
            print_pause("Excellent! Restarting the game ...\n")
            play_game()
            break
        elif answer == "n":
            print_pause("Thanks for playing! See you next time.\n")
        else:
            play_again()
            break


# the main function if the game.
def play_game():
    monster_list = ["gorgon", "wicked fairy", "mighty pirate",
                    "hideous troll", "dark ninja", "giant dragon"]
    monster = random.choice(monster_list)
    weapon_list = ["sword", "axe", "machete", "Javelin",
                   "Warhammer", "wand", "katana"]
    weapon = random.choice(weapon_list)
    items = []
    intro(items, monster, weapon)
    choose_path(items, monster, weapon)


if __name__ == "__main__":
    play_game()
