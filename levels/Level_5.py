from combat_system import start_combat
from menu import post_level_menu
from player_levels import check_level_up
import time
import sys
import os


# Text Animations
def animate_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def pause(seconds=1):
    time.sleep(seconds)


# Simple Sound Effects
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


# Level 5 Dialogue
def level5_dialogue():

    animate_text("The city streets fall silent.")
    pause(1)

    animate_text("Sarah Connor: Why did everything suddenly stop?")
    animate_text("Kyle Reese slowly looks around.")
    pause(1)

    animate_text("Kyle Reese: Because something is here.")
    play_sfx("warning")
    pause(1)

    animate_text("Heavy footsteps echo through the street.")
    play_sfx("boss")
    pause(1)

    animate_text("THUD...")
    pause(1)

    animate_text("THUD...")
    pause(1)

    animate_text("Sarah Connor: That's not the infiltrator from before...")
    animate_text("Kyle Reese: No.")
    animate_text("Kyle Reese: This is worse.")
    pause(1)

    animate_text("A large figure slowly walks out of the darkness.")
    pause(1)

    animate_text("Its red eyes glow through the smoke.")
    animate_text("Metal shines beneath torn synthetic skin.")
    play_sfx("alert")
    pause(1)

    animate_text("Kyle Reese: T-800.")
    animate_text("Sarah Connor: That's the machine you warned me about?")
    animate_text("Kyle Reese: The first cybernetic organism.")
    animate_text("Kyle Reese: Living tissue over a metal endoskeleton.")
    pause(1)

    animate_text("Sarah Connor: Can we kill it?")
    animate_text("Kyle Reese: We can try.")
    pause(1)

    animate_text("The T-800 slowly scans the area.")
    animate_text("Its eyes lock directly onto Sarah Connor.")
    play_sfx("warning")
    pause(1)

    animate_text("T-800: Sarah Connor identified.")
    animate_text("T-800: Termination required.")
    pause(1)

    animate_text("Sarah Connor: Kyle...")
    animate_text("Kyle Reese reloads his weapon.")
    animate_text("Kyle Reese: Stay behind me.")
    pause(1)

    animate_text("The T-800 begins walking forward.")
    animate_text("It doesn't hesitate.")
    animate_text("It doesn't slow down.")
    play_sfx("boss")
    pause(1)

    animate_text("Kyle Reese: RUN!")
    play_sfx("explosion")
    pause(1)

    animate_text("The T-800 smashes through a police car.")
    animate_text("Metal flies across the street.")
    play_sfx("hit")
    pause(1)

    animate_text("Sarah Connor: It just walked through that!")
    animate_text("Kyle Reese: That's what makes it terrifying.")
    pause(1)

    animate_text("The machine continues advancing through the flames.")
    play_sfx("warning")
    pause(1)

    animate_text(">>> BOSS: T-800 <<<", 0.01)
    play_sfx("boss")
    pause(1)

    animate_text("'Boss Fight Begins'", 0.02)
    play_sfx("hit")
    pause(1)

    animate_text("Kyle Reese: No matter what happens...")
    animate_text("Kyle Reese: Do not stop moving.")
    pause(2)


# Level 5 Combat
def level5(player_state):
    username = player_state["username"]

    level5_dialogue()

    animate_text("Level 5: BOSS - T-800", 0.02)
    pause(1)

    animate_text("A heavily armored Terminator approaches...")
    animate_text("It will not stop until you are terminated.")
    pause(1)

    # Combat System
    win, new_hp = start_combat(
        player_state["hp"],
        "T-800",
        100,
        12,
        18,
        is_boss=True,
        player_damage=player_state["damage"]
    )

    player_state["hp"] = new_hp

    # After Combat
    if win:

        animate_text("The T-800 staggers backward.")
        play_sfx("warning")
        pause(1)

        animate_text("Sparks burst from its damaged endoskeleton.")
        play_sfx("explosion")
        pause(1)

        animate_text("The machine slowly collapses onto the street.")
        pause(1)

        animate_text("Sarah Connor: Is it over?")
        animate_text("Kyle Reese: I think so...")
        pause(1)

        animate_text(f"Kyle Reese: Nice work, {username}.")
        animate_text("Kyle Reese: Most people never survive a T-800 encounter.")
        pause(1)

        animate_text("Sarah Connor stares at the destroyed machine.")
        animate_text("Sarah Connor: That thing felt unstoppable.")
        pause(1)

        animate_text("Kyle Reese: And in the future...")
        animate_text("Kyle Reese: Thousands of them exist.")
        pause(1)

        player_state["coins"] += 95
        player_state["xp"] += 80
        player_state = check_level_up(player_state)

        animate_text("MISSION COMPLETE: LEVEL 5")

    else:

        animate_text("Kyle Reese falls to the ground.")
        pause(1)

        animate_text("The T-800 slowly turns toward Sarah Connor.")
        play_sfx("warning")
        pause(1)

        animate_text("T-800: Target remaining.")
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
    player_state["inventory"] = result[3]

    action = result[-1]

    if action == "leave_campaign":
        player_state["leave_campaign"] = True
        return player_state
    
    return player_state