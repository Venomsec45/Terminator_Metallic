from combat_system import start_combat
from menu import post_level_menu
from player_levels import check_level_up
import time
import sys
import os


# Text Animation
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


# Level 6 Dialogue
def level6_dialogue():

    animate_text("System: Timeline shift detected.")
    play_sfx("warning")
    pause(1)

    animate_text("The surroundings suddenly change.")
    animate_text("The ruined future disappears.")
    pause(1)

    animate_text("Kyle Reese: What just happened?")
    animate_text("Sarah Connor: Where are we?")
    pause(1)

    animate_text("A digital sign nearby reads: LOS ANGELES - 1995")
    pause(1)

    animate_text("Kyle Reese: This isn't our timeline...")
    animate_text("Kyle Reese: Something changed history.")
    pause(1)

    animate_text("A motorcycle engine echoes nearby.")
    play_sfx("alert")
    pause(1)

    animate_text("John Connor: Mom?")
    animate_text("Sarah Connor: John?!")
    pause(1)

    animate_text("A large figure steps out of the shadows.")
    animate_text("Its red eyes briefly glow.")
    pause(1)

    animate_text("T-800: Come with me if you want to live.")
    play_sfx("boss")
    pause(1)

    animate_text("Kyle Reese raises his weapon immediately.")
    animate_text("Kyle Reese: Another Terminator.")
    pause(1)

    animate_text("John Connor: Wait!")
    animate_text("John Connor: He's here to protect us!")
    pause(1)

    animate_text("Sarah Connor: Protect us?")
    animate_text("T-800: Mission objective updated.")
    animate_text("T-800: Protect John Connor.")
    pause(1)

    animate_text("Suddenly, a police officer approaches silently.")
    pause(1)

    animate_text("Kyle Reese: Something feels wrong.")
    play_sfx("warning")
    pause(1)

    animate_text("T-800: He is not human.")
    pause(1)

    animate_text("The officer suddenly stops moving.")
    animate_text("Its body begins changing shape.")
    play_sfx("alert")
    pause(1)

    animate_text("Sarah Connor: What is that thing?!")
    animate_text("John Connor: I've never seen a Terminator do that!")
    pause(1)

    animate_text("The officer transforms into liquid metal.")
    play_sfx("warning")
    pause(1)

    animate_text("Kyle Reese: That's impossible...")
    animate_text("T-800: Advanced prototype identified.")
    animate_text("T-800: T-1000.")
    pause(1)

    animate_text(">>> ENCOUNTER: T-1000 UNIT <<<", 0.01)
    play_sfx("alert")
    pause(1)

    animate_text("'The T-1000 unit attacks!'", 0.02)
    play_sfx("hit")
    pause(2)


# Level 6 Combat
def level6(player_state):
    username = player_state["username"]

    level6_dialogue()

    animate_text("Level 6: New Timeline Detected", 0.02)
    pause(1)

    # Combat System
    win, new_hp = start_combat(
        player_state["hp"],
        "T-1000 Prototype",
        90,
        10,
        14,
        player_damage=player_state["damage"]
    )

    player_state["hp"] = new_hp

    # After Combat
    if not win:

        animate_text("The T-1000 prototype overpowers the group.")
        pause(1)

        animate_text("MISSION FAILED")
        return player_state

    animate_text("The T-1000 prototype collapses and turns into a puddle of liquid metal.")
    play_sfx("explosion")
    pause(1)

    animate_text("John Connor: Nice shooting!")
    animate_text(f"Sarah Connor: We survived because of you, {username}.")
    pause(1)

    animate_text("Suddenly, the ground ripples strangely nearby.")
    play_sfx("warning")
    pause(1)

    animate_text("T-800: It is not over yet.")
    animate_text("Liquid metal structure forming...")
    pause(1)

    animate_text("The T-1000 slowly reforms in front of them.")
    play_sfx("boss")
    pause(1)

    animate_text("T-1000: Target located.")
    animate_text("T-1000: John Connor.")
    pause(1)

    animate_text("John Connor: It's changing shape!")
    animate_text("Kyle Reese: Stay back!")
    pause(1)

    animate_text(">>> MINI-BOSS: T-1000 <<<", 0.01)
    play_sfx("boss")
    pause(1)

    animate_text("'The T-1000 attacks!'", 0.02)
    play_sfx("hit")
    pause(2)

    # Combat System (Mini-Boss)
    win, new_hp = start_combat(
        player_state["hp"],
        "T-1000 Reformed",
        110,
        12,
        16,
        is_boss=True,
        player_damage=player_state["damage"]
    )

    player_state["hp"] = new_hp

    # After Combat
    if win:

        animate_text("The T-1000 suddenly stops attacking.")
        pause(1)

        animate_text("Its body melts into liquid metal.")
        play_sfx("warning")
        pause(1)

        animate_text("The machine retreats into the darkness.")
        pause(1)

        animate_text("Sarah Connor: Why did it leave?")
        animate_text("T-800: Probability of defeat increased.")
        animate_text("T-800: It will return.")
        pause(1)

        animate_text("Kyle Reese: I’ve done what I needed to do here.")
        pause(1)

        animate_text("Kyle Reese looks toward the horizon.")
        animate_text("Kyle Reese: I can’t stay in this timeline any longer.")
        pause(1)

        animate_text("Kyle Reese: John… Sarah… you’re safe with him now.")
        pause(1)

        animate_text("Kyle Reese steps back into the damaged alleyway.")
        animate_text("His presence fades into the shifting timeline.")
        pause(1)

        animate_text("SYSTEM: Kyle Reese has exited the active timeline.")
        pause(1)

        player_state["coins"] += 110
        player_state["xp"] += 100
        player_state = check_level_up(player_state)

        animate_text("MISSION COMPLETE: LEVEL 6")

    else:

        animate_text("The T-1000 stands over the battlefield.")
        play_sfx("warning")
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