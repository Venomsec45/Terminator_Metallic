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

def level9_dialogue():
    animate_text("Night falls over Miles Dyson's home.")
    pause(1)

    animate_text("Miles Dyson works quietly at his computer.")
    animate_text("Complex Cyberdyne files glow across the screen.")
    pause(1)

    animate_text("Miles Dyson: Artificial intelligence...")
    animate_text("Miles Dyson: This could change the entire world.")
    pause(1)

    animate_text("Suddenly glass shatters downstairs.")
    pause(1)

    animate_text("Miles Dyson: What the hell?")
    pause(1)

    animate_text("Sarah Connor enters holding a rifle.")
    animate_text("Her hands shake with rage.")
    pause(1)

    animate_text("Sarah Connor: Your work kills billions.")
    animate_text("Sarah Connor: Men, women, children.")
    animate_text("Sarah Connor: Entire cities burned to ashes.")
    pause(1)

    animate_text("Miles Dyson: I don't understand.")
    animate_text("Miles Dyson: Who are you people?")
    pause(1)

    animate_text("John Connor slowly steps forward.")
    animate_text("John Connor: You're going to create Skynet.")
    animate_text("John Connor: A machine system that destroys humanity.")
    pause(1)

    animate_text("Miles Dyson laughs nervously.")
    animate_text("Miles Dyson: That's impossible.")
    pause(1)

    animate_text("T-800: Skynet becomes self-aware.")
    animate_text("T-800: Human decisions are removed from strategic defense.")
    animate_text("T-800: Nuclear war begins shortly after.")
    pause(1)

    animate_text("Miles Dyson's face slowly turns pale.")
    pause(1)

    animate_text("Miles Dyson: Dear God...")
    animate_text("Miles Dyson: What have I done?")
    pause(1)

    animate_text("Sarah Connor lowers her weapon slowly.")
    animate_text("Sarah Connor: Help us stop it.")
    pause(1)

    animate_text(">>> OBJECTIVE: DESTROY SKYNET RESEARCH <<<", 0.01)
    pause(2)


def level9():
    level9_dialogue()
