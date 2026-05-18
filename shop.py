from color import Colors
from additional_scripts.screen_clear import terminal_screen_clear

def show_shop(player_state):
    while True:
        terminal_screen_clear()
        sub_line = "-" * 78
        print(sub_line)

        # DEFAULTS (SAFE INIT)
        player_state.setdefault("weapon", "Fists")
        player_state.setdefault("base_damage", 10)
        player_state.setdefault("bonus_damage", 0)
        player_state.setdefault("damage", 10)
        player_state.setdefault("hp", 100)
        player_state.setdefault("max_hp", 100)
        player_state.setdefault("xp_boost", 1)
        player_state.setdefault("inventory", [])

        # Recalculate damage
        player_state["damage"] = player_state["base_damage"] + player_state["bonus_damage"]

        print(
            f"Coins: {Colors.Custom_yellow}{player_state.get('coins', 0)}{Colors.End} | "
            f"XP: {Colors.Custom_yellow}{player_state.get('xp', 0)}{Colors.End} | "
            f"HP: {Colors.Custom_yellow}{player_state['hp']}/{player_state['max_hp']}{Colors.End} | "
            f"Weapon: {Colors.Custom_yellow}{player_state['weapon']}{Colors.End}"
        )

        print(sub_line)
        print(f"{Colors.Custom_blue}SHOP{Colors.End}".center(78))
        print(sub_line)

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
            print(f"{key}. {name:<35} - {Colors.Custom_yellow}{cost}{Colors.End} coins")

        print("\nInventory:")
        if not player_state["inventory"]:
            print("- Empty")
        else:
            for i, item in enumerate(player_state["inventory"], 1):
                print(f"{i}. {item}")

        print("\nOptions:")
        print("13. Buy Item")
        print("14. Sell Item")
        print("15. Exit Shop")

        print(sub_line)
        choice = input("Enter your choice: ")

        # ---------------- BUY ----------------
        if choice == "13":
            try:
                item_choice = int(input("Enter item number to buy: "))

                if item_choice not in shop_items:
                    print("Invalid item.")
                    continue

                name, cost, stat, value = shop_items[item_choice]

                if player_state["coins"] < cost:
                    print("Not enough coins.")
                    continue

                player_state["coins"] -= cost

                if stat != "heal":
                    player_state["inventory"].append(name)

                if stat == "weapon":
                    player_state["weapon"] = name
                    player_state["base_damage"] = value
                    print(f"Equipped {name}")

                elif stat == "hp":
                    player_state["max_hp"] += value
                    player_state["hp"] = player_state["max_hp"]
                    print("Max HP increased!")

                elif stat == "damage":
                    player_state["bonus_damage"] += value
                    print("Damage increased!")

                elif stat == "xp_boost":
                    player_state["xp_boost"] *= value
                    print("XP boost upgraded!")

                elif stat == "heal":
                    old_hp = player_state["hp"]
                    player_state["hp"] = min(
                        player_state["hp"] + value,
                        player_state["max_hp"]
                    )
                    healed = player_state["hp"] - old_hp
                    print(f"Healed {healed} HP!")

            except ValueError:
                print("Invalid input.")

        # ---------------- SELL ----------------
        elif choice == "14":
            if not player_state["inventory"]:
                print("Nothing to sell.")
                continue

            for i, item in enumerate(player_state["inventory"], 1):
                print(f"{i}. {item}")

            try:
                sell_choice = int(input("Choose item to sell: ")) - 1

                if 0 <= sell_choice < len(player_state["inventory"]):
                    sold_item = player_state["inventory"].pop(sell_choice)
                    player_state["coins"] += 25
                    print(f"Sold {sold_item} for 25 coins.")
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input.")

        # ---------------- EXIT ----------------
        elif choice == "15":
            print("Leaving shop...")
            return player_state