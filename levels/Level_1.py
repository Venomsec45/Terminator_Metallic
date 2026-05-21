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

# Simple sound effects
def play_sfx(name):
    if os.name == "nt":  # Windows only
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


# LEVEL 1 DIALOGUE
def level1_dialogue():
    animate_text("Sarah Connor: Kyle… you said they would come. But this soon?")
    animate_text("Kyle Reese: Earlier than expected.")
    animate_text("Kyle Reese: Something changed in the timeline.")
    pause(1)

    animate_text("Sarah Connor: Timeline?")
    animate_text("Kyle Reese: The future.")
    animate_text("Kyle Reese: The war.")
    animate_text("Kyle Reese: Everything is happening faster than it should.")
    pause(1)

    animate_text("Sarah Connor: I still don't understand any of this.")
    animate_text("Sarah Connor: Yesterday I was just living my normal life.")
    animate_text("Sarah Connor: Now you're telling me machines from the future are hunting me.")
    pause(1)

    animate_text("Kyle Reese: I know how it sounds.")
    animate_text("Kyle Reese: But the machines don't stop.")
    animate_text("Kyle Reese: Once Skynet marks a target, it keeps coming.")
    pause(1.5)

    animate_text("A faint mechanical buzzing echoes through the alley...")
    play_sfx("alert")
    pause(1)

    animate_text("Sarah Connor: Wait...")
    animate_text("Sarah Connor: Do you hear that?")
    animate_text("Kyle Reese: Stay close to me.")
    animate_text("Kyle Reese: Don't move.")
    pause(1)

    animate_text("A red scanning light sweeps across the walls.")
    play_sfx("warning")
    pause(1)

    animate_text("Sarah Connor: Oh my God...")
    animate_text("Sarah Connor: What is that thing?")
    animate_text("Kyle Reese: Scout drone.")
    animate_text("Kyle Reese: Surveillance model.")
    animate_text("Kyle Reese: Fast. Lightweight. Dangerous.")
    pause(1)

    animate_text("Sarah Connor: It doesn't look armed.")
    animate_text("Kyle Reese: It doesn't need to be.")
    animate_text("Kyle Reese: If it alerts nearby units, we're dead.")
    pause(1)

    animate_text("The drone slowly turns toward them.")
    play_sfx("alert")
    pause(1)

    animate_text("Sarah Connor: Kyle...")
    animate_text("Kyle Reese: Get behind me.")
    animate_text("Sarah Connor: Can we hide?")
    animate_text("Kyle Reese: Too late.")
    pause(1)

    animate_text(">>> ENCOUNTER: SCOUT DRONE <<<", 0.01)
    play_sfx("warning")
    pause(1)

    animate_text("'The Scout Drone attacks!'", 0.02)
    play_sfx("hit")
    pause(1)

    animate_text("Sarah Connor: It's moving!")
    animate_text("Kyle Reese: Stay down!")
    play_sfx("hit")
    pause(1)

    animate_text("The drone fires sparks as it rushes forward.")
    play_sfx("alert")
    pause(1)

    animate_text("Sarah Connor: Watch out!")
    animate_text("Kyle Reese: I see it!")
    play_sfx("hit")
    pause(1)

    animate_text("Kyle slams the drone against the wall.")
    animate_text("Metal scrapes violently across concrete.")
    play_sfx("explosion")
    pause(1)

    animate_text("The drone twitches violently.")
    animate_text("Its red eye flickers.")
    pause(1)

    animate_text("Sarah Connor: Is it dead?")
    animate_text("Kyle Reese: Machines don't die easy.")
    pause(1)

    animate_text("The drone suddenly emits a sharp transmission sound.")
    play_sfx("warning")
    pause(1)

    animate_text("Sarah Connor: What was that?")
    animate_text("Kyle Reese: A signal.")
    animate_text("Kyle Reese: It just told every machine nearby where we are.")
    pause(1.5)

    animate_text("Sarah Connor: Then we have to leave. Right now.")
    animate_text("Kyle Reese: We will.")
    animate_text("Kyle Reese: But they're already coming.")
    pause(1)

    animate_text("Heavy thunder echoes in the distance.")
    animate_text("Kyle Reese slowly reloads his weapon.")
    pause(1)

    animate_text("Kyle Reese: This was only the first one.")
    animate_text("Kyle Reese: The real hunt starts now.")
    pause(2)


# Level 1 combat
def level1(player_state):
    username = player_state["username"]

    level1_dialogue()

    animate_text("Level 1: Scout Encounter", 0.02)
    pause(1)

    win, new_hp = start_combat(
        player_state["hp"],
        "Scout Drone",
        30,
        5,
        8,
        player_damage=player_state["damage"]
    )

    player_state["hp"] = new_hp

    if win:
        animate_text("The Scout Drone collapses into burning scrap.")
        play_sfx("explosion")
        pause(1)

        animate_text(f"Kyle Reese: Nice work, {username}.")
        animate_text("Sarah Connor: That thing almost killed us...")
        animate_text("Kyle Reese: And worse machines are coming.")
        pause(1)

        player_state["coins"] += 25
        player_state["xp"] += 20 
        player_state = check_level_up(player_state)

        animate_text("MISSION COMPLETE: LEVEL 1")
        pause(1)

    else:
        animate_text("Kyle Reese falls to the ground...")
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