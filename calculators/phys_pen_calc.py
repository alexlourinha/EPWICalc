from calculators.stat_point_calc import calculate_phys_penetration


def calc_phys_pen(character):
    equip_phys_pen = calculate_phys_penetration(character)
    buff_phys_pen = 0

    result = equip_phys_pen + buff_phys_pen

    return result