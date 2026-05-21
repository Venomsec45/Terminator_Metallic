def reset_player_state(player_state):
    
    player_state["hp"] = 100
    player_state["max_hp"] = 100
    player_state["coins"] = 0
    player_state["xp"] = 0
    player_state["level"] = 1
    player_state["inventory"] = []
    player_state["damage"] = 10
    player_state["base_damage"] = 10
    player_state["bonus_damage"] = 0
    player_state["xp_boost"] = 1
    player_state["weapon"] = "Fists"
    player_state["game_over"] = False
    player_state["leave_campaign"] = False

    return player_state
