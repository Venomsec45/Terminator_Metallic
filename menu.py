from shop import show_shop
from color import Colors
import time

def post_level_menu(player_hp, coins, xp, inventory, player_stats):

    while True:
        print("\n" + "=" * 40 + "NEXT ACTION" + "=" * 40)
        print(f"[1] {Colors.Custom_blue}Continue{Colors.End}")
        print(f"[2] {Colors.Custom_yellow}Shop{Colors.End}")
        print(f"[3] {Colors.Grey}Exit Campaign{Colors.End}")

        choice = input("> ")

        if choice == "1":
            return player_hp, coins, xp, inventory, player_stats, "continue"

        elif choice == "2":
            coins, xp, inventory, player_stats = show_shop(
                coins, xp, inventory, player_stats
            )

        elif choice == "3":
            print(f"{Colors.Custom_red}Leaving campaign...{Colors.End}")
            time.sleep(2)
            return player_hp, coins, xp, inventory, player_stats, "leave_campaign"

        else:
            print(f"{Colors.Custom_red}Invalid choice!{Colors.End}")