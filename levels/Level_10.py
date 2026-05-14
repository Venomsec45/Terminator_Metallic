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

def level10_dialogue():
    animate_text("Cyberdyne Systems burns under emergency alarms.")
    pause(1)

    animate_text("SWAT teams surround the entire building.")
    animate_text("Helicopters circle overhead.")
    pause(1)

    animate_text("John Connor: This place is a warzone...")
    animate_text("Sarah Connor: Stay close.")
    pause(1)

    animate_text("Miles Dyson collapses against the wall.")
    animate_text("He is badly wounded.")
    pause(1)

    animate_text("Miles Dyson: You have to finish this...")
    animate_text("Miles Dyson: No matter what happens to me.")
    pause(1)

    animate_text("T-800 scans incoming police units.")
    animate_text("T-800: Multiple hostiles detected.")
    pause(1)

    animate_text("SWAT Commander: FREEZE!")
    animate_text("SWAT Commander: DROP YOUR WEAPONS!")
    pause(1)

    animate_text("Gunfire suddenly erupts everywhere.")
    pause(1)

    animate_text("Sarah Connor: MOVE MOVE MOVE!")
    animate_text("John Connor: They're everywhere!")
    pause(1)

    animate_text("The T-1000 emerges from the flames.")
    animate_text("Its body glitches from damage.")
    pause(1)

    animate_text("T-1000: Target acquired.")
    animate_text("T-1000: John Connor.")
    pause(1)

    animate_text("T-800 reloads his weapon.")
    animate_text("T-800: I will hold it off.")
    pause(1)

    animate_text(">>> FINAL ASSAULT BEGINS <<<", 0.01)
    pause(2)


def level10():
    level10_dialogue()
