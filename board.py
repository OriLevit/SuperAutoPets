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

    def buy_pet(self, pet: Pet, position: int, game: Game,price=3):
        if game.get_gold() >2 and len(self.pets) >= position and self.pets[position] is not None:
            self.pets[position] = pet
            game.reduce_gold(price)

    def sell_pet(self, position: int, game: Game, price=1):
        if len(self.pets) >= position and self.pets[position] is not None:
            self.pets[position] = None
            game.add_gold(price)
