from calculators.stat_point_calc import calculate_slaying_level


def calc_slaying_level(character):
    equip_slaying_level = calculate_slaying_level(character)
    buff_slaying_level = 0

    result = equip_slaying_level + buff_slaying_level

    return result