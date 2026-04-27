from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage

    @abstractmethod
    def attack(self, target):
        pass

    @abstractmethod
    def take_damage(self, amount):
        pass


class Player(Character):
    def __init__(self, hp, damage):
        super().__init__(hp, damage)
        self.xp = 0
        self.coins = 0
        self.inventory = []

    def attack(self, target):
        print("Player attacks!")
        target.take_damage(self.damage)

    def take_damage(self, amount):
        self.hp -= amount
        print(f"Player takes {amount} damage. HP left: {self.hp}")

    def gain_rewards(self, xp, coins):
        self.xp += xp
        self.coins += coins
        print(f"Gained {xp} XP and {coins} coins!")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item} added to inventory.")