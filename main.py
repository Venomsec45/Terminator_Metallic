import time
import sys
from additional_scripts.screen_clear import terminal_screen_clear
from color import Colors
from developer_logo import *
from loading_animation import *

# Logo
try:
    for logo_function_call in [logo, logo_2]:
        terminal_screen_clear()
        logo_function_call()
        time.sleep(3)

    # Looping functions for cleanliness
    terminal_screen_clear()
    for function_call in [power_animation, status_animation, skynet_activate]:
        function_call()

except KeyboardInterrupt:
    print(f"{Colors.Custom_red}Game stopped{Colors.End}")
    sys.exit(2)