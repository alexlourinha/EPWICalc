from calculators.stat_point_calc import calculate_equip_channeling_perc


def calc_channeling(character):

    equip_channeling = calculate_equip_channeling_perc(character)
    buff_channeling = 0

    channeling = equip_channeling + buff_channeling

    return channeling