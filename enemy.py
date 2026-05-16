from abc import ABC, abstractmethod
import random

# Base Enemy class
class Enemy(ABC):
    def __init__(self, name, hp, damage, xp_reward, coin_reward):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.damage = damage
        self.xp_reward = xp_reward
        self.coin_reward = coin_reward

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} takes {amount} damage! HP: {self.hp}/{self.max_hp}")

    def is_alive(self):
        return self.hp > 0

    # Main attack logic
    def attack(self, target):
        if random.random() < 0.3:
            dmg = self.special_ability()
        else:
            dmg = random.randint(self.damage - 2, self.damage + 2)

        print(f"{self.name} attacks for {dmg} damage!")
        target.take_damage(dmg)

    @abstractmethod
    def special_ability(self):
        pass


# Boss Enemies
class T800(Enemy):
    def __init__(self):
        super().__init__("T-800", 100, 15, 50, 30)

    def special_ability(self):
        print("T-800 uses Heavy Punch!")
        return self.damage + 10


class T1000(Enemy):
    def __init__(self):
        super().__init__("T-1000", 120, 18, 80, 50)

    def special_ability(self):
        heal = random.randint(10, 25)
        self.hp += heal
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"T-1000 regenerates {heal} HP! ({self.hp}/{self.max_hp})")
        return self.damage


class TX(Enemy):
    def __init__(self):
        super().__init__("T-X", 180, 25, 120, 100)

    def special_ability(self):
        print("T-X uses Plasma Blast!")
        return self.damage + 20


# Early Game Enemies
class ScoutDrone(Enemy):
    def __init__(self):
        super().__init__("Scout Drone", 60, 10, 20, 15)

    def special_ability(self):
        return self.damage


class ResistanceSoldier(Enemy):
    def __init__(self):
        super().__init__("Captured Soldier", 80, 12, 25, 20)

    def special_ability(self):
        return self.damage


# Mid Game Enemies
class T600(Enemy):
    def __init__(self):
        super().__init__("T-600", 110, 16, 45, 35)

    def special_ability(self):
        print("T-600 uses Minigun Burst!")
        return self.damage + 10


class T700(Enemy):
    def __init__(self):
        super().__init__("T-700", 130, 18, 55, 40)

    def special_ability(self):
        print("T-700 uses Tactical Strike!")
        return self.damage + 12


# Late Game Enemies
class HKTank(Enemy):
    def __init__(self):
        super().__init__("HK Tank", 160, 22, 70, 60)

    def special_ability(self):
        bonus = random.randint(5, 15)
        print("HK Tank fires cannon!")
        return self.damage + bonus


class HKDrone(Enemy):
    def __init__(self):
        super().__init__("HK Aerial Drone", 140, 20, 65, 55)

    def special_ability(self):
        print("Drone launches missiles!")
        return self.damage + 15


# Level based enemies
def get_enemy_by_level(level):
    if level <= 2:
        return ScoutDrone()
    elif level <= 4:
        return ResistanceSoldier()
    elif level <= 7:
        return T600()
    elif level <= 9:
        return T700()
    elif level == 10:
        return T800()
    elif level <= 12:
        return HKDrone()
    elif level <= 14:
        return HKTank()
    elif level == 15:
        return TX()

# Random Enemy (Solo matches)
def random_enemy():
    enemies = [
        ScoutDrone(),
        ResistanceSoldier(),
        T600(),
        T700(),
        T800(),
        T1000(),
        HKDrone(),
        HKTank(),
        TX()
    ]
    return random.choice(enemies)