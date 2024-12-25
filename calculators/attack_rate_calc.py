from calculators.stat_point_calc import calculate_interval


def calc_atk_rate(character) :

    weapon = character.get("weapon")

    equip_int = calculate_interval(character)

    atk_rate = 5

    if weapon:
        weapon_int = round(1/weapon.get("atk_rate"), 2)
        interval = weapon_int - equip_int
        atk_rate = 1/interval


    return round(atk_rate, 2)