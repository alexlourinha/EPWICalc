from calculators.stat_point_calc import calculate_warding_level


def calc_warding_level(character):
    equip_warding_level = calculate_warding_level(character)
    buff_warding_level = 0

    result = equip_warding_level + buff_warding_level

    return result