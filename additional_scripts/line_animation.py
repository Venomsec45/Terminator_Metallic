import time

def lines():
	lines = "-" * 58
	for line in lines:
		print(f"{line}", end="", flush=True)
		time.sleep(0.05)

lines()
