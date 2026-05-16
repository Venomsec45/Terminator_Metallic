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

def level8(player_state):
    username = player_state["username"]

    level8_dialogue()

    animate_text("Level 8: Pescadero Outbreak", 0.02)
    pause(1)

    animate_text("The hospital is now in full lockdown.")
    animate_text("Steel doors slam shut across the corridors.")
    pause(1)

    # Combat 1st part
    win, new_hp = start_combat(
        player_state["hp"],
        "T-1000 Infiltrator",
        150,
        12,
        16,
        player_damage=player_state["damage"]
    )

    player_state["hp"] = new_hp

    if not win:
        animate_text("The T-1000 breaks through the barricade.")
        animate_text("The hallway goes silent.")
        animate_text("MISSION FAILED")
        player_state["game_over"] = True
        return player_state

    animate_text("The T-1000 staggers—but immediately reforms.")
    animate_text("It adapts to every shot fired.")
    pause(1)

    animate_text("T-800: It is learning faster.")
    animate_text("Sarah Connor: Then we don’t have much time.")
    pause(1)

    animate_text("Emergency alarms intensify across the hospital.")
    pause(1)

    # Combat 2nd part
    win, new_hp = start_combat(
        player_state["hp"],
        "T-1000 Hallway Form",
        175,
        13,
        18,
        is_boss=True,
        player_damage=player_state["damage"]
    )

    player_state["hp"] = new_hp

    if win:

        animate_text("The T-1000 collapses into a liquid pool.")
        animate_text("It flows through the cracks in the floor.")
        pause(1)

        animate_text("John Connor: Did we stop it?")
        animate_text("T-800: Negative.")
        animate_text("T-800: It has retreated.")
        pause(1)

        animate_text("Sarah Connor: It always comes back...")
        pause(1)

        player_state["coins"] += 120
        player_state["xp"] += 120
        player_state = check_level_up(player_state)

        animate_text("MISSION COMPLETE: LEVEL 8")

    else:

        animate_text("The lights flicker one final time.")
        animate_text("Everything cuts to black.")
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
