from abc import ABC, abstractmethod
import random

class Enemy(ABC):
    def __init__(self, name, hp, damage, xp_reward, coin_reward):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.xp_reward = xp_reward
        self.coin_reward = coin_reward

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0

    def attack(self):
        return self.damage

    @abstractmethod
    def special_ability(self):
        pass


# Boss enemies
class T800(Enemy):
    def __init__(self):
        super().__init__("T-800", hp=100, damage=15, xp_reward=50, coin_reward=30)

    def special_ability(self):
        # Heavy punch: chance to deal extra damage
        if random.random() < 0.3:
            bonus = 10
            print("T-800 uses Heavy Punch!")
            return self.damage + bonus
        return self.damage
    
class T1000(Enemy):
    def __init__(self):
        super().__init__("T-1000", hp=120, damage=18, xp_reward=80, coin_reward=50)

    def special_ability(self):
        # Regeneration ability
        heal = random.randint(5, 15)
        self.hp += heal
        print(f"T-1000 regenerates {heal} HP!")
        return self.damage
    
class TX(Enemy):
    def __init__(self):
        super().__init__("T-X", hp=180, damage=25, xp_reward=120, coin_reward=100)

    def special_ability(self):
        # Plasma blast: high burst damage
        if random.random() < 0.4:
            print("T-X uses Plasma Blast!")
            return self.damage + 20
        return self.damage
    

# Level 1-5 regular enemies
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
    
# Level 6-10 tougher enemies
class T600(Enemy):
    def __init__(self):
        super().__init__("T-600", 110, 16, 45, 35)

    def special_ability(self):
        if random.random() < 0.25:
            print("T-600 uses Minigun Burst!")
            return self.damage + 10
        return self.damage


class T700(Enemy):
    def __init__(self):
        super().__init__("T-700", 130, 18, 55, 40)

    def special_ability(self):
        if random.random() < 0.3:
            print("T-700 uses Tactical Strike!")
            return self.damage + 12
        return self.damage

# level 11-15 advanced enemies
class HKTank(Enemy):
    def __init__(self):
        super().__init__("HK Tank", 160, 22, 70, 60)

    def special_ability(self):
        print("HK Tank fires cannon!")
        return self.damage + random.randint(5, 15)


class HKDrone(Enemy):
    def __init__(self):
        super().__init__("HK Aerial Drone", 140, 20, 65, 55)

    def special_ability(self):
        if random.random() < 0.3:
            print("Drone launches missiles!")
            return self.damage + 15
        return self.damage
    

def get_enemy_by_level(level):
    if level <= 2:
        return ScoutDrone()
    elif level <= 4:
        return ResistanceSoldier()
    elif level == 5:
        return T600()
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
