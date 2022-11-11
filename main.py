import printer
import reader
from game import Game
from board import Board
from shop import Shop

games_to_play = 1

for game in range(games_to_play):
    current_game = Game(hearts=10, turn=1, gold=10, current_tier=1)
    board = Board(0, [])
    shop = Shop(3, current_game.get_current_tier())
    #all_pets = reader.get_pet_list()
    available_pets = reader.get_available_pets(current_game.get_current_tier())

    printer.print_new_game(current_game)
    available_pets_names = reader.get_pet_list_names(available_pets)
