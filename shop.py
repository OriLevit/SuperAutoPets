import random


class Shop:
    def __init__(self, amount_of_pets_in_shop: int, shop_max_tier: int, pets_in_shop: list):
        self.amount_of_pets_in_shop = amount_of_pets_in_shop
        self.shop_max_tier = shop_max_tier
        self.pets_in_shop = pets_in_shop

    # region GET methods
    def get_amount_of_pets_in_shop(self):
        return self.amount_of_pets_in_shop

    def get_pets_in_shop(self):
        return self.pets_in_shop

    def get_shop_max_tier(self):
        return self.get_shop_max_tier()

    # endregion

    # region SET methods
    def set_amount_of_pets_in_shop(self, amount: int):
        self.amount_of_pets_in_shop = amount

    def set_pets_in_shop(self, pets: list):
        self.pets_in_shop = pets

    def set_shop_max_tier(self, tier: int):
        self.shop_max_tier = tier
    # endregion

    def generate_pets(self, available_pets: list):
        self.pets_in_shop = []
        for pet in range(self.amount_of_pets_in_shop):
            self.pets_in_shop.append(random.choice(available_pets))