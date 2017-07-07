from abstractgameunit import AbstractGameUnit
from gameutils import print_bold

class OrcRider(AbstractGameUnit):
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
