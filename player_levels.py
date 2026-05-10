def xp_needed(level):
    return 50 + (level - 1) * 25


def check_level_up(player_state):
    while player_state["xp"] >= xp_needed(player_state["level"]):

        player_state["xp"] -= xp_needed(player_state["level"])
        player_state["level"] += 1

        hp_gain = 10
        player_state["max_hp"] += hp_gain
        player_state["hp"] += hp_gain

        player_state["damage"] += 2

        print(f"\nLEVEL UP! You are now level {player_state['level']}")
        print(f"+{hp_gain} Max HP, +2 Damage")

    return player_state