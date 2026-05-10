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


# Level 2 Dialogue
def level2_dialogue():

    animate_text("Cold wind blows through the ruined streets.")
    pause(1)

    animate_text("Sarah Connor: Kyle...")
    animate_text("Sarah Connor: How far do we have to go?")
    pause(1)

    animate_text("Kyle Reese: Far enough to stay alive.")
    animate_text("Kyle Reese: The Resistance had safe routes in the future.")
    animate_text("Kyle Reese: But this time period is different.")
    pause(1)

    animate_text("Sarah Connor: Future...")
    animate_text("Sarah Connor: You keep saying that like it's normal.")
    animate_text("Sarah Connor: None of this feels real.")
    pause(1)

    animate_text("Kyle Reese: I know.")
    animate_text("Kyle Reese: The first time I saw one of these machines...")
    animate_text("Kyle Reese: I couldn't believe it either.")
    pause(1)

    animate_text("Sarah Connor: What happened?")
    pause(1)

    animate_text("Kyle Reese: My entire squad disappeared in one night.")
    animate_text("Kyle Reese: We thought we were fighting soldiers.")
    animate_text("Kyle Reese: Then the machines came.")
    pause(1)

    animate_text("Sarah Connor: Machines don't feel anything...")
    animate_text("Kyle Reese: Exactly.")
    animate_text("Kyle Reese: They don't get tired.")
    animate_text("Kyle Reese: They don't panic.")
    animate_text("Kyle Reese: And they never stop hunting.")
    pause(1.5)

    animate_text("A deep mechanical humming sound echoes overhead...")
    play_sfx("warning")
    pause(1)

    animate_text("Sarah Connor: Wait...")
    animate_text("Sarah Connor: Do you hear that?")
    pause(1)

    animate_text("Kyle Reese suddenly looks up.")
    animate_text("Kyle Reese: Get down!")
    play_sfx("alert")
    pause(1)

    animate_text("A powerful searchlight sweeps across the street.")
    animate_text("Dust and debris scatter violently.")
    pause(1)

    animate_text("Sarah Connor: What is that thing?!")
    animate_text("Kyle Reese: Assault drone.")
    animate_text("Kyle Reese: Heavier armor.")
    animate_text("Kyle Reese: Military-grade weapons.")
    pause(1)

    animate_text("Sarah Connor: Can it see us?")
    animate_text("Kyle Reese: Not yet.")
    animate_text("Kyle Reese: But if it locks on, we're finished.")
    pause(1)

    animate_text("The drone slowly turns toward their hiding spot.")
    play_sfx("warning")
    pause(1)

    animate_text("Sarah Connor: Kyle...")
    animate_text("Kyle Reese: Stay behind cover.")
    animate_text("Kyle Reese: Don't move unless I tell you.")
    pause(1)

    animate_text("The drone emits a loud scanning sound.")
    play_sfx("alert")
    pause(1)

    animate_text("Sarah Connor: I think it found us.")
    animate_text("Kyle Reese: Yeah...")
    animate_text("Kyle Reese: It found us.")
    pause(1)

    animate_text(">>> ENCOUNTER: ASSAULT DRONE <<<", 0.01)
    play_sfx("warning")
    pause(1)

    animate_text("'The Assault Drone attacks!'", 0.02)
    play_sfx("hit")
    pause(1)

    animate_text("Missiles launch from the drone's side compartments!")
    play_sfx("explosion")
    pause(1)

    animate_text("Sarah Connor: MOVE!")
    pause(1)

    animate_text("A massive explosion tears through the street.")
    play_sfx("explosion")
    pause(1)

    animate_text("Kyle Reese: Keep your head down!")
    animate_text("Sarah Connor: It's destroying everything!")
    pause(1)

    animate_text("The drone fires rapidly into the ruins.")
    play_sfx("hit")
    pause(1)

    animate_text("Sarah Connor: Kyle, it's coming closer!")
    animate_text("Kyle Reese: I know!")
    animate_text("Kyle Reese: I need a clear shot!")
    pause(1)

    animate_text("Kyle reloads his weapon while sparks rain overhead.")
    pause(1)

    animate_text("Sarah Connor: How many of these things exist in the future?")
    animate_text("Kyle Reese: Too many.")
    animate_text("Kyle Reese: Entire cities burn because of machines like this.")
    pause(1)

    animate_text("The drone charges another missile barrage.")
    play_sfx("warning")
    pause(1)

    animate_text("Kyle Reese: Get back!")
    play_sfx("explosion")
    pause(1)

    animate_text("The explosion lights up the entire street.")
    pause(1)

    animate_text("Sarah Connor: We can't keep surviving this!")
    animate_text("Kyle Reese: We don't need to survive forever.")
    animate_text("Kyle Reese: We just need to survive tonight.")
    pause(2)


# Level 2 combat
def level2(player_state):
    username = player_state["username"]

    level2_dialogue()

    animate_text("Level 2: Assault Drone", 0.02)
    pause(1)

    # Combat System
    win, new_hp = start_combat(
        player_state["hp"],
        "Assault Drone",
        40,
        6,
        10
    )

    player_state["hp"] = new_hp

    # After Combat
    if win:

        animate_text("The Assault Drone spins out of control!")
        pause(1)

        animate_text("It crashes into the side of a ruined building.")
        play_sfx("explosion")
        pause(1)

        animate_text("Flames erupt across the street.")
        pause(1)

        animate_text(f"Sarah Connor: We actually destroyed it, {username}!")
        animate_text("Kyle Reese: Barely.")
        animate_text("Kyle Reese: And the noise will attract more machines.")
        pause(1)

        animate_text("Sarah Connor: Then let's keep moving.")
        animate_text("Kyle Reese: Stay close.")
        animate_text("Kyle Reese: This city gets more dangerous at night.")
        pause(1)

        player_state["coins"] += 50
        player_state["xp"] += 35
        player_state = check_level_up(player_state)

        animate_text("MISSION COMPLETE: LEVEL 2")

    else:

        animate_text("Kyle Reese collapses as explosions surround the area.")
        pause(1)

        animate_text("Sarah Connor: Kyle!")
        animate_text("The Assault Drone hovers overhead as alarms echo through the ruins.")
        pause(1)

        animate_text("MISSION FAILED")

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

    if result[5] == "exit":
        exit()

    return player_state