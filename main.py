import random
import textwrap

from sys import exit

if __name__ == '__main__':
    width = 72
    dotted_line = '-' * width
    print(dotted_line)
    print("Textual Warrior v0.0.1")
    msg = (
        "A long time ago, a warrior from Valhala came to a town "
        "because he heard the people were in need. Their princess "
        "has diappeared and the town is lost without her. The warrior "
        "is going to have to travel to distant lands to save her. "
        "You are that warrior...")

    print(textwrap.fill(msg, width = width))
    print(dotted_line)



def woods():
    #Enter the first wooded area of the game
    print("You have entered a dark wooded area.")
    print("Do you want to continue through the woods or turn around?")
    print("""
        'continue' - to continue on through the woods
        'go back' - to turn back out of the woods
    """)

    choice = input("> ")

    if choice == "continue":
        deeper_woods()
    else:
        castle_grounds()

def deeper_woods():
    #Continue deeper into the woods
    print("You have gone deeper into the woods")
    print("You hear a grumbling noise in the dark")
    #Spawns a monster

def mountains():
    print("It's cold here in the mountains, but you see a fire in the distance")
    print("Do you want to move closer to the fire?")
    print("""
        'yes' - move to the fire
        'no' - go back to the castle grounds
    """)

    choice = input("> ")

    if choice == 'yes':
        mountain_fire()
    else:
        castle_grounds()

def mountain_fire():
    print("You notice that it's not a fire, but a dragon!")
    print("You also notice that the princess is by the dragons tail")

def valley():
    print("You go the the valley and just see a bunch of villagers.")
    print("They great you with a smile, but it's makes you feel uneasy.")

def castle_grounds():
    print("Villager: Thank you! Please save our princess...")
    print("Which way would you like to go?")
    print("""
        'woods' - enter the woods
        'mountains' - head to the mountains
        'valley' - head down to the valley
    """)


    choice = input("> ")

    if choice == "woods":
        woods()
    elif choice == "mountains":
        mountains()
    else:
        valley()


# the start of the game
def start():
    print("Welcome brave Warrior. We need you to find the princess!")
    print("What is your name?")

    name = input("> ")

    print(f"Please, {name}, will you help us save our princess?")
    print("Y - Yes :: N - No")

    answer = input("> ")

    if answer == "Y" or answer == "y":
        castle_grounds()

    if answer == "N" or answer == "n":
        exit(0)

    return name

start()
