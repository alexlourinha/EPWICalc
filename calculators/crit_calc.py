import math
from math import floor

from calculators.stat_point_calc import calculate_dex, calculate_equip_crit


def crit_calc(character):
    dex = calculate_dex(character)
    equip_crit = calculate_equip_crit(character)
    buff_crit = 0

    crit_rate = round(1 + math.floor(dex / 20) + equip_crit + buff_crit)

    return crit_rate