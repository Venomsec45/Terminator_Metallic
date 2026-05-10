from levels.Level_1 import level1
from levels.Level_2 import level2
from levels.Level_3 import level3
from levels.Level_4 import level4
from levels.Level_5 import level5
from levels.Level_6 import level6

# IMPORTANT: import run_level from wherever you defined it
from game_flow import run_level


def start_campaign(player_state):

    # Run all levels using run_level system
    player_state = run_level(level1, "Level 1", player_state)
    player_state = run_level(level2, "Level 2", player_state)
    player_state = run_level(level3, "Level 3", player_state)
    player_state = run_level(level4, "Level 4", player_state)
    player_state = run_level(level5, "Level 5", player_state)
    player_state = run_level(level6, "Level 6", player_state)

    print("\nCAMPAIGN COMPLETE!")
    print(f"Final Coins: {player_state['coins']}")
    print(f"Final XP: {player_state['xp']}")
    print(f"Weapon: {player_state['weapon']}")

    return player_state