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


def level12_dialogue_1():
    animate_text("System: Initializing mission...")
    pause(2)

    animate_text("System: Loading sector map...")
    pause(2)

    animate_text("System: Location [Abandoned Skynet Military Facility]")
    animate_text("System: Weather Status [Extreme Storm Activity]")
    pause(1.5)

    animate_text("Thunder rumbles across the dead city.")
    animate_text("Cold wind whistles through broken metal walls.")
    pause(1)

    animate_text("You: This place feels like a graveyard.")
    animate_text("Kara: That’s because it is.")
    pause(1)

    animate_text("You: You’ve been here before?")
    animate_text("Kara: Years ago. Before the machines took control.")
    pause(1.5)

    animate_text("Electric sparks flicker from damaged ceiling wires.")
    animate_text("System: Power levels unstable.")
    pause(1)

    animate_text("Metal door slowly creaks open.")
    animate_text("Distant metallic footsteps echo.")
    animate_text("CLANG... CLANG... CLANG...")
    pause(1.5)

    animate_text("Kara: Weapons ready.")
    animate_text("System: Motion detected.")
    animate_text("System: Unknown hostile signature.")
    pause(1.5)

    animate_text("Two glowing red eyes appear in darkness.")
    pause(1.5)

    animate_text("Terminator Unit: Target identified.")
    animate_text("You: CONTACT!")


def level12_dialogue_2():
    animate_text("Kara: Take cover!")
    animate_text("Bullets spark against reinforced armor.")
    pause(1)

    animate_text("Terminator Unit: Resistance is irrational.")
    animate_text("You: Yeah? So is walking into bullets!")
    pause(1)

    animate_text("Kara throws an explosive.")
    animate_text("BOOM!")
    pause(1)

    animate_text("Smoke fills the corridor.")
    animate_text("You: Did we get it?")
    pause(1)

    animate_text("A metal hand slowly pushes through the smoke.")
    animate_text("Terminator Unit: Mission continues.")
    pause(1)

    animate_text("Kara: RUN!")
    pause(1)

    animate_text("Warning: Additional hostiles awakening.")
    animate_text("System: Reinforcement detected.")
    pause(1)

    animate_text("You: There’s MORE?!")
    animate_text("Rows of dormant machines begin powering on.")
    pause(1)

    animate_text("System: Defense protocol activated.")
    animate_text("You: I think we made them angry.")
    pause(1)

    animate_text("Kara: You think?!")
    pause(1)

    animate_text("A steel door slams shut behind them.")
    animate_text("Loud pounding starts immediately.")
    pause(1)

    animate_text("Kara: This way!")
    animate_text("They enter an old command room filled with dead systems.")
    pause(1)

    animate_text("System: Unauthorized access detected.")
    animate_text("Unknown AI: Judgment Day protocol remains active.")
    pause(1)

    animate_text("You: Of course it is...")
    animate_text("Kara: Keep moving!")
    pause(1)

    animate_text("The facility begins shaking.")
    animate_text("System: Structural failure imminent.")
    pause(1)

    animate_text("You: That sounds bad.")
    animate_text("Kara: Because it is!")
    pause(1)

    animate_text("Unknown AI: Humanity will not survive termination.")
    animate_text("You: We’ll see about that.")
    pause(1)

    animate_text("Emergency systems begin collapsing around them.")


def level12(player_state):
    username = player_state["username"]

    level12_dialogue_1()

    animate_text("\nLevel 12: T-7 Assault System")
    pause(1)

    win, new_hp = start_combat(
        player_state["hp"],
        "T-7 Unit (Phase 1)",
        150,
        10,
        14,
        player_damage=player_state["damage"]
    )

    player_state["hp"] = new_hp

    if not win:
        animate_text("The unit overwhelms the team in seconds.")
        animate_text("MISSION FAILED")
        player_state["game_over"] = True
        return player_state

    animate_text("The first unit collapses into broken metal.")
    pause(1)

    animate_text("System: Secondary signature detected.")
    animate_text("Kara: That wasn’t the main one...")
    pause(1)

    win, new_hp = start_combat(
        player_state["hp"],
        "T-7 Core Unit (Phase 2)",
        225,
        12,
        16,
        is_boss=True,
        player_damage=player_state["damage"]
    )

    player_state["hp"] = new_hp

    if not win:
        animate_text("The core unit regenerates faster than expected.")
        animate_text("MISSION FAILED")
        player_state["game_over"] = True
        return player_state

    animate_text("The second unit finally collapses...")
    animate_text("Its system shuts down completely.")
    pause(1)

    animate_text("Kara: That was only a forward defense system.")
    animate_text("You: Then what’s deeper inside?")
    pause(1.5)

    level12_dialogue_2()

    player_state["coins"] += 150
    player_state["xp"] += 100
    player_state = check_level_up(player_state)

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