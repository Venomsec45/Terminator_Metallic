import json
from additional_scripts.screen_clear import terminal_screen_clear

SETTINGS_FILE = "settings.json"

# Default settings
settings = {
    "username": None,
    "theme": "Default",
    "save_text_results": True,
    "save_player_status": True
}

# ---------------- SAVE ----------------
def save_settings():
    with open(SETTINGS_FILE, "w") as file:
        json.dump(settings, file, indent=4)

# ---------------- LOAD ----------------
def load_settings():
    global settings
    try:
        with open(SETTINGS_FILE, "r") as file:
            settings.update(json.load(file))
    except FileNotFoundError:
        save_settings()

# ---------------- MENU ----------------
def settings_menu():
    while True:
        terminal_screen_clear()
        print("\n" + "-" * 40 + "SETTINGS" + "-" * 40 + "\n")

        print(f"Current Username: {settings['username']}")
        print(f"Theme: {settings['theme']}")
        print(f"Save Text Results: {settings['save_text_results']}")
        print(f"Save Player Status: {settings['save_player_status']}")

        print("\n1. Change Username")
        print("2. Toggle Text Save Results")
        print("3. Toggle Player Save Status")
        print("4. Back")

        choice = input("> ").strip()

        # ---------------- USERNAME ----------------
        if choice == "1":
            username = input("Enter username (min 5 chars): ").strip()

            if len(username) >= 5:
                settings["username"] = username
                print("Username updated!")
            else:
                print("Invalid username!")
            input("Press Enter...")

        # THEME IS DEPRECATED 

        # ---------------- TOGGLE TEXT SAVE ----------------
        elif choice == "2":
            settings["save_text_results"] = not settings["save_text_results"]
            print(f"Text Save Results: {settings['save_text_results']}")
            input("Press Enter...")

        # ---------------- TOGGLE PLAYER SAVE ----------------
        elif choice == "3":
            settings["save_player_status"] = not settings["save_player_status"]
            print(f"Player Save Status: {settings['save_player_status']}")
            input("Press Enter...")

        # ---------------- EXIT ----------------
        elif choice == "4":
            save_settings()
            break

        else:
            print("Invalid choice!")
            input("Press Enter...")

# auto load on import
load_settings()