from shop import show_shop

def post_level_menu(player_hp, coins, xp, inventory, player_stats):

    while True:
        print("\n=== NEXT ACTION ===")
        print("[1] Continue")
        print("[2] Shop")
        print("[3] Exit")

        choice = input("> ")

        if choice == "1":
            return player_hp, coins, xp, inventory, player_stats, "continue"

        elif choice == "2":

            # ENTER SHOP → RETURNS UPDATED VALUES
            coins, xp, inventory, player_stats = show_shop(
                coins, xp, inventory, player_stats
            )

        elif choice == "3":
            exit()

        else:
            print("Invalid choice.")