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

def level11_dialogue():
    animate_text("Molten steel glows beneath the massive factory.")
    animate_text("Steam fills the air.")
    pause(1)

    animate_text("John Connor: It's over...")
    animate_text("John Connor: We destroyed Cyberdyne.")
    pause(1)

    animate_text("T-800 scans the area silently.")
    animate_text("T-800: Negative.")
    animate_text("T-800: The T-1000 is still active.")
    pause(1)

    animate_text("Heavy metallic footsteps echo through the darkness.")
    pause(1)

    animate_text("Sarah Connor: Everybody RUN!")
    pause(1)

    animate_text("The T-1000 slowly emerges from the shadows.")
    animate_text("Its body constantly mutates from heat damage.")
    animate_text("Metal shifts violently across its form.")
    pause(1)

    animate_text("T-1000: You... all... terminated.")
    pause(1)

    animate_text("John Connor: It's breaking apart!")
    animate_text("T-800: It is unstable.")
    animate_text("T-800: This is our only chance.")
    pause(1)

    animate_text(">>> FINAL BOSS: T-1000 FINAL FORM <<<", 0.01)
    pause(2)

    animate_text("The final battle shakes the entire steel mill.")
    animate_text("Explosions erupt across molten platforms.")
    pause(1)

    animate_text("Sarah Connor fires her final shotgun blast.")
    pause(1)

    animate_text("The T-1000 falls into molten steel.")
    animate_text("Its body melts violently.")
    animate_text("Screams distort into metallic static.")
    pause(2)

    animate_text("Silence fills the steel mill.")
    pause(2)

    animate_text("John Connor: We did it...")
    animate_text("Sarah Connor slowly lowers her weapon.")
    pause(1)

    animate_text("T-800 looks toward the molten steel.")
    animate_text("T-800: There is still one more chip.")
    animate_text("T-800: Inside me.")
    pause(1)

    animate_text("John Connor: No...")
    animate_text("John Connor: You don't have to do this.")
    pause(1)

    animate_text("T-800: My existence would allow Skynet to rebuild.")
    animate_text("T-800: I cannot allow that.")
    pause(1)

    animate_text("Sarah Connor watches silently.")
    animate_text("Her eyes slowly fill with tears.")
    pause(1)

    animate_text("John Connor: I order you not to go!")
    pause(1)

    animate_text("T-800: I know now why humans cry.")
    animate_text("T-800: But it is something I can never do.")
    pause(2)

    animate_text("The T-800 slowly lowers itself into the molten steel.")
    pause(2)

    animate_text("John Connor: Goodbye...")
    animate_text("The T-800 gives a final thumbs up.")
    pause(2)

    animate_text("The machine disappears beneath the molten steel.")
    pause(3)


def level11():
    level11_dialogue()