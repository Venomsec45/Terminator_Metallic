from player import Player
from enemy import random_enemy
from color import Colors


# Solo Match Function
def solo_match(player):

    enemy = random_enemy()

    print(f"\nFight started against {Colors.Custom_red}{enemy.name}!{Colors.End}")

    # Combat Loop
    while player.is_alive() and enemy.is_alive():

        print("\n" + "-" * 40 + "STATUS" + "-" * 40)
        print(f"Your HP: {Colors.Custom_green_1}{player.hp}{Colors.End}/{Colors.Custom_green_1}{player.max_hp}{Colors.End}")
        print(f"{enemy.name} HP: {enemy.hp}")

        print(f"\n1. {Colors.Custom_red}Attack{Colors.End}")
        print(f"2. {Colors.Custom_blue}Use Item{Colors.End}")

        action = input("Choose action: ")

        if action == "1":
            player.attack(enemy)

        elif action == "2":
            player.use_item()

        else:
            print(f"{Colors.Custom_red}Invalid choice!{Colors.End}")
            continue

        # Enemy defeated check
        if not enemy.is_alive():
            break

        # Enemy turn
        enemy.attack(player)

    # Results
    print("\n" + "-" * 40 + "RESULT" + "-" * 40)

    if player.hp <= 0:
        print(f"{Colors.Custom_red}You lost the match!{Colors.End}")

    else:
        print(f"{Colors.Custom_green_1}You won the match!{Colors.End}")
        player.gain_rewards(enemy.xp_reward, enemy.coin_reward)

    # Reset HP
    player.reset_hp()

    print("HP restored.\n")


# Test
if __name__ == "__main__":

    player = Player("Player1")

    solo_match(player)