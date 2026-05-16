from levels.Level_1 import level1
from levels.Level_2 import level2
from levels.Level_3 import level3
from levels.Level_4 import level4
from levels.Level_5 import level5
from levels.Level_6 import level6
from levels.Level_7 import level7
from levels.Level_8 import level8
from levels.Level_9 import level9
from levels.Level_10 import level10
from levels.Level_11 import level11
from levels.Level_12 import level12
from levels.Level_13 import level13
from levels.Level_14 import level14

from game_flow import run_level


def start_campaign(player_state):
    player_state = run_level(level1, "Level 1", player_state)
    if player_state.get("game_over") or player_state.get("leave_campaign"):
        return player_state

    player_state = run_level(level2, "Level 2", player_state)
    if player_state.get("game_over") or player_state.get("leave_campaign"):
        return player_state

    player_state = run_level(level3, "Level 3", player_state)
    if player_state.get("game_over") or player_state.get("leave_campaign"):
        return player_state

    player_state = run_level(level4, "Level 4", player_state)
    if player_state.get("game_over") or player_state.get("leave_campaign"):
        return player_state

    player_state = run_level(level5, "Level 5", player_state)
    if player_state.get("game_over") or player_state.get("leave_campaign"):
        return player_state

    player_state = run_level(level6, "Level 6", player_state)
    if player_state.get("game_over") or player_state.get("leave_campaign"):
        return player_state

    player_state = run_level(level7, "Level 7", player_state)
    if player_state.get("game_over") or player_state.get("leave_campaign"):
        return player_state

    player_state = run_level(level8, "Level 8", player_state)
    if player_state.get("game_over") or player_state.get("leave_campaign"):
        return player_state

    player_state = run_level(level9, "Level 9", player_state)
    if player_state.get("game_over") or player_state.get("leave_campaign"):
        return player_state

    player_state = run_level(level10, "Level 10", player_state)
    if player_state.get("game_over") or player_state.get("leave_campaign"):
        return player_state

    player_state = run_level(level11, "Level 11", player_state)
    if player_state.get("game_over") or player_state.get("leave_campaign"):
        return player_state

    player_state = run_level(level12, "Level 12", player_state)
    if player_state.get("game_over") or player_state.get("leave_campaign"):
        return player_state

    player_state = run_level(level13, "Level 13", player_state)
    if player_state.get("game_over") or player_state.get("leave_campaign"):
        return player_state

    player_state = run_level(level14, "Level 14", player_state)
    if player_state.get("game_over") or player_state.get("leave_campaign"):
        return player_state

    print("\nCAMPAIGN COMPLETE!")
    print(f"Final Coins: {player_state['coins']}")
    print(f"Final XP: {player_state['xp']}")
    print(f"Weapon: {player_state['weapon']}")

    return player_state