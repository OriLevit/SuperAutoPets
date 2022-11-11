class Game:
    def __init__(self, hearts, turn, gold, current_tier):
        self.hearts = hearts
        self.turn = turn
        self.gold = gold
        self.current_tier = current_tier
        self.wins = 0

    # region GET methods
    def get_hearts(self):
        return self.hearts

    def get_turn(self):
        return self.turn

    def get_gold(self):
        return self.gold

    def get_current_tier(self):
        return self.current_tier

    def get_wins(self):
        return self.wins
    # endregion

    # region SET methods
    def set_gold(self, gold):
        self.gold = gold

    def set_hearts(self, hearts):
        self.hearts = hearts

    def set_turn(self, turn):
        self.turn = turn

    def set_current_tier(self, tier):
        self.current_tier = tier

    def set_wins(self, amount):
        self.wins = amount
    # endregion

    # region change values
    def next_turn(self):
        self.turn += 1

    def reduce_hearts(self, amount):
        self.hearts -= amount

    def reduce_gold(self, amount):
        self.gold -= amount

    def add_gold(self, amount):
        self.gold += amount

    def advance_tier(self):
        self.current_tier += 1

    def add_win(self):
        self.wins += 1
    # endregion
