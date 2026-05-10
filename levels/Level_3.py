from combat_system import start_combat
from menu import post_level_menu
from player_levels import check_level_up
import time
import sys
import os


# Text animations
def animate_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def pause(seconds=1):
    time.sleep(seconds)


# Simple Sound effects
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


# Level 3 DIalogue
def level3_dialogue():

    animate_text("Rain pours heavily across the ruined city.")
    pause(1)

    animate_text("Broken streetlights flicker in the darkness.")
    pause(1)

    animate_text("Sarah Connor: We've been walking for hours...")
    animate_text("Sarah Connor: How much farther?")
    pause(1)

    animate_text("Kyle Reese: Not far.")
    animate_text("Kyle Reese: There's an abandoned resistance shelter nearby.")
    animate_text("Kyle Reese: If it still exists.")
    pause(1)

    animate_text("Sarah Connor: Resistance...")
    animate_text("Sarah Connor: You really fought a war against machines?")
    pause(1)

    animate_text("Kyle Reese: Since I was a child.")
    animate_text("Kyle Reese: Most people in my time never saw peace.")
    animate_text("Kyle Reese: We grew up underground.")
    pause(1)

    animate_text("Sarah Connor: Underground?")
    animate_text("Kyle Reese: The machines controlled the surface.")
    animate_text("Kyle Reese: Hunter killers patrolled the skies.")
    animate_text("Kyle Reese: T-600 units hunted survivors at night.")
    pause(1)

    animate_text("Sarah Connor: T-600?")
    pause(1)

    animate_text("Kyle Reese suddenly stops walking.")
    pause(1)

    animate_text("Heavy metallic footsteps echo nearby...")
    play_sfx("warning")
    pause(1)

    animate_text("THUD...")
    pause(1)

    animate_text("THUD...")
    pause(1)

    animate_text("Sarah Connor: Kyle...")
    animate_text("Sarah Connor: Tell me that's not one of them.")
    pause(1)

    animate_text("Kyle Reese slowly reloads his weapon.")
    animate_text("Kyle Reese: Stay behind me.")
    animate_text("Kyle Reese: And stay quiet.")
    pause(1)

    animate_text("A massive shadow moves through the fog.")
    play_sfx("alert")
    pause(1)

    animate_text("Sarah Connor: Oh my God...")
    animate_text("Sarah Connor: It's huge.")
    animate_text("Kyle Reese: T-600 infiltration unit.")
    animate_text("Kyle Reese: Old model.")
    animate_text("Kyle Reese: But still deadly.")
    pause(1)

    animate_text("The machine steps into the light.")
    pause(1)

    animate_text("Its damaged rubber skin hangs from exposed metal.")
    animate_text("Its glowing red eyes lock onto them.")
    play_sfx("warning")
    pause(1)

    animate_text("Sarah Connor: That thing looks human...")
    animate_text("Kyle Reese: From far away.")
    animate_text("Kyle Reese: That's how they fooled people before the newer models.")
    pause(1)

    animate_text("Sarah Connor: It's staring at us...")
    animate_text("Kyle Reese: It already identified us as targets.")
    pause(1)

    animate_text("The T-600 raises its weapon.")
    play_sfx("alert")
    pause(1)

    animate_text("Kyle Reese: MOVE!")
    play_sfx("explosion")
    pause(1)

    animate_text("Gunfire erupts through the street!")
    play_sfx("hit")
    pause(1)

    animate_text("Concrete explodes around them.")
    pause(1)

    animate_text("Sarah Connor: It's shooting at us!")
    animate_text("Kyle Reese: Get behind cover!")
    pause(1)

    animate_text("The T-600 slowly marches forward through the smoke.")
    play_sfx("warning")
    pause(1)

    animate_text("Sarah Connor: It just keeps coming!")
    animate_text("Kyle Reese: That's what they do.")
    animate_text("Kyle Reese: They don't fear anything.")
    pause(1)

    animate_text("The machine lets out a distorted mechanical growl.")
    play_sfx("alert")
    pause(1)

    animate_text("Sarah Connor: How do we stop that thing?!")
    animate_text("Kyle Reese: We hit it hard enough.")
    animate_text("Kyle Reese: Or we die trying.")
    pause(1)

    animate_text(">>> ENCOUNTER: T-600 UNIT <<<", 0.01)
    play_sfx("warning")
    pause(1)

    animate_text("'The T-600 attacks!'", 0.02)
    play_sfx("hit")
    pause(1)

    animate_text("The machine charges directly toward them!")
    pause(1)

    animate_text("Sarah Connor: Kyle!")
    animate_text("Kyle Reese: RUN!")
    play_sfx("explosion")
    pause(1)

    animate_text("The T-600 smashes through a concrete wall.")
    pause(1)

    animate_text("Sarah Connor: Nothing should survive that!")
    animate_text("Kyle Reese: Machines aren't supposed to survive.")
    animate_text("Kyle Reese: But they do.")
    pause(1)

    animate_text("Kyle grips his weapon tighter.")
    animate_text("Rain drips from the barrel.")
    pause(1)

    animate_text("Kyle Reese: If this thing kills us...")
    animate_text("Kyle Reese: The future changes forever.")
    pause(2)


# Level 3 Combat
def level3(player_state):
    username = player_state["username"]

    level3_dialogue()

    animate_text("Level 3: T-600 Unit", 0.02)
    pause(1)

    # Combat System
    win, new_hp = start_combat(
        player_state["hp"],
        "T-600",
        50,
        8,
        12
    )

    player_state["hp"] = new_hp

    # After Combat
    if win:

        animate_text("The T-600 stumbles backward.")
        pause(1)

        animate_text("Its red eyes flicker violently.")
        play_sfx("warning")
        pause(1)

        animate_text("The massive machine collapses into the street.")
        play_sfx("explosion")
        pause(1)

        animate_text("Sarah Connor: We actually destroyed it...")
        animate_text("Sarah Connor: That thing felt unstoppable.")
        pause(1)

        animate_text(f"Kyle Reese: Nice shooting, {username}.")
        animate_text("Kyle Reese: But the newer models are even worse.")
        pause(1)

        animate_text("Sarah Connor: Worse than THAT?!")
        animate_text("Kyle Reese: Much worse.")
        pause(1)

        animate_text("Lightning flashes across the sky.")
        pause(1)

        animate_text("Kyle Reese: Come on.")
        animate_text("Kyle Reese: We can't stay here.")
        animate_text("Kyle Reese: The gunfire will attract more patrols.")
        pause(1)

        player_state["coins"] += 65
        player_state["xp"] += 50
        player_state = check_level_up(player_state)

        animate_text("MISSION COMPLETE: LEVEL 3")

    else:

        animate_text("The T-600 towers over the battlefield.")
        pause(1)

        animate_text("Kyle Reese falls to the ground.")
        animate_text("Sarah Connor: Kyle!")
        pause(1)

        animate_text("The machine slowly advances through the smoke.")
        play_sfx("warning")
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