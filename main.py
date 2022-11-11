import printer
from game import Game

games_to_play = 1

for game in range(games_to_play):
    current_game = Game(hearts=10, turn=1, gold=10,current_tier=1)
    printer.print_new_game(current_game)

