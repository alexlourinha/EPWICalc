from calculators.stat_point_calc import calculate_mag_penetration


def calc_mag_pen(character):
    equip_mag_pen = calculate_mag_penetration(character)
    buff_mag_pen = 0

    result = equip_mag_pen + buff_mag_pen

    return result