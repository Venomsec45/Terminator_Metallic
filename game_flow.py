def run_level(level_function, level_name, player_state):

    print(f"\n=== {level_name} ===")

    player_state = level_function(player_state)

    return player_state