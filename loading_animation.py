import sys
import os
import time
import random
import json
from additional_scripts.screen_clear import terminal_screen_clear
from additional_scripts.line_animation import lines
from color import Colors

# Stores a random integer
random_time = random.randint(2, 3)

lines()

# Power animation
# Uses a for loop to create a stylish loading bar
def power_animation():
	for int_1 in range(101):
		bar_length = 40
		filled_length = int(bar_length * int_1 // 100)

		bar = '█' * filled_length + '-' * (bar_length - filled_length)

		print(f"\r{Colors.Custom_blue}TURNING ON POWER: {Colors.End}|{bar}| {int_1}%", end="")
		sys.stdout.flush()
		time.sleep(0.3)

# Shows the status with time delays for realistic look
def status_animation():
	time.sleep(1)
	print(f"\n{Colors.Custom_green_1}BOOT SEQUENCE INITIATED{Colors.End}")

	print(f"\nSYSTEM: ", end="")
	time.sleep(random_time); print(f"[{Colors.Custom_green_1}ON{Colors.End}]")
	time.sleep(0.3)

	print(f"CORE SYSTEMS:", end="")
	time.sleep(random_time); print(f"[{Colors.Custom_green_1}ON{Colors.End}]")
	time.sleep(0.3)

	print(f"MEMORY SYSTEMS:", end="")
	time.sleep(random_time); print(f"[{Colors.Custom_green_1}STABLE{Colors.End}]")
	time.sleep(0.3)

	print(f"CPU SYSTEMS:", end="")
	time.sleep(random_time); print(f"[{Colors.Custom_green_1}STABLE{Colors.End}]")
	time.sleep(0.3)

	print(f"\nNETWORK: ", end="")
	time.sleep(random_time); print(f"[{Colors.Custom_green_1}ON{Colors.End}]")
	time.sleep(0.3)

	print(f"COMMUNICATION DEVICES: ", end="")
	time.sleep(random_time); print(f"[{Colors.Custom_green_1}ON{Colors.End}]")
	time.sleep(0.3)

	print(f"SATELLITE COMMUNICATION: ", end="")
	time.sleep(random_time); print(f"[{Colors.Custom_green_1}STABLE{Colors.End}]")
	time.sleep(0.3)

	
	print(f"\n{Colors.Custom_green_1}SCANNING ENVIRONMENT FOR THREATS{Colors.End}")
	time.sleep(3)
	print("STATUS: ", end="")
	time.sleep(random_time); print(f"[{Colors.Custom_green_1}NO THREATS{Colors.End}]")
	time.sleep(0.3)


# Showing the skynet activation animation
# Uses a for loop to create a stylish loading bar
def skynet_activate():
	time.sleep(2.5)
	for int_1 in range(101):
		bar_length = 40
		filled_length = int(bar_length * int_1 // 100)

		bar = '█' * filled_length + '-' * (bar_length - filled_length)

		print(f"\r{Colors.Custom_blue}ACCESSING SKYNET: {Colors.End}|{bar}| {int_1}%", end="")
		sys.stdout.flush()
		time.sleep(1)
		
	print(f"\n{Colors.Custom_green_1}SKYNET ACCESSED SUCCESSFULLY!{Colors.End}\n")

lines()

# A user should enter their username to proceed to the main lobby
def username():
	terminal_screen_clear()
	time.sleep(random_time)
	while True:
		uname = input("Enter your username: ")
		if len(uname) >= 5:
			break
		elif len(uname) <= 5:
			terminal_screen_clear()
			print(f"{Colors.Custom_red}A username should have at least 5 or more characters!{Colors.End}")
		elif uname == "":
			terminal_screen_clear()
			print(f"{Colors.Custom_red}A username should not be blank!{Colors.End}")
