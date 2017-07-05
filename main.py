from __future__ import print_function

import random
import sys

if sys.version_info < (3, 0):
    print("This code requires Python 3.x and is tested with version 3.5.x ")
    print("Looks like you are trying to run this using "
          "Python version: %d.%d " % (sys.version_info[0],
                                      sys.version_info[1]))
    print("Exiting...")
    sys.exit(1)

def weighted_random_selection(obj1, obj2):
    weighted_list = 3 * [id(obj1)] + 7 * [id(obj2)]
    selection = random.choice(weighted_list)

    if selection == id(obj1):
        return obj1

    return obj2


def print_bold(msg, end='\n'):
    """Print a string in 'bold' font"""
    print(msg, end=end)


class GameUnit:
    """Base class for creating various game characters"""
    def __init__(self, name=""):
        self.max_hp = 0
        self.health_meter = 0
        self.name = name
        self.enemy = None
        self.unit_type = None

    def info(self):
        """Info on the unit to be overridden by subclass"""
        pass

    def attack(self, enemy):
        """
        The main logic to determine injured unit and amount of injury
        """
        injured_unit = weighted_random_selection(self, enemy)
        injury = random.randint(10, 15)
        injured_unit.health_meter = max(injured_unit.health_meter - injury, 0)
        print("ATTACK! ", end='')
        self.show_health(end=' ')
        enemy.show_health(end=' ')

    def heal(self, heal_by=2, full_healing=True):
        """Heals the character by all hit points"""
        if self.health_meter == self.max_hp:
            return

        if full_healing:
            self.health_meter == self.max_hp
        else:
            #This can exceed max hit points FIX LATER
            self.health_meter += heal_by

        print_bold("You are fully healed!", end =' ')
        self.show_health(bold=True)

    def reset_health_meter(self):
        """Reset the values of health_meter"""
        self.health_meter = self.max_hp

    def show_health(self, bold=False, end='\n'):
        """Show the remaining hit points of the player and the enemy"""
        # FIX FOR NO ENEMY
        msg = "Health: %s: %d" % (self.name, self.health_meter)

        if bold:
            print_bold(msg, end=end)
        else:
            print(msg, end=end)


class Knight(GameUnit):
    """
    Class for the Knight Unit

    The instance for the play is as the Knight class right now. Will add other
    classes for players later
    """
    def __init__(self, name="Knight"):
        super().__init__(name=name)
        self.max_hp = 40
        self.health_meter = self.max_hp
        self.unit_type = 'friend'

    def info(self):
        """ Prints out the basic information for this unit """
        print("I am a Knight!")

    def acquire_house(self, house):
        """ Fight to acquire the hosue"""
        print_bold("Entering house %d..." % house.number, end=' ')
        is_enemy = (isinstance(house.occupant, GameUnit) and house.occupant.unit_type == 'enemy')
        continue_attack = 'y'
        if is_enemy:
            print_bold("Enemy sighted!")
            self.show_health(bold=True, end=' ')
            house.occupant.show_health(bold=True, end=' ')
            while continue_attack:
                continue_attack = input(".... continue attack? (y/n): ")
                if continue_attack == 'n':
                    self.run_away()
                    break

                self.attack(house.occupant)

                if house.occupant.health_meter <= 0:
                    print("")
                    house.acquire(self)
                    break
                if self.health_meter <= 0:
                    print("")
                    break
        else:
            if house.get_occupant_type() == 'unoccupied':
                print_bold("House is empty")
            else:
                print_bold("There is an ally in here")
            house.acquire(self)
            self.heal()

    def run_away(self):
        """
        Run away from the house
        """
        print_bold("RUN AWAY!")
        self.enemy = None


class OrcRider(GameUnit):
    """This class represents the enemy/Orc"""
    def __init__(self, name=''):
        super().__init__(name=name)
        self.max_hp = 30
        self.health_meter = self.max_hp
        self.unit_type = 'enemy'
        self.house_number = 0

    def info(self):
        """ Print basic information on the Orc"""
        print("We Orc are strong warrior. Turn back now!")


class House:
    def __init__(self, number, occupant):
        self.occupant = occupant
        self.number = number
        self.is_acquired = False

    def acquire(self, new_occupant):
        """ Updates whether occupied or not"""
        self.occupant = new_occupant
        self.is_acquired = True
        print_bold("GOOD JOB! House %d acquired" % self.number)

    def get_occupant_type(self):
        """ Returns info on house occupants"""
        if self.is_acquired:
            occupant_type = 'ACQUIRED'
        elif self.occupant is None:
            occupant_type = 'unoccupied'
        else:
            occupant_type = self.occupant.unit_type

        return occupant_type


class ReturnOfTheWarrior:
    """ Acts as the main class of the game"""
    def __init__(self):
        self.houses = []
        self.player = None

    def get_occupants(self):
        """ Returns a list of occupants in all the houses"""
        return [x.get_occupant_type() for x in self.houses]

    def show_game_mission(self):
        """Print the game mission in the terminal window"""
        print("Your Mission:")
        print(" - Defeat all the Orcs.")
        print(" - Regain control of all the houses in the village.")
        print("---------------------------------------------------\n")

    def _process_user_choice(self):
        """Takes user input for choice of houses to enter"""
        verifiying_choice = True
        idx = 0
        print("Current occupants: %s" % self.get_occupants())
        while verifiying_choice:
            user_choice = input("Choose a house number to enter (1-5): ")
            idx = int(user_choice)
            if self.houses[idx-1].is_acquired:
                print("You already cleared this house of Orcs, or a friend lives in it."
                    "Please try to clear another house")
            else:
                verifiying_choice = False

        return idx

    def _occupy_houses(self):
        """Randomly populate the `houses` list with occupants"""
        for i in range(5):
            choice_lst = ['enemy', 'friend', None]
            computer_choice = random.choice(choice_lst)
            if computer_choice == 'enemy':
                name = 'enemy-' + str(i + 1)
                self.houses.append(House(i+1, OrcRider(name)))
            elif computer_choice == 'friend':
                name = 'knight-' + str(i+1)
                self.houses.append(House(i+1, Knight(name)))
            else:
                self.houses.append(House(i+1, computer_choice))


    def play(self):
        """ This is what controls the logic of the game.
        As well as the main method that begins game execution"""

        self.player = Knight()
        self._occupy_houses()
        acquired_house_counter = 0

        self.show_game_mission()
        self.player.show_health(bold=True)

        while acquired_house_counter < 5:
            idx = self._process_user_choice()
            self.player.acquire_house(self.houses[idx-1])

            if self.player.health_meter <= 0:
                print_bold("YOU LOSE! Try again later")
                break

            if self.houses[idx-1].is_acquired:
                acquired_house_counter += 1

        if acquired_house_counter == 5:
            print_bold("Congratulations! You cleared all the houses of Orcs!")

if __name__ == '__main__':
    game = ReturnOfTheWarrior()
    game.play()
