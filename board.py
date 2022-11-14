from Pet import Pet
from game import Game
from shop import Shop


class Board:
    def __init__(self, pets: list):
        self.pets = pets

    # region GET methods
    def get_pets(self):
        return self.pets

    # endregion

    # region GET methods
    def set_pets(self, pets):
        self.pets = pets

    # endregion

    def add_pet(self, pet:Pet, position:int):
        if len(self.pets) >= position and self.pets[position] is not None:
            self.pets[position] = pet

    def remove_pet(self, position: int):
        if len(self.pets) >= position and self.pets[position] is not None:
            self.pets[position] = None
