from combat_system import start_combat
from menu import post_level_menu
from player_levels import check_level_up
import os
import sys
import time


def animate_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def pause(seconds=1):
    time.sleep(seconds)

def level13_dialogue_1():
    animate_text("Cold wind blows through the cemetery.")
    animate_text("Thunder rumbles in the distance.")

    animate_text("You: Why would the Resistance hide weapons here?")
    animate_text("Kara: Because nobody comes here anymore.")
    animate_text("Kara: Even machines avoid places like this.")

    animate_text("Metal cemetery gates slowly creak open.")
    pause(1)

    animate_text("System: Low visibility detected.")
    animate_text("Lightning reveals broken tombstones.")
    pause(1)

    animate_text("A distant metallic sound echoes.")
    animate_text("Kara: That wasn't the wind.")
    pause(1)

    animate_text("System: Motion detected nearby.")

    animate_text("A Scout Drone rises behind a tombstone.")
    animate_text("Scout Drone: Target located.")
    animate_text("You: CONTACT!")

def level13_dialogue_2():
    animate_text("Kara: Nice shot.")
    animate_text("You: Lucky shot.")

    animate_text("More red lights appear deeper in the cemetery.")
    pause(1)

    animate_text("Spider crawlers rush across the graves.")
    animate_text("You: WHY ARE THERE SPIDER ROBOTS?!")
    animate_text("Kara: Less screaming. More shooting!")

    animate_text("Rapid gunfire echoes through the graveyard.")
    pause(1)

    animate_text("Spider crawler: Target surrounded.")
    animate_text("You: I officially hate this place!")


def level13_dialogue_3():
    animate_text("Heavy rain begins pouring.")
    pause(1)

    animate_text("Lightning reveals a ruined chapel ahead.")
    animate_text("Kara: The bunker is beneath it.")

    animate_text("System: Heavy unit detected.")

    animate_text("A Heavy terminator steps forward.")
    animate_text("Heavy terminator: Resistance identified.")
    animate_text("You: That's heavy enough!")

    animate_text("Plasma fire erupts across the cemetery.")
    pause(1)

    animate_text("Kara: FALL BACK!")

    animate_text("Both retreat into the chapel.")

    animate_text("THUMP... THUMP... THUMP...")

    animate_text("Heavy terminator: Target persistence active.")

    animate_text("They open the hidden bunker entrance.")

    animate_text("System: Hidden facility detected.")

    animate_text("They descend into the bunker.")
    animate_text("[Silence]")

def level13(player_state):
    username = player_state["username"]

    level13_dialogue_1()

    animate_text("\nLevel 13: Scout Drone Encounter")
    pause(1)

    win, new_hp = start_combat(
        player_state["hp"],
        "Scout Drone",
        125,
        5,
        8,
        player_damage=player_state["damage"]
    )

    player_state["hp"] = new_hp

    if not win:
        animate_text("MISSION FAILED")
        player_state["game_over"] = True
        return player_state

    player_state["coins"] += 125
    player_state["xp"] += 125
    player_state = check_level_up(player_state)

    animate_text("The Scout Drone collapses into scrap.")
    pause(1)

    level13_dialogue_2()

    animate_text("\nLevel 13: Spider Crawler Encounter")
    pause(1)

    win, new_hp = start_combat(
        player_state["hp"],
        "Spider Crawler",
        150,
        7,
        12,
        player_damage=player_state["damage"]
    )

    player_state["hp"] = new_hp

    if not win:
        animate_text("MISSION FAILED")
        player_state["game_over"] = True
        return player_state

    player_state["coins"] += 135
    player_state["xp"] += 140
    player_state = check_level_up(player_state)

    animate_text("The Spider Crawler collapses in sparks.")
    pause(1)

    level13_dialogue_3()

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