import subprocess as sub
import os

def terminal_screen_clear():
	sub.run("clear" if os.name == "posix" else "cls")
