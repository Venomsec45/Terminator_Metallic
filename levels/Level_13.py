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


def level13_dialogue_1():
    animate_text("Cold wind blows through the cemetery.")
    animate_text("Thunder rumbles in the distance.")

    animate_text("You: Why would the Resistance hide weapons in a cemetery?")
    animate_text("Kara: Because nobody comes here anymore.")
    animate_text("Kara: Even machines avoid places that remind humans of death.")

    animate_text("Metal cemetery gates slowly creak open.")
    pause(1)

    animate_text("You: This place gives me bad feelings.")
    animate_text("Kara: Good. That means your instincts still work.")

    animate_text("Footsteps crunch on wet gravel.")
    pause(1)

    animate_text("System: Low visibility detected.")

    animate_text("You: I can barely see anything.")
    animate_text("Kara: Stay close.")

    animate_text("Lightning briefly illuminates rows of broken tombstones.")
    pause(1)

    animate_text("You: How big is this place?")
    animate_text("Kara: Bigger than it looks.")

    animate_text("A distant metallic sound echoes.")
    pause(1)

    animate_text("You: Tell me that was the wind.")
    animate_text("Kara: That wasn't the wind.")

    animate_text("System: Motion detected nearby.")

    animate_text("You: Great.")

    animate_text("A damaged Scout drone rises from behind a tombstone.")
    pause(1)

    animate_text("Scout drone: Target located.")

    animate_text("You: Contact!")
    # Fighting part

def level13_dialogue_2():
    animate_text("Kara: Nice shot.")
    animate_text("You: Lucky shot.")

    animate_text("More red lights appear deeper in the cemetery.")
    pause(1)

    animate_text("You: Please tell me those are not eyes.")
    animate_text("Kara: Run.")

    animate_text("Several Spider crawlers rush across tombstones.")

    animate_text("You: WHY ARE THERE SPIDER ROBOTS?!")
    animate_text("Kara: Less screaming. More shooting!")

    animate_text("Rapid gunfire echoes through the graveyard.")
    pause(1)

    animate_text("Spider crawler: Target surrounded.")

    animate_text("You: I officially hate this place!")

def level13_dialogue_3():
    animate_text("Heavy rain begins pouring.")
    pause(1)

    animate_text("System: Storm intensity increasing.")

    animate_text("You: Perfect timing.")
    animate_text("Lightning reveals a ruined chapel ahead.")
    pause(1)    

    animate_text("Kara: There.")
    animate_text("You: The weapon cache is inside?")
    animate_text("Kara: Underground bunker beneath it.")

    animate_text("Large metal doors suddenly open nearby.")
    pause(1)

    animate_text("System: Warning. Heavy unit detected.")

    animate_text("You: Define heavy.")
    animate_text("A Heavy terminator steps from the shadows.")
    pause(1)

    animate_text("Heavy terminator: Resistance members identified.")
    animate_text("You: That's heavy enough!")

    animate_text("The Terminator fires plasma rounds.")
    pause(1)
    
    animate_text("Kara: TAKE COVER!")
    
    animate_text("Explosions destroy nearby tombstones.")
    pause(1)

    animate_text("You: This thing is insane!")
    animate_text("Kara: Aim for the joints!")

    animate_text("You fires repeatedly.")
    pause(1)

    animate_text("Heavy terminator: Damage insignificant.")
    pause(1)

    animate_text("You: Why do robots always say dramatic things?!")
    animate_text("Heavy terminator punches through a stone wall.")
    animate_text("You: OKAY THAT'S TERRIFYING!")
    animate_text("Kara: Fall back to the chapel!")
    
    animate_text("The two rush inside the ruined chapel.")
    animate_text("Old wooden floor creaks loudly.")
    pause(1)
    
    animate_text("You: This place looks ready to collapse.")
    animate_text("Kara: Hopefully after we leave.")

    animate_text("The Heavy terminator slowly approaches outside.")
    pause(1)

    animate_text("THUMP.")
    animate_text("THUMP.")
    animate_text("THUMP.")

    animate_text("You: It's still coming.")
    animate_text("Kara: Help me move this altar.")
    animate_text("You: Wait... the bunker entrance is under the altar?")
    animate_text("Kara: Exactly.")

    animate_text("Both push the heavy altar aside.")
    animate_text("Hidden metal hatch revealed.")
    pause(1)

    animate_text("You: Nice.")
    animate_text("Kara: Open it!")

    animate_text("The hatch opens with rusty mechanical sounds.")
    pause(1)

    animate_text("System: Hidden facility detected.")
    animate_text("Heavy terminator begins breaking chapel entrance.")
    pause(1)

    animate_text("Heavy terminator: Escape attempt detected.")
    animate_text("You: MOVE MOVE MOVE!")

    animate_text("Both descend ladder into underground bunker.")
    animate_text("Hatch slams shut above them.")
    animate_text("[Silence]")
    pause(1)

    animate_text("You: ...Did we lose it?")
    animate_text("Kara: For now.")

    animate_text("Emergency lights flicker on underground.")
    animate_text("System: Resistance bunker online.")
    animate_text("You: Whoa...")
    animate_text("Rows of hidden weapons line the bunker walls.")
    animate_text("You: That's a lot of weapons.")
    animate_text("Kara: The Resistance prepared for war long before Judgment Day.")
    animate_text("You: Plasma rifles...")
    animate_text("You: EMP grenades...")
    animate_text("You: Military explosives...")
    animate_text("Kara: Take what you can carry.")
    animate_text("You picks up plasma rifle.")

    animate_text("System: New weapon acquired.")
    animate_text("You: This feels way better than my old gun.")
    animate_text("Kara: You'll need it.")

    animate_text("Old computer terminal suddenly activates.")

    animate_text("Unknown transmission: If anyone is hearing this...")
    animate_text("Unknown transmission: Skynet is preparing a mass activation event.")
    animate_text("Unknown transmission: Survivors must reach Sector Zero immediately.")

    animate_text("You: Sector Zero?")
    animate_text("Kara: That's impossible.")

    animate_text("You: What is it?")
    animate_text("Kara: The machine capital.")

    animate_text("You: ...That's where we're going next, isn't it?")

    animate_text("Kara: Probably.")

    animate_text("Loud explosion shakes bunker ceiling.")
    pause(1)

    animate_text("You: Please tell me that's not the Terminator.")
    animate_text("Kara: That's definitely the Terminator.")
    animate_text("System: Surface breach detected.")
    animate_text("You: It followed us?!")
    animate_text("Kara: Grab the explosives!")
    animate_text("Heavy footsteps echo above bunker.")
    pause(1)

    animate_text("Heavy terminator: Target persistence active.")
    animate_text("You: It literally does not stop!")
    animate_text("Kara: That's kind of their thing!")

    animate_text("You: Arms explosives.")

    animate_text("You: Ready!")
    animate_text("Kara: Set them near the support pillars!")

    animate_text("The bunker door begins bending inward.")
    pause(1)

    animate_text("You: It's coming through!")
    animate_text("Kara: FALL BACK!")

    animate_text("Heavy terminator enters bunker.")
    animate_text("Heavy terminator: Resistance termination imminent.")
    animate_text("You: You first!")
    animate_text("Massive firefight erupts.")
    animate_text("Sparks fly across bunker walls.")
    animate_text("System: Structural instability detected.")

    animate_text("Kara: Detonate the charges!")

    animate_text("You: NOW?!")
    animate_text("Kara: NOW!")

    animate_text("You presses detonator.")
    animate_text("Massive explosion tears through bunker.")
    animate_text("Heavy terminator buried under collapsing debris.")
    pause(1)

    animate_text("You: Did we finally destroy it?")
    animate_text("[Silence]")
    pause(1)

    animate_text("A damaged metal hand rises from rubble.")
    pause(1)

    animate_text("You: YOU HAVE GOT TO BE KIDDING ME!")
    animate_text("Kara: RUN!")

    animate_text("Both escape through emergency tunnel.")
    pause(1)

    animate_text("Tunnel lights flicker rapidly.")
    pause(1)

    animate_text("System: Emergency exit ahead.")
    animate_text("You: I see daylight!")

    animate_text("Both emerge outside far from cemetery.")
    animate_text("Rain slowly stops.")
    pause(1)

    animate_text("You: We actually survived.")
    animate_text("Kara: Barely.")

    animate_text("You: So what now?")
    animate_text("Kara: Now we take the fight to them.")

    animate_text("System: Level 13 Complete.")
    animate_text("System: New Objective Unlocked.")
    animate_text("System: Travel to Sector Zero.")

def level13(player_state):
    username = player_state["username"]

    level13_dialogue_1()

    animate_text("Level 13: Scout Encounter", 0.02)
    pause(1)

    win, new_hp = start_combat(
        player_state["hp"],
        "Scout Drone",
        50,
        8,
        5
    )

    player_state["hp"] = new_hp

    if win:
        animate_text("The Scout Drone collapses into burning scrap.")
        pause(1)

        player_state["coins"] += 25
        player_state["xp"] += 20 
        player_state = check_level_up(player_state)

    else:
        animate_text("MISSION FAILED")
        return player_state
    
    level13_dialogue_2()

    animate_text("Level 13: Spider crawler", 0.02)
    pause(1)

    win, new_hp = start_combat(
        player_state["hp"],
        "Spider crawler",
        85,
        7,
        2
    )

    player_state["hp"] = new_hp

    if win:
        animate_text("The Spider crawler was destroyed.")
        pause(1)

        player_state["coins"] += 25
        player_state["xp"] += 20 
        player_state = check_level_up(player_state)

    else:
        animate_text("MISSION FAILED")
        return player_state
    
    level13_dialogue_3()

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
