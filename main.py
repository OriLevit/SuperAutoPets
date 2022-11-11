import printer
import reader
from game import Game

games_to_play = 1

for game in range(games_to_play):
    current_game = Game(hearts=10, turn=1, gold=10, current_tier=1)
    printer.print_new_game(current_game)
    all_pets = reader.get_pet_list()
    available_pets = reader.get_available_pets(1)
    available_pets_names = reader.get_pet_list_names(available_pets)
    print(available_pets_names)
