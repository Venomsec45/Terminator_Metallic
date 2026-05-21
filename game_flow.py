def run_level(level_function, level_name, player_state):

    if player_state.get("game_over") or player_state.get("leave_campaign"):
        return player_state

    print("\n" + "=" * 40 + f"{level_name}" + "=" * 40)

    player_state = level_function(player_state)

    # CHECK IF PLAYER DIED
    if player_state["hp"] <= 0:
        print("\nGAME OVER - RESETTING PROGRESS")
        player_state["game_over"] = True

    return player_state