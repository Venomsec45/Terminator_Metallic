import sys
import os
import time
import json

# Dayshaun part, ignore mo nalang ito
def check_codes():
	main_directory = [
		root
		for root, _, _ in os.walk(os.path.dirname(__file__))
	]

	subdirectories = [
		directory
		for _, directory, _ in os.walk(os.path.dirname(__file__))
	]

	files = [
		file
		for _, _, files in os.walk(os.path.dirname(__file__))
		for file in files
	]

	if not os.path.exists(f"{os.path.dirname(__file__)}/.project_codes_snapshot.json"):
		snapshot = {
			"Main directory": main_directory,
			"Subdirectories": subdirectories,
			"Files": files
		}

		with open(f"{os.path.dirname(__file__)}/.project_codes_snapshot.json", "w") as file:
			json.dump(snapshot, file, indent=4)


check_codes()

# Edson part
def loading_animation():

	print("Accessing Skynet...\n")

	for i in range(101):
		bar_length = 40
		filled_length = int(bar_length * i // 100)

		bar = '█' * filled_length + '-' * (bar_length - filled_length)

		print(f"\rloading: |{bar}| {i}%", end="")
		sys.stdout.flush()
		time.sleep(0.03)
	
	print("\nSkynet accessed successfully!\n")