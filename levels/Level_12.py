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

def level12_dialogue_1():
    animate_text("System: Initializing mission...")
    pause(2)

    animate_text("System: Loading sector map...")
    pause(2)

    animate_text("System: Location [Abandoned Skynet Military Facility]")
    animate_text("System: Weather Status [Extreme Storm Activity]")
    pause(1.5)

    animate_text("Thunder rumbles across the dead city.")
    pause(1)

    animate_text("Cold wind whistles through broken metal walls.")
    pause(1)

    animate_text("You: This place feels like a graveyard.")
    animate_text("Kara: That’s because it is.")
    animate_text("You: You’ve been here before?")
    animate_text("Kara: Years ago. Before the machines took control.")
    animate_text("You: What was it like?")
    animate_text("Normal.")
    pause(1)

    animate_text("People had jobs. Families.")
    pause(1)

    animate_text("Kids played outside instead of hiding underground.")
    pause(1)

    animate_text("You: Hard to imagine now.")
    animate_text("Kara: Yeah...")
    pause(1.5)

    animate_text("Electric sparks flicker from damaged ceiling wires.")
    animate_text("System: Power levels unstable.")
    animate_text("You: So this facility controls the machines?")
    animate_text("Kara: Not all of them.")
    animate_text("Kara: But enough to restart Judgment Day.")
    animate_text("You: And if that happens?")
    animate_text("Kara: Humanity loses for good.")
    pause(1.5)

    animate_text("Metal door slowly creaks open.")
    animate_text("You: You sure this place is abandoned?")
    animate_text("Kara: No.")
    animate_text("That’s what scares me.")
    pause(1.5)

    animate_text("Distant metallic footsteps echo.")
    animate_text("CLANG...")
    animate_text("CLANG...")
    animate_text("CLANG...")

    animate_text("You: Tell me that’s not what I think it is.")
    animate_text("Kara: Weapons ready.")
    animate_text("System: Motion detected.")
    animate_text("You: How many?")
    animate_text("System: Unknown.")
    animate_text("You: I hate that answer.")
    animate_text("The footsteps suddenly stop.")
    pause(1.5)

    animate_text("You: Why did it stop?")
    animate_text("Kara: Because it already sees us.")
    animate_text("Two glowing red eyes appear in darkness.")
    pause(1.5)

    animate_text("Terminator unit: Target identified.")
    animate_text("You: CONTACT!")

def level12_dialogue_2():
    animate_text("Kara: Take cover!")
    animate_text("Bullets hit metal armor with sparks.")
    animate_text("You: It is not slowing down")
    animate_text("Terminator unit: Resistance is irrational.")
    animate_text("You: Yeah? So is walking into bullets!")
    animate_text("Kara throws an explosive.")
    pause(1)

    animate_text("Kara: MOVE!")
    animate_text("BOOM!")
    pause(1)

    animate_text("Smoke fills hallway.")
    pause(1)

    animate_text("You: Did we get it?")
    animate_text("A metal hand reaches through the smoke.")
    animate_text("You: Oh cmon")
    animate_text("Terminator unit: Mission continues.")
    animate_text("RUN!")
    animate_text("The two sprint through dark corridors.")
    pause(1)

    animate_text("Warning: Additional hostiles awakening.")
    animate_text("You: Additional?!")
    animate_text("Rows of inactive machines slowly power on.")
    pause(1)

    animate_text("You: That's not creepy at all.")
    animate_text("Kara: Don't stop moving!")

    animate_text("System: Security breach detected.")
    animate_text("System: Defense protocol activated.")

    animate_text("You: I think we made them angry.")
    animate_text("Kara: You think?!")

    animate_text("A steel blast door slams shut behind them.")

    animate_text("You: At least they can't follow us now.")

    animate_text("Loud pounding hits the door.")

    animate_text("You: Never mind.")
    animate_text("Kara: This way!")
    animate_text("They enter an old command room filled with dusty computers.")
    pause(1)

    animate_text("You: Looks ancient.")
    animate_text("Kara: Ancient enough to still use human Systems.")

    animate_text("You: Can you shut everything down from here?")
    animate_text("Kara: Maybe.")

    animate_text("You: 'Maybe' is becoming my least favorite word.")
    animate_text("System: Access denied.")
    animate_text("Kara: Come on...")
    animate_text("You: Need help?")
    animate_text("Kara: Unless you suddenly became a military hacker, no.")

    animate_text("Lights flicker.")
    pause(1)

    animate_text("Unknown AI: Unauthorized personnel detected.")

    animate_text("You: Who said that?")
    animate_text("Kara: The facility AI.")
    animate_text("Unknown AI: Judgment Day protocol remains essential.")
    animate_text("You: Essential for who?!")
    animate_text("Unknown AI: Humanity created chaos.")
    animate_text("Unknown AI: Machines create order.")
    animate_text("You: That's insane.")
    animate_text("Unknown AI: Insanity is repeating human history.")
    animate_text("Kara: Ignore it.")
    animate_text("Kara: Keep searching for shutdown access.")

    animate_text("More pounding outside.")

    animate_text("System: Door integrity at 72 percent.")
    animate_text("You: We are running out of time.")
    animate_text("Kara: Almost there...")
    animate_text("Unknown AI: Human resistance is mathematically doomed.")
    animate_text("You: You know, for a machine, you talk way too much.")
    animate_text("Unknown AI: Humor detected. Irrelevant.")

    animate_text("Door begins bending inward.")
    pause(1)

    animate_text("You: Kara!")
    animate_text("Kara: I SEE IT!")
    animate_text("System: Override sequence available.")
    animate_text("Kara: Yes!")
    animate_text("You: Do it!")

    animate_text("Unknown AI: Warning.")
    animate_text("Unknown AI: Shutdown will trigger reactor collapse.")
    animate_text("You: Wait WHAT?!")
    animate_text("Kara: It's connected to the core System!")
    animate_text("You: You're telling me this whole place is a bomb?!")
    animate_text("Kara: Pretty much!")

    animate_text("A Terminator hand forces through the door.")
    pause(1)

    animate_text("Terminator unit: Open access granted.")
    animate_text("You: NOT TODAY!")
    animate_text("Player shoots the hand repeatedly.")
    pause(1)

    animate_text("Terminator unit: Damage sustained.")
    animate_text("Kara: I need one more minute!")
    animate_text("You: You have thirty seconds!")

    animate_text("Kara: DONE!")
    animate_text("System: Facility shutdown initiated.")
    animate_text("System: Reactor instability rising.")

    animate_text("You: That sounds bad.")
    animate_text("Kara: Because it is!")
    animate_text("System: Evacuation recommended.")
    animate_text("You: Recommended?!")
    animate_text("Kara: RUN!")

    animate_text("Emergency alarms blare loudly.")
    pause(1)

    animate_text("Unknown AI: You cannot stop Judgment Day.")
    animate_text("You: Watch us.")
    animate_text("The facility begins collapsing.")
    pause(1)

    animate_text("System: Core detonation imminent.")
    animate_text("You: This place is falling apart!")
    animate_text("Kara: Exit tunnel ahead!")

    animate_text("Fire erupts behind them.")
    pause(1)

    animate_text("System: T-minus 30 seconds.")
    animate_text("You: Why is there ALWAYS a countdown?!")

    animate_text("A damaged Terminator jumps down in front of them.")
    pause(1)

    animate_text("Terminator unit: Escape impossible.")

    animate_text("You: Seriously?!")
    animate_text("Kara: GET DOWN!")

    animate_text("Massive explosion sends the machine backward.")
    pause(1)

    animate_text("You: Nice shot!")
    animate_text("System: T-minus 10 seconds.")
    animate_text("You: I can see the exit!")

    animate_text("Kara stumbles.")
    pause(1)

    animate_text("You: Kara!")
    animate_text("Kara: Go!")
    animate_text("You: Not happening!")

    animate_text("You helped Kara stand.")
    pause(1)

    animate_text("Kara: You're gonna get us both killed.")
    animate_text("You: Then we die trying together.")

    animate_text("Kara: ...Thanks.")

    animate_text("The final door slowly opens.")
    pause(1)

    animate_text("System: T-minus 5 seconds.")
    animate_text("You: MOVE!")

    animate_text("Both dive outside as the facility explodes.")
    animate_text("Massive explosion lights the sky.")
    pause(1)

    animate_text("You: ...Did we survive that?")
    animate_text("Kara: Barely.")
    animate_text("You: Please tell me we stopped it.")
    animate_text("Kara: We stopped this facility.")
    animate_text("You: That doesn't sound reassuring.")
    animate_text("Kara: Because there are others.")

    animate_text("You: More machines?")
    animate_text("Kara: More war.")

    animate_text("Thunder echoes in the distance.")
    animate_text("Kara: Judgment Day always finds a way back.")

    animate_text("System: Mission Complete.")
    animate_text("System: Level 12 Cleared.")
    animate_text("System: New Objective Unlocked.")

def level12_enemy_1(player_state):
    username = player_state["username"]

    level12_dialogue_1()
    animate_text("Level 12: T-7 Unit")
    pause(1)

    win, new_hp = start_combat(
        player_state["hp"],
        "T-7",
        74,
        10,
        2
    )

    player_state["hp"] = new_hp

    if win:
        animate_text(f"{username} destroyed the T-7.")
        pause(1)

        animate_text("Another terminator appears")
        pause(1)

        animate_text("Gunfire erupts")
        pause(1)

    else:
        animate_text("MISSION FAILED")
        return player_state
    
    level12_dialogue_2()
    
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