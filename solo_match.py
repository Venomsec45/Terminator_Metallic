from player import Player
from enemy import random_enemy

# Solo Match Function
def solo_match(player):
    enemy = random_enemy()
    print(f"\nFight started against {enemy.name}!")

    # Combat Loop
    while player.is_alive() and enemy.is_alive():
        print("\n--- STATUS ---")
        print(f"Your HP: {player.hp}/{player.max_hp}")
        print(f"{enemy.name} HP: {enemy.hp}")

        print("\n1. Attack")
        print("2. Use Item")

        action = input("Choose action: ")

        if action == "1":
            player.attack(enemy)

        elif action == "2":
            player.use_item()

        else:
            print("Invalid choice!")
            continue

        # Enemy defeated check
        if enemy.is_alive():
            break

        # Enemy turn
        enemy.attack(player)

    # Results
    print("\n--- RESULT ---")

    if player.hp <= 0:
        print("You lost the match!")
    else:
        print("You won the match!")
        player.gain_rewards(enemy.xp_reward, enemy.coin_reward)

    # Reset HP
    player.reset_hp()
    print("HP restored.\n")


# Test
if __name__ == "__main__":
    player = Player()
    solo_match(player)