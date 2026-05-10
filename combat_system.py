import random
import sys
import time


# Text animation
def animate_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# Player attack (NOW USES WEAPON DAMAGE)
def player_attack(player_damage):
    base = random.randint(1, 5)
    return base + player_damage


# Enemy attack
def enemy_attack(min_dmg, max_dmg):
    return random.randint(min_dmg, max_dmg)


# Boss special attack
def boss_special():
    if random.random() < 0.3:
        return random.randint(18, 25), True
    return random.randint(10, 15), False


# CORE COMBAT SYSTEM (FIXED)
def start_combat(player_hp, enemy_name, enemy_hp, enemy_min, enemy_max,
                 is_boss=False, player_damage=10):

    animate_text(f"\nA {enemy_name} appears!")

    while player_hp > 0 and enemy_hp > 0:

        input("Press ENTER to attack...")

        # PLAYER TURN (NOW USES DAMAGE FROM SHOP/WEAPON)
        damage = player_attack(player_damage)
        enemy_hp -= damage
        animate_text(f"You dealt {damage} damage!")

        if enemy_hp <= 0:
            animate_text(f"{enemy_name} destroyed!")
            return True, player_hp

        time.sleep(0.5)

        # ENEMY TURN
        if is_boss:
            damage, special = boss_special()
            player_hp -= damage

            if special:
                animate_text(f"{enemy_name} used SPECIAL ATTACK! ({damage} dmg)")
            else:
                animate_text(f"{enemy_name} attacks for {damage} damage")

        else:
            damage = enemy_attack(enemy_min, enemy_max)
            player_hp -= damage
            animate_text(f"{enemy_name} attacks for {damage} damage")

        animate_text(f"Your HP: {player_hp}")
        time.sleep(0.5)

    return False, player_hp