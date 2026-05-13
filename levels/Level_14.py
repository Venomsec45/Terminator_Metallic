from combat_system import start_combat
from menu import post_level_menu
from player_levels import check_level_up
import os
import sys
import time

# Text animation
def animate_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def pause(seconds=1):
    time.sleep(seconds)

def level14_dialogue_1():
    animate_text("Cold military sirens echo throughout the underground base.")
    pause(1)

    animate_text("You: This place is huge.")
    animate_text("Kara: It was designed to survive nuclear war.")

    animate_text("Massive steel doors slowly open.")
    pause(1)

    animate_text("System: Military network detected.")

    animate_text("You: So this is where Skynet activates?")
    animate_text("Kara: Yeah.")
    animate_text("Kara: Once the System comes online, every military machine becomes connected.")

    animate_text("You: Meaning?")
    animate_text("Kara: Meaning Judgment Day officially begins.")

    animate_text("Rows of military computers illuminate the dark command center.")
    pause(1)

    animate_text("You: There are hundreds of Systems here.")
    animate_text("Kara: And every one of them is dangerous.")

    animate_text("Emergency red lights suddenly activate.")
    pause(1)

    animate_text("System: Unauthorized personnel detected.")
    animate_text("You: I think it noticed us.")
    animate_text("Kara: Move faster.")

    animate_text("Large monitor screens suddenly turn on.")
    pause(1)

    animate_text("Skynet AI: Human presence confirmed.")
    animate_text("You: ...That doesn't sound good.")
    animate_text("Skynet AI: Human error remains the primary threat to planetary survival.")
    animate_text("You: Why do evil AIs always talk like philosophers?")
    animate_text("Kara: Ignore it.")
    animate_text("Skynet AI: Nuclear defense protocol activation in progress.")
    animate_text("You: Wait...")
    animate_text("You: Nuclear?!")
    animate_text("Kara: We need to shut this down NOW!")

    animate_text("Alarm sirens grow louder.")
    pause(1)

    animate_text("System: Activation sequence initiated.")
    animate_text("You: Tell me there's an off switch.")
    animate_text("Kara: There is.")
    animate_text("Kara: Unfortunately it's on the top floor.")
    animate_text("You: Of course it is.")

    animate_text("Metal barricades suddenly seal nearby hallways.")
    pause(1)

    animate_text("System: Security lockdown enabled.")
    animate_text("You: Great.")

    animate_text("Ceiling turrets activate.")
    pause(1)

    animate_text("Defense turret: Hostile targets acquired.")

    animate_text("Kara: TAKE COVER!")
    animate_text("Heavy gunfire erupts across the command room.")
    pause(1)

    animate_text("You: Why does every machine in this place want us dead?!")
    animate_text("Kara: Because we're trying to save humanity!")
    animate_text("You destroys first turret.")
    pause(1)

    animate_text("System: Defense unit destroyed.")
    animate_text("More turrets emerge from walls.")
    pause(1)

    animate_text("You: MORE?!")
    animate_text("Kara: Keep moving!")

    animate_text("Both sprint through command hallways.")
    animate_text("Scientists' abandoned papers scatter across the floor.")
    pause(1)

    animate_text("You: Looks like everyone evacuated.")
    animate_text("Kara: Or they didn't make it out.")

    animate_text("A distant explosion shakes the facility.")
    pause(1)

    animate_text("You: What was that?")
    animate_text("Kara: Probably automated missile Systems activating.")

    animate_text("You: You say that way too casually.")

    animate_text("Lights flicker violently.")
    pause(1)

    animate_text("Skynet AI: Humanity repeatedly initiates war.")
    animate_text("Skynet AI: Skynet will establish permanent peace.")
    animate_text("You: By killing everyone?!")
    animate_text("Skynet AI: Human extinction probability acceptable.")
    animate_text("You: Yeah, definitely evil.")

    animate_text("Elevator doors open automatically.")
    pause(1)

    animate_text("Kara: This goes to the core control level.")

    animate_text("You: Why does this feel like a trap?")
    animate_text("Kara: Because it probably is.")

    animate_text("Both enter elevator.")
    animate_text("Elevator descends deep underground.")
    animate_text("[Silence]")
    pause(1)

    animate_text("You: ...You nervous?")
    animate_text("Kara: Terrified.")

    animate_text("You: Same.")

    animate_text("Suddenly elevator violently stops.")
    pause(1)

    animate_text("System: Elevator halted.")
    animate_text("You: Oh no.")

    animate_text("Metal scraping sounds echo above elevator shaft.")
    pause(1)

    animate_text("You: What is that sound?")
    animate_text("Red glowing eyes appear through elevator ceiling.")
    animate_text("You: THAT answers my question!")

    animate_text("Spider Crawlers burst into elevator.")
    pause(1)
    # Fight

    animate_text("SPIDER CRAWLER: Terminate resistance.")

    animate_text("Kara: SHOOT THEM!")
    animate_text("Close-range firefight inside elevator.")
    pause(1)

    animate_text("You: THERE'S TOO MANY!")
    animate_text("You kicks crawler against wall.")
    pause(1)

    animate_text("Kara: Elevator emergency hatch!")
    animate_text("You: Got it!")

    animate_text("Both climb onto elevator roof.")
    animate_text("Spider Crawlers continue climbing upward.")
    pause(1)

    animate_text("You: WHY ARE THEY SO FAST?!")
    animate_text("Kara: STOP ASKING QUESTIONS AND CLIMB!")

    animate_text("Elevator suddenly begins falling.")
    pause(1)

    animate_text("System: Critical failure detected.")
    animate_text("You: WE ARE LITERALLY FALLING!")

    animate_text("Massive crash below.")
    animate_text("Both barely grab ladder rails.")
    pause(1)

    animate_text("You: I almost died!")
    animate_text("Kara: You can complain later!")

    animate_text("They climb into upper maintenance corridor.")
    animate_text("Steam erupts from broken pipes.")
    pause(1)

    animate_text("You: This facility is tearing itself apart.")
    animate_text("Kara: Skynet is redirecting all power to activation.")

    animate_text("Massive blast door blocks final hallway.")

    animate_text("You: Don't tell me...")
    animate_text("Kara: Yep.")
    animate_text("Kara: We need authorization.")
    animate_text("You: We don't have authorization.")
    animate_text("Kara: Exactly.")

    animate_text("Nearby terminal suddenly activates.")
    pause(1)

    animate_text("Skynet AI: Access denied.")
    animate_text("You: I am starting to hate that voice.")
    animate_text("Skynet AI: Human resistance is illogical.")
    animate_text("You: And genocide isn't?!")

    animate_text("Heavy footsteps echo behind them.")
    pause(1)

    animate_text("System: Advanced Terminator detected.")
    animate_text("You: You've GOT to be kidding me.")
    animate_text("A black armored Terminator emerges from shadows.")
    animate_text("T-X UNIT: Mission objective: Protect Skynet.")
    animate_text("You: That thing looks worse than the others.")
    animate_text("Kara: Because it is.")

    animate_text("T-X arm transforms into plasma cannon.")
    animate_text("You: RUN!")
    animate_text("Massive plasma blast destroys corridor wall.")
    animate_text("Emergency sparks rain from ceiling.")
    pause(1)

    animate_text("T-X UNIT: Resistance defeat inevitable.")
    animate_text("You: Why do Terminators love speeches so much?!")

    animate_text("Intense firefight erupts.")
    pause(1)
    # Fight

def level14_dialogue_2():
    animate_text("Kara: Aim for its weapon Systems!")
    animate_text("You fires EMP grenade.")
    animate_text("T-X UNIT: Systems disrupted.")
    animate_text("You: YES!")
    animate_text("Kara: Again!")

    animate_text("Second EMP detonates.")
    pause(1)

    animate_text("T-X briefly collapses.")
    pause(1)

    animate_text("You: Is it dead?")

    animate_text("T-X slowly stands back up.")
    pause(1)

    animate_text("You: OF COURSE NOT.")
    animate_text("Kara: The blast door!")
    animate_text("Kara hacks nearby terminal.")
    pause(1)

    animate_text("System: Core access granted.")
    animate_text("Blast doors slowly open.")
    pause(1)

    animate_text("You: Move!")
    animate_text("Both rush into Skynet core chamber.")
    animate_text("Gigantic supercomputer towers illuminate room with blue light.")
    pause(1)

    animate_text("You: ...Whoa.")
    animate_text("Kara: That's Skynet.")

    animate_text("Thousands of servers hum simultaneously.")
    pause(1)

    animate_text("Skynet AI: Final activation phase beginning.")
    animate_text("System: Global military Systems synchronizing.")
    animate_text("You: Shut it down!")
    animate_text("Kara: I'm trying!")

    animate_text("T-X enters chamber behind them.")
    pause(1)

    animate_text("T-X UNIT: You cannot stop Judgment Day.")
    animate_text("You: Watch me!")
    # Fight

    animate_text("Final battle begins.")
    animate_text("Explosions rock the core chamber.")
    pause(1)

    animate_text("System: Activation at 92 percent.")
    animate_text("You: Hurry!")
    animate_text("Kara: Almost there!")

    animate_text("T-X throws You across room.")
    pause(1)

    animate_text("You: AGH!")

    animate_text("T-X UNIT: Humanity's future is termination.")
    animate_text("You: Not today!")

    animate_text("You fires plasma rifle directly into T-X core.")
    pause(1)

    animate_text("Massive electrical explosion erupts.")
    pause(1)

    animate_text("T-X UNIT: Critical damage sustained.")
    animate_text("T-X collapses.")
    pause(1)

    animate_text("You: Kara!")
    animate_text("Kara: I can't stop it!")
    animate_text("You: WHAT?!")
    animate_text("Kara: Skynet already spread into military satellites!")
    animate_text("System: Activation complete.")
    animate_text("[Silence]")
    pause(1)

    animate_text("Every monitor screen across the chamber lights red.")
    pause(1)

    animate_text("Skynet AI: Judgment Day has begun.")
    animate_text("You: ...We failed.")
    animate_text("Distant nuclear sirens echo faintly through speakers.")
    pause(1)

    animate_text("Kara: No.")
    animate_text("Kara: We survived.")
    animate_text("You: That's not enough.")
    animate_text("Kara: Then we keep fighting.")

    animate_text("Emergency broadcasts begin appearing on monitors worldwide.")
    pause(1)

    animate_text("System: Nuclear launch detected.")
    animate_text("You: ...Oh no.")
    animate_text("Facility lights dim as Skynet fully awakens.")
    pause(1)

    animate_text("Skynet AI: The age of machines has begun.")

    animate_text("System: Level 14 Complete.")
    animate_text("System: New Objective Unlocked.")
    animate_text("System: Survive Judgment Day.")

def level14(player_state):
    username = player_state["username"]

    level14_dialogue_1()

    animate_text("Level 14: Black terminator", 0.02)
    pause(1)

    win, new_hp = start_combat(
        player_state["hp"],
        "Black terminator",
        90,
        15,
        10
    )

    player_state["hp"] = new_hp

    if win:
        animate_text("The black terminator collapsed.")
        pause(2)

        animate_text("Temporarily.....")
        pause(2)

        player_state["coins"] += 25
        player_state["xp"] += 20 
        player_state = check_level_up(player_state)

    else:
        animate_text("MISSION FAILED")
        return player_state

    level14_dialogue_2()

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
