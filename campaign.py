from campaign_levels.level1 import level1
from campaign_levels.level2 import level2
from campaign_levels.level3 import level3
from campaign_levels.level4 import level4
from campaign_levels.level5 import level5
from campaign_levels.level6 import level6

def start_campaign(username, xp, coins, wins):
    for level in [level1, level2, level3, level4, level5, level6]:
        gained_xp, gained_coins, win = level(username)
        xp += gained_xp
        coins += gained_coins
        wins += win

    return xp, coins, wins