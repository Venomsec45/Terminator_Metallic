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


def level10(player_state):
    username = player_state["username"]

    level10_dialogue()

    animate_text("Level 10: Cyberdyne Final Assault", 0.02)
    pause(1)

    animate_text("The entire facility is collapsing under heavy fire.")
    animate_text("This is the final stand against Skynet's creation.")
    pause(1)

    # Phase 1: Swat assault

    animate_text("\n--- PHASE 1: SWAT BREACH ---", 0.02)
    pause(1)

    win, new_hp = start_combat(
        player_state["hp"],
        "SWAT Assault Unit",
        180,
        14,
        18,
        player_damage=player_state["damage"]
    )

    player_state["hp"] = new_hp

    if not win:
        animate_text("The SWAT units overwhelm the resistance.")
        animate_text("MISSION FAILED")
        player_state["game_over"] = True
        return player_state

    animate_text("SWAT units are down... but something else is coming.")
    pause(1)

    # Phase 2 T-1000 Prototype Form
    animate_text("\n--- PHASE 2: T-1000 PROTOTYPE ---", 0.02)
    pause(1)

    win, new_hp = start_combat(
        player_state["hp"],
        "T-1000 Prototype Form",
        200,
        16,
        20,
        is_boss=True,
        player_damage=player_state["damage"]
    )

    player_state["hp"] = new_hp

    if not win:
        animate_text("The T-1000 overwhelms the team.")
        animate_text("MISSION FAILED")
        player_state["game_over"] = True
        return player_state

    animate_text("The T-1000 collapses… but begins to reform.")
    animate_text("Warning: Regeneration detected.")
    pause(1)


    # Phase 3: FInal form with boss HP regen

    animate_text("\n--- PHASE 3: FINAL FORM ---", 0.02)
    pause(1)

    animate_text("The T-1000 stabilizes into its most dangerous state.")
    animate_text("It will not stay down.")
    pause(1)

    win, new_hp = start_combat(
        player_state["hp"],
        "T-1000 Final Form",
        250,
        18,
        22,
        is_boss=True,
        player_damage=player_state["damage"]
    )

    player_state["hp"] = new_hp

    if win:

        animate_text("The T-1000 finally loses structural stability.")
        animate_text("Its form dissolves into inert liquid metal.")
        pause(1)

        animate_text("John Connor: It’s finally over...")
        animate_text("T-800: Confirmed termination.")
        pause(1)

        player_state["coins"] += 250
        player_state["xp"] += 180
        player_state = check_level_up(player_state)

        animate_text("MISSION COMPLETE: LEVEL 10")

    else:

        animate_text("The T-1000 adapts beyond control.")
        animate_text("Everything is lost in the collapse.")
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