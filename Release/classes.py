class Character:
    def __init__(self, name, hp, attack, defense, unlocked, price):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.unlocked = unlocked
        self.price = price

    def is_alive(self):
        return self.hp > 0


class Enemy:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.hp > 0

class User:
    def __init__(self, name, coins, registered):
        self.name = name
        self.coins = coins
        self.registered = registered

class VisualCoins:
    def __init__(self, coins):
        self.coins = coins
        visual_coins = coins
    def __str__(self):
        visual_coins = str(self.coins)
        if self.coins > 1000000:
            visual_coins = self.coins / 1000000
            visual_coins = f"{visual_coins}млн."
        elif self.coins > 1000:
            visual_coins = self.coins / 1000
            visual_coins = f"{visual_coins}тыс."
        return visual_coins