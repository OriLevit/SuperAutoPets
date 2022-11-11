from game import Game


def print_new_game(current_game: Game):
    print("Started new game! \n"
          f" Tier: {current_game.get_current_tier()} \n"
          f" Turn: {current_game.get_turn()} \n"
          f" Hearts: {current_game.get_hearts()} \n"
          f" Gold: {current_game.get_gold()}")
