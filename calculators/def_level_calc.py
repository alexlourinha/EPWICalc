from calculators.stat_point_calc import calculate_def_level


def calc_def_level(character):

    equip_def_level = calculate_def_level(character)
    buff_def_level = 0

    result = equip_def_level + buff_def_level

    return result