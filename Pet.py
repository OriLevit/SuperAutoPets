class Pet:
    def __init__(self, name, tier, attack, health, t1_power, t2_power, t3_power, power_keyword):
        self.name = name
        self.tier = tier
        self.attack = attack
        self.health = health
        self.t1_power = t1_power
        self.t2_power = t2_power
        self.t3_power = t3_power
        self.power_keyword = power_keyword
        self.fruit_on_pet = ""

    # region GET Methods
    def get_name(self):
        return self.name

    def get_tier(self):
        return self.tier

    def get_attack(self):
        return self.attack

    def get_health(self):
        return self.health

    def get_t1_power(self):
        return self.t1_power

    def get_t2_power(self):
        return self.t2_power

    def get_t3_power(self):
        return self.t3_power

    def get_keyword(self):
        return self.power_keyword

    def get_fruit_on_pet(self):
        return self.fruit_on_pet

    # endregion

    # region SET Methods
    def set_name(self, name):
        self.name = name

    def set_tier(self, tier):
        self.tier = tier

    def set_attack(self, attack):
        self.attack = attack

    def set_health(self, health):
        self.health = health

    def set_t1_power(self, t1_power):
        self.t1_power = t1_power

    def set_t2_power(self, t2_power):
        self.t2_power = t2_power

    def set_t3_power(self, t3_power):
        self.t3_power = t3_power

    def set_keyword(self, keyword):
        self.power_keyword = keyword

    def set_fruit_on_pet(self, fruit):
        self.fruit_on_pet = fruit
    # endregion


