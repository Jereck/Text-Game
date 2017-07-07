from abstractgameunit import AbstractGameUnit
from gameutils import print_bold

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
