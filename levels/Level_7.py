from combat_system import start_combat
from menu import post_level_menu
from player_levels import check_level_up
import time
import sys
import os

# Text animation
def animate_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def pause(seconds=1):
    time.sleep(seconds)

def level7_dialogue():
    animate_text("Rain pours heavily across the empty highway.")
    animate_text("Police sirens echo in the distance.")
    pause(1)

    animate_text("John Connor: We lost him... right?")
    animate_text("T-800: Negative.")
    animate_text("T-800: The T-1000 does not stop.")
    pause(1)

    animate_text("Sarah Connor reloads her shotgun nervously.")
    animate_text("Sarah Connor: Then why isn't it attacking?")
    animate_text("T-800: It is waiting.")
    animate_text("T-800: Studying us.")
    pause(1)

    animate_text("A large truck suddenly crashes through nearby barricades.")
    pause(1)

    animate_text("John Connor: Oh no...")
    animate_text("Sarah Connor: Everybody MOVE!")
    pause(1)

    animate_text("The T-1000 steps out of the flames unharmed.")
    pause(1)

    animate_text("T-1000: John Connor.")
    animate_text("T-1000: You cannot escape.")
    pause(1)

    animate_text("John Connor: WHY WON'T YOU DIE?!")
    animate_text("The T-1000's face slowly reforms from liquid metal.")
    pause(1)

    animate_text("T-800: Get on the motorcycle.")
    animate_text("Sarah Connor: NOW!")
    pause(1)

    animate_text(">>> OBJECTIVE: ESCAPE THE T-1000 <<<", 0.01)
    # Fight
    pause(1)

    animate_text("The motorcycle speeds into the storm.")
    pause(1)

    animate_text("John Connor: It's gaining on us!")
    animate_text("Sarah Connor fires at the windshield.")
    pause(1)

    animate_text("The truck smashes through abandoned cars.")
    animate_text("Metal explodes everywhere.")
    pause(1)

    animate_text("T-800: Incoming collision.")
    animate_text("Sarah Connor: HOLD ON!")
    pause(2)

def level7():
    level7_dialogue()
