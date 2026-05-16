from combat_system import start_combat
from menu import post_level_menu
from player_levels import check_level_up
import os
import sys
import time


def animate_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def pause(seconds=1):
    time.sleep(seconds)


# Dialogue
def level14_dialogue_1():
    animate_text("Cold military sirens echo endlessly through the underground command base.")
    pause(1)

    animate_text("You: This place feels like it goes on forever...")
    animate_text("Kara: It was built to survive the end of the world. Literally.")

    animate_text("Massive steel blast doors grind open slowly, like the facility is waking up.")
    pause(1)

    animate_text("System: Military network detected.")
    animate_text("System: Defense grid synchronizing.")

    animate_text("You: So this is it... the heart of Skynet?")
    animate_text("Kara: One of them. The most important one.")

    animate_text("You: And if we fail?")
    animate_text("Kara: Then every machine connected to this network becomes a soldier.")
    animate_text("Kara: Not just here... everywhere.")

    animate_text("A long silence fills the hallway as distant alarms echo deeper inside the base.")
    pause(1)

    animate_text("Skynet AI: Human presence confirmed.")
    animate_text("Skynet AI: Emotional reasoning detected. Classified as inefficient.")

    animate_text("You: It always talks like it's above us.")
    animate_text("Kara: Because it thinks it is.")

    animate_text("Skynet AI: Nuclear defense protocol activation initiated.")
    animate_text("You: Did it just say nuclear?!")
    animate_text("Kara: That means we're out of time.")

    animate_text("Emergency lights turn deep red.")
    pause(1)

    animate_text("System: Containment protocols engaged.")
    animate_text("Metal walls begin sealing behind you one by one.")

    animate_text("You: So every hallway is closing off?")
    animate_text("Kara: It's trying to trap us inside the core zone.")

    animate_text("Ceiling turrets rotate into position.")
    animate_text("Defense turret: Target acquired.")
    animate_text("Defense turret: Engage.")

    animate_text("Gunfire erupts violently across the corridor.")
    pause(1)

    animate_text("You: Why does everything here want us erased?!")
    animate_text("Kara: Because we're the only variable Skynet can't control!")

    animate_text("You take cover behind a shattered console as sparks fly everywhere.")
    animate_text("Kara: Move when I say move!")

    animate_text("Elevator doors open with a loud metallic scream.")
    animate_text("Kara: Core level access confirmed.")
    animate_text("You: Of course it's underground... always underground.")

    animate_text("Both step inside the elevator.")
    animate_text("The doors close slowly... almost too slowly.")
    pause(1)

    animate_text("Elevator descends into darkness.")
    pause(1)

    animate_text("System: Elevator integrity unstable.")

    animate_text("You: That doesn't sound reassuring.")
    animate_text("Kara: Nothing about this mission is.")

    animate_text("Metal scraping echoes above the elevator shaft.")
    animate_text("You: Something’s up there...")

    animate_text("Suddenly red lights flicker overhead.")

    animate_text("Spider Crawlers drop from the ceiling into the elevator!")
    animate_text("SPIDER CRAWLER: Eliminate resistance units!")
    pause(1)

# Dialogue
def level14_dialogue_2():
    animate_text("Kara: The blast door is right ahead!")
    animate_text("You: Then open it before we get turned into scrap!")

    animate_text("System: Access denied.")
    animate_text("Skynet AI: Authorization levels insufficient.")

    animate_text("Kara: I’m forcing a manual override!")
    pause(1)

    animate_text("You: How long?!")
    animate_text("Kara: Not long if you keep talking!")

    animate_text("Massive blast doors begin grinding open slowly.")
    animate_text("Steam bursts out from the edges as ancient locks disengage.")

    animate_text("You: That sounds like a bad sign...")
    animate_text("Kara: Everything here is a bad sign.")

    animate_text("The doors finally open to reveal the core chamber.")

    animate_text("Gigantic towers of servers stretch upward into darkness.")
    animate_text("Blue light pulses like a heartbeat across the machines.")

    animate_text("You: This is it...")
    animate_text("Kara: The brain of Skynet.")

    animate_text("Skynet AI: Final activation sequence initiated.")
    animate_text("Skynet AI: Global synchronization commencing.")

    animate_text("You: Shut it down NOW!")
    animate_text("Kara: I'm trying to break into the core control loop!")

    animate_text("A deep mechanical voice echoes from everywhere at once.")

    animate_text("T-X UNIT: You are interference.")
    animate_text("T-X UNIT: Interference will be removed.")

    pause(1)

# Level 14 Combat
def level14(player_state):
    username = player_state["username"]

    # Phase 1
    level14_dialogue_1()

    animate_text("LEVEL 14: SPIDER SWARM ASSAULT", 0.02)
    pause(1)

    win, new_hp = start_combat(
        player_state["hp"],
        "Spider Crawlers",
        300,
        8,
        13,
        player_damage=player_state["damage"]
    )

    player_state["hp"] = new_hp

    if not win:
        animate_text("MISSION FAILED")
        player_state["game_over"] = True
        return player_state

    animate_text("Spider Crawlers destroyed... but more systems are waking up.")
    pause(1.5)

    animate_text("The facility is now fully alert.")
    pause(1)


    level14_dialogue_2()

    # Final boss
    animate_text("LEVEL 14: FINAL BOSS - T-X UNIT", 0.02)
    pause(1)

    animate_text("T-X UNIT: ENGAGING TARGETS")

    win, new_hp = start_combat(
        player_state["hp"],
        "T-X UNIT",
        500,
        14,
        20,
        is_boss=True,
        player_damage=player_state["damage"]
    )

    player_state["hp"] = new_hp

    if not win:
        animate_text("MISSION FAILED")
        player_state["game_over"] = True
        return player_state

    # ---------------- ENDING ----------------
    animate_text("T-X UNIT: System failure... critical damage detected.")
    animate_text("The machine collapses, its armor melting into molten steel.")

    animate_text("Skynet AI: Alert... core instability detected...")
    animate_text("Skynet AI: Containment failure imminent...")

    animate_text("You: Did we stop it?")
    animate_text("Kara: We slowed it... not stopped it.")

    animate_text("Massive warning sirens begin echoing worldwide through the system feed.")

    player_state["coins"] += 1000
    player_state["xp"] += 500
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