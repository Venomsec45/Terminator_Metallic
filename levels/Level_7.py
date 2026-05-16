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

def level7_dialogue():
    animate_text("Rain pours heavily across the empty highway.")
    animate_text("Police sirens echo in the distance.")
    pause(1)

    animate_text("John Connor: We lost him... right?")
    animate_text("T-800: Negative.")
    animate_text("T-800: The T-1000 does not stop.")
    pause(1)

    animate_text("Sarah Connor reloads her shotgun nervously.")
    animate_text("Sarah Connor: Then why isn't it attacking?")
    animate_text("T-800: It is waiting.")
    animate_text("T-800: Studying us.")
    pause(1)

    animate_text("A large truck suddenly crashes through nearby barricades.")
    pause(1)

    animate_text("John Connor: Oh no...")
    animate_text("Sarah Connor: Everybody MOVE!")
    pause(1)

    animate_text("The T-1000 steps out of the flames unharmed.")
    pause(1)

    animate_text("T-1000: John Connor.")
    animate_text("T-1000: You cannot escape.")
    pause(1)

    animate_text("John Connor: WHY WON'T YOU DIE?!")
    animate_text("The T-1000's face slowly reforms from liquid metal.")
    pause(1)

    animate_text("T-800: Get on the motorcycle.")
    animate_text("Sarah Connor: NOW!")
    pause(1)

    animate_text(">>> OBJECTIVE: ESCAPE THE T-1000 <<<", 0.01)
    # Fight
    pause(1)

    animate_text("The motorcycle speeds into the storm.")
    pause(1)

    animate_text("John Connor: It's gaining on us!")
    animate_text("Sarah Connor fires at the windshield.")
    pause(1)

    animate_text("The truck smashes through abandoned cars.")
    animate_text("Metal explodes everywhere.")
    pause(1)

    animate_text("T-800: Incoming collision.")
    animate_text("Sarah Connor: HOLD ON!")
    pause(2)

def level7(player_state):
    username = player_state["username"]

    level7_dialogue()

    animate_text("Level 7: Highway Escape", 0.02)
    pause(1)

    animate_text("The storm grows stronger as the chase intensifies.")
    animate_text("The T-1000 closes in on the motorcycle.")
    pause(1)

    # Combat
    win, new_hp = start_combat(
        player_state["hp"],
        "T-1000 Pursuit Unit",
        125,
        11,
        15,
        player_damage=player_state["damage"]
    )

    player_state["hp"] = new_hp

    if not win:
        animate_text("The motorcycle crashes violently into the wreckage.")
        animate_text("MISSION FAILED")
        player_state["game_over"] = True
        return player_state

    animate_text("The T-1000 is knocked back—but not destroyed.")
    animate_text("It reforms instantly behind them.")
    pause(1)

    animate_text("T-800: It is still active.")
    animate_text("Sarah Connor: Of course it is...")
    pause(1)

    animate_text("The chase continues through burning debris.")
    pause(1)

    # Combat 2nd part
    win, new_hp = start_combat(
        player_state["hp"],
        "T-1000 Highway Form",
        150,
        13,
        17,
        is_boss=True,
        player_damage=player_state["damage"]
    )

    player_state["hp"] = new_hp

    if win:

        animate_text("The T-1000 loses balance mid-pursuit.")
        animate_text("It collapses into molten metal on the highway.")
        pause(1)

        animate_text("John Connor: Did we finally lose it?")
        animate_text("T-800: Temporarily.")
        pause(1)

        animate_text("Sarah Connor: That thing just won't stay down...")
        pause(1)

        player_state["coins"] += 110
        player_state["xp"] += 110
        player_state = check_level_up(player_state)

        animate_text("MISSION COMPLETE: LEVEL 7")

    else:

        animate_text("The T-1000 overtakes the motorcycle.")
        animate_text("Everything goes black in the crash.")
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