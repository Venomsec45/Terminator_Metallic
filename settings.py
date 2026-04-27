import json

# Default settings
settings = {
    "username": None,
    "theme": None,
    "save_text_results": True,
    "save_player_status": True
}

# Save settings
def save_settings():
    with open("settings.json", "w") as file:
        json.dump(settings, file, indent=4)

# Load settings
def load_settings():
    global settings
    try:
        with open("settings.json", "r") as file:
            settings = json.load(file)
    except FileNotFoundError:
        save_settings()

# Settings menu
def settings_menu():
    while True:
        print("\n--- SETTINGS ---")
        print("1. Username change")
        print("2. Theme change")
        print("3. Text save results (True/False)")
        print("4. Save player status in JSON (True/False)")
        print("5. Back")

        choice = input("Choose: ")

        if choice == "1":
            username = input("Enter username (min 5 chars): ")
            if username != "" and len(username) >= 5:
                settings["username"] = username
                print("Username updated!")
            else:
                print("Invalid username!")

        elif choice == "2":
            print("""1. Red
2. Blue
3. Green""")
            theme = input("Choose theme: ")
            if theme == "1":
                settings["theme"] = "Red"
            elif theme == "2":
                settings["theme"] = "Blue"
            elif theme == "3":
                settings["theme"] = "Green"
            else:
                print("Invalid!")

        elif choice == "3":
            settings["save_text_results"] = True
            print("Text Saved")

        elif choice == "4":
            settings["save_player_status"] = True
            print("Player status saved")

        elif choice == "5":
            save_settings()
            break

        else:
            print("Invalid choice!")

# auto load pag run
load_settings()