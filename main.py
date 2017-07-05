import random
import textwrap

def show_theme_message():
    print(dotted_line)
    print("Viking Warrior v0.0.1:")
    msg = (
        "You died in battle as a brave warrior many years ago. Now you find yourself"
        "risen from Valhalla but you don't know why. In your search for answers you"
        "stumble upon a castle. The townsfolk and King of this land are upset. Their"
        "precious princess has disappeared. Seeing your shield and sword, the King"
        "asks you for your help."
        )
    print(textwrap.fill(msg, width = width))


def show_game_mission():
    print("Mission:")
    print("\tChoose a place where you can rest...")
    print(dotted_line)


def occupy_zones():
    while keep_playing == 'y':
        zones = []
        # Randomly append 'enemy' or 'friend' or None to the zones list
        while len(zones) < 5:
            computer_choice = random.choice(occupants)
            zones.append(computer_choice)


def process_user_choice():
    # Prompt user to select a huts
    msg = "Choose a zone to ender (1-5): "
    user_choice = input("\n" + msg)
    idx = int(user_choice)
    # Print the occupant info
    print("Revealing the occupants...")
    msg = ""


def reveal_occupants():
    for i in range(len(zones)):
        occupant_info = "<%d:%s>"%(i + 1, zones[i])
        if i + 1 == idx:
            occupant_info = occupant_info
        msg += occupant_info + " "
    print("\t" + msg)
    print(dotted_line)


def enter_zone():
    print("Entering zone %d... " % idx, end = ' ')

    # Determine and annouce the winnder
    if zones[idx - 1] == "enemy":
        print("YOU LOSE :( Better luck next time!")
    else:
        print("Congratulations! YOU WIN!!!")
    print(dotted_line)
    keep_playing = input("Play again? Yes(y)/No(n)")


def run_application():
    keep_playing = 'y'
    width = 72
    dotted_line = '-' * width

    show_theme_message(dotted_line, width)
    show_game_mission(dotted_line)

    while keep_playing == 'y':
        zones = occupy_zones()
        idx = process_user_choice()
        reveal_occupants(idx, zones, dotted_line)
        enter_zone(idx, zones, dotted_line)
        keep_playing = input("Play again? Yes(y)/No(n):")


if __name__ == '__main__':
    run_application()
    occupants = ['enemy', 'friend', 'unoccupied']
