import time
import sys
from additional_scripts.screen_clear import terminal_screen_clear
from additional_scripts.line_animation import lines
from color import Colors
from developer_logo import logo, logo_2, logo_3
from loading_animation import power_animation, status_animation, skynet_activate
from lobby import lobby_layout

# Function to handle username input and validation
def get_username():
    while True:
        # Ask user to input a username
        username = input(f"{Colors.Custom_cyan}Enter username: {Colors.End}").strip()

        # Check if username is empty
        if username == "":
            print(f"{Colors.Custom_red}Username cannot be blank.{Colors.End}")

        # Check if username is too short
        elif len(username) < 5:
            print(f"{Colors.Custom_red}Username must be at least 5 characters long.{Colors.End}")

        # If valid, return the username
        else:
            return username

# Function to run logo and loading animations
def run_intro():
    # Loop contains functions from "developer_logo" module
    for logo_function_call in [logo, logo_2]:
        terminal_screen_clear()    
        logo_function_call()       
        time.sleep(2)        

    # Loop contains functions from "loading_animation" module
    for loading_function_call in [
        terminal_screen_clear,
        power_animation,
        status_animation,
        skynet_activate,
        terminal_screen_clear,
        logo_3
    ]:
        loading_function_call()    


# Main function that controls program flow
def main():
    try:
        # Run intro animations
        run_intro()

        # Clear screen before user input
        terminal_screen_clear()

        # User is required to enter a username
        username = get_username()

        # Clear screen before entering lobby
        terminal_screen_clear()

        # Call lobby module and pass username
        lobby_layout(username)

    # Handle Ctrl + C (force stop)
    except KeyboardInterrupt:
        print(f"\n{Colors.Custom_red}GAME STOPPED!{Colors.End}")
        sys.exit(2)


# Ensures main() only runs when this file is executed directly
if __name__ == "__main__":
    main()