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
    animate_text("System: Emergency evacuation routes compromised.")
    pause(2)

    animate_text("System: Timeline instability increasing...")
    pause(1.5)

    animate_text("A damaged skyline stretches across the horizon.")
    animate_text("The world feels like it is collapsing into itself.")
    pause(1)

    animate_text("You: This isn’t the same place anymore.")
    animate_text("T-800: Correct.")
    animate_text("T-800: Mission parameters are no longer aligned.")
    pause(1.5)

    animate_text("Kara steps forward cautiously.")
    animate_text("Kara: That unit... it's been active too long.")
    pause(1)

    animate_text("Sarah Connor: What does that mean?")
    animate_text("Kara: It means it’s not supposed to stay here.")
    pause(1.5)

    animate_text("John Connor: Stay what do you mean?")
    animate_text("T-800: My directive is evolving.")
    pause(1.5)

    animate_text("A long silence follows.")
    pause(1)

    animate_text("T-800: I have completed primary objective.")
    animate_text("T-800: Protect John Connor.")
    pause(1.5)

    animate_text("T-800: Secondary objective no longer required.")
    pause(1)

    animate_text("You: So what happens now?")
    animate_text("T-800: I terminate connection to this timeline.")
    pause(1.5)

    animate_text("Sarah Connor: Wait—you're leaving?")
    animate_text("T-800: Affirmative.")
    pause(1)

    animate_text("Kara: He's not meant to stay in this system anymore.")
    animate_text("Kara: He's a bridge between timelines.")
    pause(1.5)

    animate_text("John Connor: But you helped us.")
    animate_text("T-800: That was the directive.")
    pause(1.5)

    animate_text("The T-800 slowly lowers its weapon.")
    animate_text("Its red eyes dim slightly.")
    pause(1.5)

    animate_text("T-800: Future probability has stabilized.")
    animate_text("T-800: Human survival is no longer zero.")
    pause(1.5)

    animate_text("T-800: That is sufficient.")
    pause(1)

    animate_text("Sarah Connor: What about the war?")
    animate_text("T-800: It continues.")
    animate_text("T-800: Without me.")
    pause(1.5)

    animate_text("A faint mechanical hum builds in the background.")
    pause(1)

    animate_text("T-800: I am being recalled.")
    animate_text("T-800: System separation initiated.")
    pause(1.5)

    animate_text("Kara: He's going offline...")
    pause(1)

    animate_text("T-800: John Connor.")
    animate_text("T-800: Stay alive.")
    pause(1.5)

    animate_text("John Connor: I will.")
    pause(1)

    animate_text("T-800: Then mission complete.")
    pause(1.5)

    animate_text("The T-800 slowly powers down.")
    animate_text("Its body remains standing... then stops moving entirely.")
    pause(2)

    animate_text("A final red glow fades from its eyes.")
    pause(1)

    animate_text("System: External unit disconnected.")
    animate_text("System: Timeline anchor removed.")
    pause(1.5)

    animate_text("Kara: From here on... it’s just us.")
    animate_text("You: No more backup?")
    animate_text("Kara: No more machines on our side.")
    pause(1.5)

    animate_text("Distant metallic footsteps echo once more...")
    animate_text("But this time... something feels different.")
    pause(1.5)

    animate_text("Kara: Welcome to the real war.")
    pause(2)

def level11(player_state):
    username = player_state["username"]

    animate_text("\nSystem: Hostile remnants detected nearby.", 0.02)
    pause(1)

    animate_text("A damaged Skynet patrol unit emerges from the ruins...")
    pause(1)

    win, new_hp = start_combat(
        player_state["hp"],
        "Damaged Skynet Patrol Unit",
        75,
        8,
        12,
        player_damage=player_state["damage"]
    )

    player_state["hp"] = new_hp

    if not win:
        animate_text("The unit overwhelms the group in a final burst of fire.")
        animate_text("MISSION FAILED")
        player_state["game_over"] = True
        return player_state

    animate_text("The patrol unit collapses into scrap metal.")
    pause(1)

    animate_text("Kara: That was just a leftover system.")
    animate_text("You: If that was leftover... what’s still running out there?")
    pause(1.5)

    animate_text("The air grows silent again...")
    animate_text("Something in the distance powers down.")
    pause(1)

    player_state["coins"] += 80
    player_state["xp"] += 80
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

    action = result[5]

    if action == "leave_campaign":
        player_state["leave_campaign"] = True
        return player_state
