from player import Player
from enemy import random_enemy
from color import Colors
import time
from additional_scripts.screen_clear import terminal_screen_clear

def solo_match(player):

    enemy = random_enemy()

    print(f"\nFight started against {Colors.Custom_red}{enemy.name}!{Colors.End}")

    # Combat Loop
    while player.is_alive() and enemy.is_alive():
        terminal_screen_clear()

        print("\n" + "-" * 40 + "STATUS" + "-" * 40 + "\n")
        print(f"Your HP: {Colors.Custom_green_1}{player.hp}{Colors.End}/{player.max_hp}")
        print(f"{enemy.name} HP: {Colors.Custom_green_1}{enemy.hp}{Colors.End}")
        print("\n" + "-" * 86)

        print(f"\n1. {Colors.Custom_red}Attack{Colors.End}")
        print(f"2. {Colors.Custom_blue}Use Item{Colors.End}")

        action = input("Choose action: ").strip()

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
        time.sleep(2.5)

    # RESULTS
    print("\n" + "-" * 40 + "RESULT" + "-" * 40 + "\n")

    if player.hp <= 0:
        print(f"{Colors.Custom_red}You lost the match!{Colors.End}")
        player.game_over = True

    else:
        print(f"{Colors.Custom_green_1}You won the match!{Colors.End}")
        player.gain_rewards(enemy.xp_reward, enemy.coin_reward)

    print("\n" + "-" * 86)
    time.sleep(2.5)

    return player