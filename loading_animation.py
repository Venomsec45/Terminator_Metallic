import sys
import os
import time
import random
import json
from additional_scripts.screen_clear import terminal_screen_clear
from color import Colors

# Stores a random integer
random_time = random.randint(2, 3)

# Power animation
# Uses a for loop to create a stylish loading bar
def power_animation():
	for int_1 in range(101):
		bar_length = 40
		filled_length = int(bar_length * int_1 // 100)

		bar = '█' * filled_length + '-' * (bar_length - filled_length)

		print(f"\r{Colors.Custom_blue}TURNING ON POWER: {Colors.End}|{bar}| {int_1}%", end="")
		sys.stdout.flush()
		time.sleep(0.03)

# Shows the status with time delays for realistic look
def status_animation():
	time.sleep(1)
	print(f"\n{Colors.Custom_green_1}BOOT SEQUENCE INITIATED{Colors.End}")

	print(f"\nSYSTEM: ", end="", flush=True)
	time.sleep(random_time); print(f"[{Colors.Custom_green_1}ON{Colors.End}]")
	time.sleep(0.2)

	print(f"CORE SYSTEMS: ", end="", flush=True)
	time.sleep(random_time); print(f"[{Colors.Custom_green_1}ON{Colors.End}]")
	time.sleep(0.2)

	print(f"MEMORY SYSTEMS: ", end="", flush=True)
	time.sleep(random_time); print(f"[{Colors.Custom_green_1}STABLE{Colors.End}]")
	time.sleep(0.2)

	print(f"CPU SYSTEMS: ", end="", flush=True)
	time.sleep(random_time); print(f"[{Colors.Custom_green_1}STABLE{Colors.End}]")
	time.sleep(0.2)

	print(f"\nSERVER: ", end="", flush=True)
	time.sleep(random_time); print(f"[{Colors.Custom_green_1}ON{Colors.End}]")
	time.sleep(0.2)

	print(f"NETWORK: ", end="", flush=True)
	time.sleep(random_time); print(f"[{Colors.Custom_green_1}ON{Colors.End}]")
	time.sleep(0.2)

	print(f"COMMUNICATION DEVICES: ", end="", flush=True)
	time.sleep(random_time); print(f"[{Colors.Custom_green_1}ON{Colors.End}]")
	time.sleep(0.2)

	print(f"SATELLITE COMMUNICATION: ", end="", flush=True)
	time.sleep(random_time); print(f"[{Colors.Custom_green_1}STABLE{Colors.End}]")
	time.sleep(0.2)

	print(f"SIGNAL: ", end="", flush=True)
	time.sleep(random_time); print(f"[{Colors.Custom_green_1}STABLE{Colors.End}]")
	time.sleep(0.2)

	print(f"\n{Colors.Custom_green_1}DEFENSE SYSTEM ACTIVATED{Colors.End}")
	time.sleep(2)
	print("AUTOMATIC MACHINE GUN: ", end="", flush=True)
	time.sleep(random_time); print(f"[{Colors.Custom_green_1}ACTIVATED{Colors.End}]")
	time.sleep(0.2)

	print("RADAR: ", end="", flush=True)
	time.sleep(random_time); print(f"[{Colors.Custom_green_1}ACTIVATED{Colors.End}]")
	time.sleep(0.2)

	print("UAV: ", end="", flush=True)
	time.sleep(random_time); print(f"[{Colors.Custom_green_1}OPERATING{Colors.End}]")
	time.sleep(0.2)

	print("GROUND EXPLOSIVES: ", end="", flush=True)
	time.sleep(random_time); print(f"[{Colors.Custom_green_1}ACTIVATED{Colors.End}]")
	time.sleep(0.2)

	print("MISSILES: ", end="", flush=True)
	time.sleep(random_time); print(f"[{Colors.Custom_green_1}ACTIVE{Colors.End}]")
	time.sleep(0.2)

	print("NUCLEAR WEAPONS: ", end="", flush=True)
	time.sleep(random_time); print(f"[{Colors.Custom_green_1}ACTIVATED{Colors.End}]")
	time.sleep(0.2)	
	
	print(f"\n{Colors.Custom_green_1}SCANNING ENVIRONMENT FOR THREATS{Colors.End}")
	time.sleep(2)
	print("STATUS: ", end="", flush=True)
	time.sleep(random_time); print(f"[{Colors.Custom_green_1}SCANNED COMPLETE{Colors.End}]")

	print("THREATS: ", end="", flush=True)
	time.sleep(random_time); print(f"[{Colors.Custom_green_1}0{Colors.End}]")
	time.sleep(2)


# Showing the skynet activation animation
# Uses a for loop to create a stylish loading bar
def skynet_activate():
	time.sleep(3)
	for int_1 in range(101):
		bar_length = 40
		filled_length = int(bar_length * int_1 // 100)

		bar = '█' * filled_length + '-' * (bar_length - filled_length)

		print(f"\r{Colors.Custom_blue}ACCESSING SKYNET: {Colors.End}|{bar}| {int_1}%", end="")
		sys.stdout.flush()
		time.sleep(0.5)
		
	print(f"\n{Colors.Custom_green_1}SKYNET ACCESSED SUCCESSFULLY!{Colors.End}\n")

# A user should enter their username to proceed to the main lobby
def username():
	terminal_screen_clear()
	time.sleep(random_time)
	while True:
		uname = input("Enter your username: ")
		if len(uname) >= 5:
			return uname
		elif uname == "":
			terminal_screen_clear()
			print(f"{Colors.Custom_red}A username should not be blank!{Colors.End}")
		elif len(uname) <= 5:
			terminal_screen_clear()
			print(f"{Colors.Custom_red}A username should have at least 5 or more characters!{Colors.End}")
