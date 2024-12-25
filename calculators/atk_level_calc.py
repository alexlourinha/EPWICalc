from calculators.stat_point_calc import calculate_atk_level


def calc_atk_level(character):

    equip_atk_level = calculate_atk_level(character)
    buff_atk_level = 0

    result = equip_atk_level + buff_atk_level

    return result