from color import Colors
from additional_scripts.screen_clear import terminal_screen_clear

def show_shop(coins, xp_points, inventory, player_stats):
    while True:
        terminal_screen_clear()
        sub_line = "-" * 78
        print(sub_line)

        # SAFE DEFAULTS
        player_stats.setdefault("weapon", "Fists")
        player_stats.setdefault("base_damage", 10)
        player_stats.setdefault("bonus_damage", 0)
        player_stats.setdefault("damage", 10)
        player_stats.setdefault("hp", 100)
        player_stats.setdefault("max_hp", 100)
        player_stats.setdefault("xp_boost", 1)

        # Recalculate damage safety
        player_stats["damage"] = player_stats["base_damage"] + player_stats["bonus_damage"]

        # Player info
        print(f"Coins: {Colors.Custom_yellow}{coins}{Colors.End} | XP: {Colors.Custom_yellow}{xp_points}{Colors.End} | Weapon: {Colors.Custom_yellow}{player_stats['weapon']}{Colors.End}")
        print(sub_line)

        print("SHOP".center(78))
        print(sub_line)

        # SHOP ITEMS
        shop_items = {
            1: ("AMT Hardballer Longslide", 25, "weapon", 15),
            2: ("Uzi 9mm SMG", 75, "weapon", 25),
            3: ("Winchester Shotgun", 100, "weapon", 35),
            4: ("HK G36 Rifle", 150, "weapon", 45),
            5: ("Browning M1919", 200, "weapon", 55),
            6: ("M79 Grenade Launcher", 250, "weapon", 65),
            7: ("M134 Minigun", 300, "weapon", 75),
            8: ("Plasma Rifle", 350, "weapon", 85),

            9: ("Armor Upgrade (+20 Max HP)", 100, "hp", 20),
            10: ("Damage Boost (+15 Damage)", 150, "damage", 15),
            11: ("XP Booster (x2 XP)", 200, "xp_boost", 2),

            12: ("Medkit (+40 HP)", 60, "heal", 40),
        }

        print("\nItems:")
        for key, (name, cost, stat, value) in shop_items.items():
            print(f"{key}. {name:<35} - {cost} coins")

        print("\nInventory:")
        if not inventory:
            print("- Empty")
        else:
            for i, item in enumerate(inventory, 1):
                print(f"{i}. {item}")

        print("\nOptions:")
        print("12. Buy Item")
        print("13. Sell Item")
        print("14. Exit Shop")

        print(sub_line)
        choice = input("Enter your choice: ")

        # ---------------- BUY ----------------
        if choice == "12":
            try:
                item_choice = int(input("Enter item number to buy: "))

                if item_choice not in shop_items:
                    print("Invalid item.")
                    continue

                name, cost, stat, value = shop_items[item_choice]

                if coins < cost:
                    print("Not enough coins.")
                    continue

                coins -= cost
                inventory.append(name)

                # WEAPON SYSTEM (AUTO-EQUIP)
                if stat == "weapon":
                    player_stats["weapon"] = name
                    player_stats["base_damage"] = value
                    player_stats["damage"] = player_stats["base_damage"] + player_stats["bonus_damage"]
                    print(f"Equipped {name} (+{value} base damage)")

                # MAX HP UPGRADE
                elif stat == "hp":
                    player_stats["max_hp"] += value
                    player_stats["hp"] = player_stats["max_hp"]
                    print(f"Max HP increased by {value}")

                # DAMAGE BOOST
                elif stat == "damage":
                    player_stats["bonus_damage"] += value
                    player_stats["damage"] = player_stats["base_damage"] + player_stats["bonus_damage"]
                    print(f"Damage increased by {value}")

                # XP BOOST
                elif stat == "xp_boost":
                    player_stats["xp_boost"] *= value
                    print("XP boost upgraded")

                # HEAL ITEM
                elif stat == "heal":
                    player_stats["hp"] = min(
                        player_stats["hp"] + value,
                        player_stats["max_hp"]
                    )
                    print(f"Restored {value} HP")

                else:
                    print(f"Purchased {name}")

            except ValueError:
                print("Invalid input.")

        # ---------------- SELL ----------------
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
                    coins += 50
                    print(f"Sold {sold_item} for 50 coins.")
                else:
                    print("Invalid choice.")

            except ValueError:
                print("Invalid input.")

        # ---------------- EXIT ----------------
        elif choice == "14":
            print("Leaving shop...")
            return coins, xp_points, inventory, player_stats

        else:
            print("Invalid choice.")