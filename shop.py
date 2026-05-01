def show_shop(coins, xp_points, inventory, player_stats):
    while True:
        sub_line = "-" * 78
        print(sub_line)

        # Player info
        print(f"Coins: {coins} | XP: {xp_points}")
        print(sub_line)

        print("SHOP".center(78))
        print(sub_line)

        # Shop items (name, cost, effect)
        shop_items = {
            # Weapons
            1: ("AMT Hardballer Longslide", 75, "damage", 15),
            2: ("Uzi 9mm SMG", 125, "damage", 25),
            3: ("Winchester Shotgun", 150, "damage", 35),
            4: ("HK G36 Rifle", 200, "damage", 45),
            5: ("Browning M1919", 250, "damage", 55),
            6: ("M79 Grenade Launcher", 300, "damage", 65),
            7: ("M134 Minigun", 350, "damage", 75),
            8: ("Plasma Rifle", 400, "damage", 85),
            #Upgrades
            9: ("Armor Upgrade", 100, "hp", 20),
            10: ("Damage Boost", 150, "damage", 15),
            11: ("XP Booster", 200, "xp_boost", 2),
        }

        print("\nItems:")
        for key, (name, cost, stat, value) in shop_items.items():
            print(f"{key}. {name:<35} - {cost} coins")

        print("\nInventory:")
        if inventory:
            for i, item in enumerate(inventory, 1):
                print(f"{i}. {item}")
        else:
            print("- Empty")

        print("\nOptions:")
        print("12. Buy Item")
        print("13. Sell Item")
        print("14. Exit Shop")

        print(sub_line)
        choice = input("Enter your choice: ")

        # BUY
        if choice == "12":
            try:
                item_choice = int(input("Enter item number to buy: "))
                if item_choice in shop_items:
                    name, cost, stat, value = shop_items[item_choice]

                    if coins >= cost:
                        coins -= cost
                        inventory.append(name)

                        # Apply upgrade immediately
                        if stat == "damage":
                            player_stats["damage"] += value
                        elif stat == "hp":
                            player_stats["hp"] += value
                        elif stat == "xp_boost":
                            player_stats["xp_boost"] *= value

                        print(f"Bought {name}!")
                    else:
                        print("Not enough coins!")
                else:
                    print("Invalid item.")
            except ValueError:
                print("Invalid input.")

        # Selling
        elif choice == "13":
            if not inventory:
                print("Nothing to sell.")
                continue

            try:
                for i, item in enumerate(inventory, 1):
                    print(f"{i}. {item}")

                sell_choice = int(input("Choose item to sell: ")) - 1

                if 0 <= sell_choice < len(inventory):
                    sold_item = inventory.pop(sell_choice)
                    coins += 50  # fixed sell price
                    print(f"Sold {sold_item} for 50 coins.")
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input.")

        # Exit
        elif choice == "14":
            print("Leaving shop...")
            return coins, xp_points, inventory, player_stats

        else:
            print("Invalid choice.")