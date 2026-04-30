def show_shop(coins, xp_points, inventory):
    # Lines
    sub_line = "-" * 78

    print(sub_line)

    # Player information
    print(f"Coins: {coins} | XP: {xp_points}")
    print(sub_line)

    # Shop Title
    print("SHOP".center(78))
    print(sub_line)

    # Weapons Section
    print("\nWeapons:")
    print(f"{'1. AMT Hardballer Longslide (.45 ACP)':<40} - {'75 coins':<20} = (+15 damage)")
    print(f"{'2. Uzi 9mm Submachine Gun':<40} - {'125 coins':<20} = (+25 damage)")
    print(f"{'3. Winchester Model 1887 Shotgun':<40} - {'150 coins':<20} = (+35 damage)")
    print(f"{'4. HK G36 Rifle':<40} - {'200 coins':<20} = (+45 damage)")
    print(f"{'5. Browning M1919 Machine Gun':<40} - {'250 coins':<20} = (+55 damage)")
    print(f"{'6. M79 Grenade Launcher':<40} - {'300 coins':<20} = (+65 damage)")
    print(f"{'7. M134 Minigun':<40} - {'350 coins':<20} = (+75 damage)")
    print(f"{'8. Plasma Rifle':<40} - {'400 coins':<20} = (+85 damage)")
    print("\n")
    print(sub_line)

    # Upgrades
    print("\nUpgrades:")
    print(f"{'9. Armor Upgrade':<40} - {'100 coins':<20} = (+20 HP)")
    print(f"{'10. Damage Boost':<40} - {'150 coins':<20} = (+15 damage)")
    print(f"{'11. XP Booster':<40} - {'200 coins':<20} = (+2x XP)")
    print("\n")
    print(sub_line)

    # Inventory
    print("\nInventory:")
    if inventory:
        for item in inventory:
            print(f"- {item}")
    else:
        print("- Empty")
    print("\n")
    print(sub_line)

    #Menu Options
    print("\n")
    print("12. Buy Item")
    print("13. Sell Item")
    print("14. Back to Main Menu")
    print("\n")

    print(sub_line)

    choice = input("Enter your choice: ")
    return choice

print(show_shop(20, 30, ["AK47", "Rocket launcher"]))



