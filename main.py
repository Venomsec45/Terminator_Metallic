import os
import subprocess as sub
import time
import sys
from developer_logo import logo
from loading_animation import loading_animation

sub.run("clear" if os.name == "posix" else "cls")
print(logo())
time.sleep(2)
loading_animation()