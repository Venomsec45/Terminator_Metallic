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


def level9(player_state):
    username = player_state["username"]

    level9_dialogue()

    animate_text("Level 9: Dyson Residence Assault", 0.02)
    pause(1)

    animate_text("The house feels suffocatingly quiet.")
    animate_text("Every second feels like the moment before disaster.")
    pause(1)

    # Combat 1
    win, new_hp = start_combat(
        player_state["hp"],
        "Cyberdyne Security Unit",
        200,
        12,
        17,
        player_damage=player_state["damage"]
    )

    player_state["hp"] = new_hp

    if not win:
        animate_text("Gunfire overwhelms the group inside the house.")
        animate_text("Everything fades into chaos.")
        animate_text("MISSION FAILED")
        player_state["game_over"] = True
        return player_state

    animate_text("The security unit collapses on the floor.")
    animate_text("The silence that follows feels heavier than before.")
    pause(1)

    animate_text("Miles Dyson: I never meant for this...")
    animate_text("Sarah Connor: Intent doesn’t matter anymore.")
    pause(1)

    animate_text("T-800: Additional hostiles detected.")
    animate_text("T-800: They are not stopping.")
    pause(1)

    animate_text("Windows shatter as reinforcements arrive.")
    pause(1)

    # Combat 2
    win, new_hp = start_combat(
        player_state["hp"],
        "Cyberdyne Assault Squad",
        225,
        14,
        19,
        is_boss=True,
        player_damage=player_state["damage"]
    )

    player_state["hp"] = new_hp

    if win:

        animate_text("The final attacker drops its weapon.")
        animate_text("The house slowly falls quiet again.")
        pause(1)

        animate_text("Miles Dyson: I’ll help you stop this.")
        animate_text("Miles Dyson: No matter what it takes.")
        pause(1)

        animate_text("John Connor: Then we move fast.")
        pause(1)

        player_state["coins"] += 130
        player_state["xp"] += 130
        player_state = check_level_up(player_state)

        animate_text("MISSION COMPLETE: LEVEL 9")

    else:

        animate_text("The defense line collapses completely.")
        animate_text("The mission fails as the house is overtaken.")
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