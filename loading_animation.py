import sys
import os
import time
import json
from color import Colors

# Edson part
def loading_animation():

	print("Accessing Skynet...\n")

	for i in range(101):
		bar_length = 40
		filled_length = int(bar_length * i // 100)

		bar = '█' * filled_length + '-' * (bar_length - filled_length)

		print(f"\r{Colors.Custom_blue}LOADING: {Colors.End}|{bar}| {i}%", end="")
		sys.stdout.flush()
		time.sleep(0.1)
		
	
	print("\nSkynet accessed successfully!\n")
