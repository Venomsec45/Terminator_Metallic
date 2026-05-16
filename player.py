from abc import ABC, abstractmethod
import random


# Base Class
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

    def is_alive(self):
        return self.hp > 0

# Player class
class Player(Character):

    def __init__(self, username, hp=100, damage=15):
        super().__init__(hp, damage)

        self.username = username
        self.max_hp = hp
        self.xp = 0
        self.coins = 50
        self.inventory = []
        self.max_inventory = 4


    # Combat system
    def attack(self, target):
        dmg = random.randint(self.damage - 3, self.damage + 3)
        print(f"\nYou attack for {dmg} damage!")
        target.take_damage(dmg)


    def take_damage(self, amount):
        self.hp -= amount

        if self.hp < 0:
            self.hp = 0

        print(f"You took {amount} damage! HP: {self.hp}/{self.max_hp}")


    def heal(self, amount):
        self.hp += amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp

        print(f"Healed {amount} HP! HP: {self.hp}/{self.max_hp}")


    # Items
    def add_item(self, item):

        if len(self.inventory) >= self.max_inventory:
            print("Inventory is full!")
            return False

        self.inventory.append(item)

        print(f"{item} added to inventory.")
        return True


    def use_item(self):

        if not self.inventory:
            print("No items available!")
            return

        print("\nInventory:")

        for i, item in enumerate(self.inventory, 1):
            print(f"{i}. {item}")

        choice = input("Choose item number: ")

        if not choice.isdigit():
            print("Invalid input!")
            return

        index = int(choice) - 1

        if index < 0 or index >= len(self.inventory):
            print("Invalid choice!")
            return

        item = self.inventory.pop(index)

        # Item effects
        if item == "Medkit":
            self.heal(40)

        elif item == "Shield":
            print("Shield activated! Reduced next damage.")

        else:
            print("Unknown item.")


    # Progression system
    def gain_rewards(self, xp, coins):
        self.xp += xp
        self.coins += coins

        print(f"\nGained {xp} XP and {coins} coins!")
        print(f"XP: {self.xp} | Coins: {self.coins}")


    # Utility
    def reset_hp(self):
        self.hp = self.max_hp
        print("HP fully restored!")


    def show_status(self):
        print("\n--- PLAYER STATUS ---")
        print(f"Username: {self.username}")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"XP: {self.xp}")
        print(f"Coins: {self.coins}")
        print(f"Inventory: {self.inventory if self.inventory else 'Empty'}")