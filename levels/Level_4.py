from unittest import result

from combat_system import start_combat
from menu import post_level_menu
from player_levels import check_level_up
import time
import sys
import os


# Text Animation
def animate_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def pause(seconds=1):
    time.sleep(seconds)


# Simple Sound effects
def play_sfx(name):
    if os.name == "nt":
        import winsound

        sounds = {
            "alert": 1000,
            "explosion": 600,
            "hit": 800,
            "warning": 1200,
            "boss": 400
        }

        if name in sounds:
            winsound.Beep(sounds[name], 200)

    else:
        pass


# Level 4 Dialogue
def level4_dialogue():

    animate_text("The streets grow quieter as the rain slowly stops.")
    pause(1)

    animate_text("Sarah Connor: This place feels empty.")
    animate_text("Kyle Reese: That's what worries me.")
    pause(1)

    animate_text("Broken streetlights flicker above them.")
    animate_text("A cold wind moves through the abandoned buildings.")
    pause(1)

    animate_text("Sarah Connor: We've been running all night.")
    animate_text("Sarah Connor: How do you keep doing this?")
    pause(1)

    animate_text("Kyle Reese: In the future, you don't get tired.")
    animate_text("Kyle Reese: You either keep moving or you die.")
    pause(1)

    animate_text("Suddenly, footsteps echo nearby.")
    play_sfx("warning")
    pause(1)

    animate_text("Sarah Connor: Did you hear that?")
    animate_text("Kyle Reese quickly turns around.")
    animate_text("Kyle Reese: Quiet.")
    pause(1)

    animate_text("The footsteps sound calm.")
    animate_text("Almost human.")
    pause(1)

    animate_text("Unknown Voice: Sarah Connor?")
    pause(1)

    animate_text("Sarah Connor: Who's there?")
    animate_text("Kyle Reese: Don't answer it.")
    pause(1)

    animate_text("A man slowly steps out of the darkness.")
    animate_text("He looks completely normal.")
    pause(1)

    animate_text("Unknown Man: I've been looking for you.")
    animate_text("Unknown Man: You need to come with me.")
    pause(1)

    animate_text("Sarah Connor: Maybe he's trying to help.")
    animate_text("Kyle Reese slowly raises his weapon.")
    animate_text("Kyle Reese: No human moves like that.")
    pause(1)

    animate_text("The man's eyes suddenly glow red.")
    play_sfx("alert")
    pause(1)

    animate_text("Sarah Connor: Oh my God...")
    animate_text("Kyle Reese: Infiltrator unit.")
    pause(1)

    animate_text("Parts of the man's skin tear away, revealing metal underneath.")
    play_sfx("warning")
    pause(1)

    animate_text("Infiltrator: Sarah Connor identified.")
    animate_text("Infiltrator: Beginning termination.")
    pause(1)

    animate_text("Sarah Connor: Kyle!")
    animate_text("Kyle Reese: Get back!")
    play_sfx("explosion")
    pause(1)

    animate_text("The infiltrator smashes through a parked car.")
    play_sfx("hit")
    pause(1)

    animate_text("Sarah Connor: It's strong!")
    animate_text("Kyle Reese: Stronger than the older models.")
    pause(1)

    animate_text("The machine slowly walks through the smoke.")
    animate_text("Its glowing red eyes lock onto Sarah.")
    play_sfx("warning")
    pause(1)

    animate_text(">>> ENCOUNTER: INFILTRATOR UNIT <<<", 0.01)
    play_sfx("alert")
    pause(1)

    animate_text("'The Infiltrator attacks!'", 0.02)
    play_sfx("hit")
    pause(1)

    animate_text("Kyle Reese: Stay behind me, Sarah.")
    animate_text("Sarah Connor: Be careful.")
    pause(2)


# Level 4 Combat
def level4(player_state):
    username = player_state["username"]

    level4_dialogue()

    animate_text("Level 4: Infiltrator Unit", 0.02)
    pause(1)

    # Combat System
    win, new_hp = start_combat(
        player_state["hp"],
        "Infiltrator",
        75,
        9,
        13,
        player_damage=player_state["damage"]
    )

    player_state["hp"] = new_hp

    # After Combat
    if win:

        animate_text("The infiltrator sparks violently.")
        play_sfx("explosion")
        pause(1)

        animate_text("The machine collapses onto the street.")
        pause(1)

        animate_text("Sarah Connor: It looked completely human...")
        animate_text(f"Kyle Reese: That's how they hunt, {username}.")
        pause(1)

        animate_text("Kyle Reese: The newer machines are harder to detect.")
        animate_text("Sarah Connor: So anyone could be one of them?")
        animate_text("Kyle Reese: That's the terrifying part.")
        pause(1)

        player_state["coins"] += 75
        player_state["xp"] += 65
        player_state = check_level_up(player_state)

        animate_text("MISSION COMPLETE: LEVEL 4")

    else:

        animate_text("Kyle Reese falls to the ground.")
        pause(1)

        animate_text("The infiltrator slowly walks toward Sarah Connor.")
        play_sfx("warning")
        pause(1)

        animate_text("MISSION FAILED")
        player_state["game_over"] = True

        return player_state

    result = post_level_menu(
        player_state["hp"],
        player_state["coins"],
        player_state["xp"],
        player_state["inventory"],
        player_state
    )

    player_state["hp"] = result[0]
    player_state["coins"] = result[1]
    player_state["xp"] = result[2]

    action = result[5]

    if action == "leave_campaign":
        player_state["leave_campaign"] = True
        return player_state