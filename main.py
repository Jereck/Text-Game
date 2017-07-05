import random
import textwrap
import sys

if sys.version_info < (3, 0):
    print("This code requires Python 3.x and is tested with version 3.5.x ")
    print("Looks like you are trying to run this using "
          "Python version: %d.%d " % (sys.version_info[0],
                                      sys.version_info[1]))
    print("Exiting...")
    sys.exit(1)


def show_theme_message(width):
    """Print the game theme in the terminal window"""
    print_dotted_line()
    print_bold("Viking Warrior v0.0.5:")
    msg = (
        "You were once a proud warrior who ran away from battle."
        "This is extremely frowned upon in your home land and for your"
        "betrayal, they banished to the the world of the humans. On a"
        "mission to redeem yourself, you stumble upon a castle. The king"
        "sees your sword and shield and immediatly asks you for help."
        "The princess is missing, and the orcs are invading the village."
        "You see this as a chance to redeem yourself, and save these people")

    print(textwrap.fill(msg, width=width))


def show_game_mission():
    """Print the game mission in the terminal window"""
    print_bold("Mission:")
    print("\tChoose a house to search...")
    print_dotted_line()


def reveal_occupants(idx, houses):
    """Print the occupants of the hut"""
    msg = ""
    print("Revealing the occupants...")
    for i in range(len(houses)):
        occupant_info = "<%d:%s>" % (i+1, houses[i])
        if i + 1 == idx:
            occupant_info = occupant_info
        msg += occupant_info + " "

    print("\t" + msg)
    print_dotted_line()


def occupy_houses():
    """Randomly populate the `houses` list with occupants"""
    huts = []
    occupants = ['enemy', 'friend', 'unoccupied']
    while len(houses) < 5:
        computer_choice = random.choice(occupants)
        houses.append(computer_choice)
    return houses


def process_user_choice():
    """Accepts the house number from the user"""
    msg = "Choose a house number to enter (1-5): "
    user_choice = input("\n" + msg)
    idx = int(user_choice)
    return idx


def show_health(health_meter, bold=False):
    """Show the remaining hit points of the player and the enemy"""
    msg = "Health: You: %d, Enemy: %d" \
          % (health_meter['player'], health_meter['enemy'])

    if bold:
        print_bold(msg)
    else:
        print(msg)


def reset_health_meter(health_meter):
    """Reset the values of health_meter dict to the original ones"""
    health_meter['player'] = 40
    health_meter['enemy'] = 30


def print_bold(msg, end='\n'):
    """Print a string in 'bold' font"""
    print(msg, end=end)


def print_dotted_line(width=72):
    """Print a dotted (rather 'dashed') line"""
    print('-'*width)

def attack(health_meter):
    """The main logic to determine injured unit and amount of injury"""
    hit_list = 4 * ['player'] + 6 * ['enemy']
    injured_unit = random.choice(hit_list)
    hit_points = health_meter[injured_unit]
    injury = random.randint(10, 15)
    health_meter[injured_unit] = max(hit_points - injury, 0)
    print("ATTACK! ", end='')
    show_health(health_meter)


def play_game(health_meter):
    """The main control function for playing the game"""
    houses = occupy_houses()
    idx = process_user_choice()
    reveal_occupants(idx, houses)

    if houses[idx - 1] != 'enemy':
        print_bold("Congratulations! YOU WIN!!!")
    else:
        print_bold('ENEMY SIGHTED! ', end='')
        show_health(health_meter, bold=True)
        continue_attack = True

        # Loop that actually runs the combat if user wants to attack
        while continue_attack:
            continue_attack = input(".......continue attack? (y/n): ")
            if continue_attack == 'n':
                print_bold("RUNNING AWAY with following health status...")
                show_health(health_meter, bold=True)
                print_bold("GAME OVER!")
                break

            attack(health_meter)

            # Check if either one of the opponents is defeated
            if health_meter['enemy'] <= 0:
                print_bold("GOOD JOB! Enemy defeated! YOU WIN!!!")
                break

            if health_meter['player'] <= 0:
                print_bold("YOU LOSE  :(  Better luck next time")
                break


def run_application():
    """Top level control function for running the application."""
    keep_playing = 'y'
    health_meter = {}
    reset_health_meter(health_meter)
    show_game_mission()

    while keep_playing == 'y':
        reset_health_meter(health_meter)
        play_game(health_meter)
        keep_playing = input("\nPlay again? Yes(y)/No(n): ")


if __name__ == '__main__':
    run_application()
