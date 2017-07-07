import random
from house import House
from knight import Knight
from orcrider import OrcRider
from gameutils import print_bold

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
            try:
                idx = int(user_choice)
            except ValueError as e:
                print("Invalid input, args: %s \n" % e.args)
                continue

            try:
                if self.houses[idx-1].is_acquired:
                    print("You already cleared this house of Orcs, or a friend lives in it."
                    "Please try to clear another house")
                else:
                    verifiying_choice = False
            except IndexError:
                print("Invalid input : ", idx)
                print("Number should be in the range of 1 to 5. Try again")
                continue
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
