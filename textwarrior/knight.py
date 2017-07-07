from abstractgameunit import AbstractGameUnit
from gameutils import print_bold

class Knight(AbstractGameUnit):
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
        is_enemy = (isinstance(house.occupant, AbstractGameUnit) and house.occupant.unit_type == 'enemy')
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
