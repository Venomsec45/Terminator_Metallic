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

def level8_dialogue():
    animate_text("Cold fluorescent lights flicker inside Pescadero Hospital.")
    pause(1)

    animate_text("Sarah Connor sits alone inside her room.")
    animate_text("Her hands tremble slightly.")
    pause(1)

    animate_text("Sarah Connor: They're coming...")
    animate_text("Sarah Connor: I knew this day would come.")
    pause(1)

    animate_text("A nurse slowly approaches the hallway.")
    animate_text("Then suddenly screams echo downstairs.")
    pause(1)

    animate_text("Security Guard: LOCK THE DOORS!")
    animate_text("Security Guard: SOMETHING'S INSIDE THE BUILDING!")
    pause(1)

    animate_text("Sarah Connor slowly looks up.")
    animate_text("A familiar metallic footstep echoes.")
    pause(1)

    animate_text("Sarah Connor: No...")
    animate_text("Sarah Connor: Not again...")
    pause(1)

    animate_text("The T-1000 walks through the hallway disguised as a police officer.")
    animate_text("Its silver blade forms from its arm.")
    pause(1)

    animate_text("T-1000: Sarah Connor.")
    animate_text("T-1000: Come with me.")
    pause(1)

    animate_text("Suddenly shotgun blasts erupt nearby.")
    pause(1)

    animate_text("T-800: Sarah Connor.")
    animate_text("T-800: Come with me if you want to live.")
    pause(1)

    animate_text("Sarah Connor stares in shock.")
    animate_text("Sarah Connor: You...")
    animate_text("Sarah Connor: You're one of THEM!")
    pause(1)

    animate_text("John Connor: Mom wait!")
    animate_text("John Connor: He's here to help us!")
    pause(1)

    animate_text("The hallway erupts into chaos.")
    animate_text("Patients scream while alarms blare.")
    pause(1)

    animate_text(">>> BOSS ENCOUNTER: T-1000 <<<", 0.01)
    pause(2)

def level8():
    level8_dialogue()

