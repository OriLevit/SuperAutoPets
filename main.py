import random

import printer
import reader
from game import Game
from board import Board
from shop import Shop

games_to_play = 1

for game in range(games_to_play):

    # Declaring starting values
    current_game = Game(hearts=10, turn=1, gold=10, current_tier=1)
    player_board = Board([])

    # getting all available pets in current tier or below
    available_pets = reader.get_available_pets(current_game.get_current_tier())

    # setup shop with default values -> generate pets list in shop based on tier
    shop = Shop(amount_of_pets_in_shop=3, shop_max_tier=current_game.get_current_tier(), pets_in_shop=[])
    shop.generate_pets(available_pets)

    # print starting message
    printer.print_new_game(current_game)

    print(shop.get_pets_in_shop_names())
    pos_pet_to_buy = random.randint(1,shop.get_amount_of_pets_in_shop())
    pet_to_buy = shop.get_pets_in_shop()[pos_pet_to_buy]
    print(f"{pet_to_buy['name']} -- pos: {pos_pet_to_buy}")


