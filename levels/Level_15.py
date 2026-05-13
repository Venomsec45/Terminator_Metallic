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

def level15_dialogue():
    animate_text("System: Loading Level 15...")
    animate_text("System: Location: Crystal Peak Fallout Shelter")
    animate_text("System: Objective: Survive Judgment Day")

    animate_text("Emergency sirens echo throughout the underground bunker.")
    pause(1)

    animate_text("You: The doors sealed behind us.")
    animate_text("Kara: Then this is it.")
    animate_text("Massive steel blast doors lock with a thunderous impact.")
    pause(1)

    animate_text("System: Fallout shelter secured.")

    animate_text("You: Tell me we have a plan.")
    animate_text("Kara: Survival.")
    animate_text("You: That's not much of a plan.")

    animate_text("The entire bunker shakes violently.")
    pause(1)

    animate_text("System: Nuclear launch confirmed.")

    animate_text("You: ...It's happening.")
    animate_text("Kara: Judgment Day.")

    animate_text("Emergency red lights flood the shelter.")
    pause(1)

    animate_text("You: There has to be a way to stop the missiles.")
    animate_text("Kara: We were too late.")
    animate_text("Old military radios suddenly activate.")
    pause(1)

    animate_text("Radio operator: This is Northern Command!")
    animate_text("Radio operator: Multiple nuclear impacts confirmed!")
    animate_text("Static fills the radio.")
    pause(1)

    animate_text("You: Oh my god...")

    animate_text("Radio operator: Cities are gone!")
    animate_text("Radio operator: We need immediate assistance!")
    animate_text("Signal cuts out.")
    animate_text("[Silence]")
    pause(1)

    animate_text("You: ...How many people just died?")
    animate_text("Kara: Millions.")

    animate_text("Distant rumbling echoes deep underground.")
    pause(1)

    animate_text("System: Shockwave approaching.")
    animate_text("You: Shockwave?!")

    animate_text("The bunker violently trembles.")
    animate_text("Dust falls from the ceiling.")
    pause(1)

    animate_text("You: The whole mountain is shaking!")
    animate_text("Kara: Stay down!")

    animate_text("Massive explosion sound echoes from far above.")
    animate_text("[LONG SILENCE]")
    pause(1)

    animate_text("You: ...Is it over?")
    animate_text("Kara: No.")
    animate_text("Kara: That's only the beginning.")

    animate_text("Emergency backup generators activate.")
    pause(1)

    animate_text("System: Switching to internal power.")
    animate_text("Dim bunker lights flicker on.")
    pause(1)

    animate_text("You: This place feels like a tomb.")
    animate_text("Kara: It probably was designed to be one.")

    animate_text("You walks through abandoned military control room.")
    pause(1)

    animate_text("You: Look at this...")
    animate_text("You: They knew this could happen.")

    animate_text("Kara: Governments always prepare for the end.")
    animate_text("Kara: They just never thought they'd lose control.")
    animate_text("Old computer terminals suddenly activate automatically.")
    pause(1)

    animate_text("System: External satellite feeds available.")
    animate_text("You: Can we see the surface?")
    animate_text("Kara: ...You sure You want to?")
    animate_text("You: No.")
    animate_text("You: But I need to.")
    animate_text("Monitor screen slowly flickers on.")
    pause(1)

    animate_text("Burning cities appear across the screen.")
    pause(1)

    animate_text("Massive mushroom clouds rise into the sky.")
    animate_text("[Silence]")
    pause(1)

    animate_text("You: ...Everything's gone.")
    animate_text("Kara: Not everything.")
    animate_text("You: How can You even say that right now?!")
    animate_text("Kara: Because if humanity survives...")
    animate_text("Kara: Then this war isn't over.")

    animate_text("Emergency military transmission appears.")
    pause(1)

    animate_text("Automated voice: Attention all surviving personnel.")
    animate_text("Automated voice: Skynet has assumed control of military assets.")

    animate_text("You: It controls everything now.")
    animate_text("Automated voice: All remaining resistance forces regroup immediately.")

    animate_text("You: Resistance forces?")
    animate_text("Kara: That's how it starts.")

    animate_text("The bunker shakes again.")
    pause(1)

    animate_text("System: Surface radiation levels critical.")

    animate_text("You: So we're trapped down here.")
    animate_text("Kara: For now.")

    animate_text("You notices old photographs on bunker desk.")
    pause(1)

    animate_text("You: Families...")
    animate_text("You: They were living normal lives a few hours ago.")
    animate_text("Kara: That's the terrifying part.")
    animate_text("Kara: The world ended on an ordinary day.")

    animate_text("Static suddenly bursts from nearby radio.")
    pause(1)

    animate_text("Unknown survivor: Please respond!")
    animate_text("Unknown survivor: Anyone alive out there?!")

    animate_text("You: Someone survived!")
    animate_text("Kara: Answer them!")
    animate_text("You: This is Crystal Peak Shelter!")
    animate_text("You: We read You!")
    animate_text("Heavy static.")
    pause(1)

    animate_text("Unknown survivor: Machines...")
    animate_text("Unknown survivor: They're everywhere...")
    animate_text("Distant screaming heard through radio.")
    pause(1)

    animate_text("You: Hello?!")
    animate_text("Signal abruptly dies.")
    animate_text("[Silence]")
    pause(1)

    animate_text("You: ...We couldn't help them.")
    animate_text("Kara: Not yet.")

    animate_text("You punches nearby wall in frustration.")
    pause(1)

    animate_text("You: We failed!")
    animate_text("You: We had one job!")
    animate_text("Kara: Listen to me.")
    animate_text("Kara: This was never about stopping Judgment Day.")
    animate_text("You: Then what was the point?!")
    animate_text("Kara: Survival.")
    animate_text("Kara: Humanity survives long enough to fight back.")

    animate_text("Emergency map appears on bunker monitor.")
    pause(1)

    animate_text("System: Multiple survivor signals detected.")

    animate_text("You: There are more survivors?")
    animate_text("Kara: Scattered across the country.")
    animate_text("You: Then we find them.")
    animate_text("Kara: Exactly.")

    animate_text("Another massive rumble echoes above.")
    pause(1)

    animate_text("You: The surface must be hell right now.")
    animate_text("Kara: Worse.")
    animate_text("Kara: Machines don't sleep.")
    animate_text("Kara: They don't panic.")
    animate_text("Kara: And now they own the world.")

    animate_text("A child can be heard crying faintly somewhere deeper in the shelter.")
    pause(1)

    animate_text("You: Wait...")
    animate_text("You: There are civilians here?")
    animate_text("Kara: Some military families made it inside before lockdown.")
    animate_text("You: So now we protect them too.")
    animate_text("Kara: Welcome to the Resistance.")
    animate_text("You slowly looks toward bunker blast door.")
    pause(1)

    animate_text("You: One day...")
    pause(1)

    animate_text("You: We're going back up there.")

    animate_text("Kara: And when we do...")
    animate_text("Kara: We take the world back.")

    animate_text("Distant thunder echoes far above ruined Earth.")
    pause(1)

    animate_text("System: Incoming encrypted transmission.")

    animate_text("Unknown leader: If anyone can hear this...")
    animate_text("Unknown leader: Humanity is not extinct.")
    animate_text("Unknown leader: Fight the machines.")
    animate_text("Unknown leader: Never surrender.")

    animate_text("Transmission ends.")
    animate_text("[LONG SILENCE]")
    pause(1)

    animate_text("You: ...Who was that?")
    animate_text("Kara: I don't know.")
    animate_text("Kara: But they just gave humanity hope.")
    animate_text("You reloads plasma rifle slowly.")
    pause(1)

    animate_text("You: Then let's give Skynet something to fear.")
    animate_text("Bunker lights dim as the camera slowly fades to darkness.")
    pause(1)

    animate_text("System: Level 15 Complete.")
    animate_text("System: Judgment Day Saga Complete.")
    animate_text("System: New Campaign Unlocked.")
    animate_text("System: Rise of the Resistance.")