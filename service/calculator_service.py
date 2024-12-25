from calculators.accuracy_calc import calc_accuracy
from calculators.atk_level_calc import calc_atk_level
from calculators.attack_calc import calculate_attack
from calculators.attack_rate_calc import calc_atk_rate
from calculators.channeling_calc import calc_channeling
from calculators.crit_calc import crit_calc
from calculators.def_calc import calculate_def_stats
from calculators.def_level_calc import calc_def_level
from calculators.detection_calc import calc_detection_level
from calculators.evasion_calc import calc_evasion
from calculators.hp_calc import calculate_hp
from calculators.mag_pen_calc import calc_mag_pen
from calculators.mana_calc import calculate_mana
from calculators.phys_pen_calc import calc_phys_pen
from calculators.slaying_calc import calc_slaying_level
from calculators.soulforce_calc import calc_soulforce
from calculators.speed_calc import calculate_speed
from calculators.spirit_calc import calc_spirit
from calculators.stat_point_calc import calculate_ability_points, calculate_vit, calculate_hp_equip_stat, \
    calculate_max_hp, calculate_str, calculate_dex, calculate_mag, calculate_mana_equip_stat, calculate_max_mana
from calculators.stealth_calc import calc_stealth_level
from calculators.warding_calc import calc_warding_level
from classes.character import Character


def calculate_character_hp_and_mana(char):

    hp = calculate_hp(char)[0]
    total_vit = calculate_hp(char)[1]

    mp = calculate_mana(char)[0]
    total_mag = calculate_mana(char)[1]

    return [hp, total_vit, mp, total_mag]

def calculate_character_stats(char):

    hp = calculate_character_hp_and_mana(char)[0]
    mp = calculate_character_hp_and_mana(char)[2]
    vitality = calculate_character_hp_and_mana(char)[1]
    magic = calculate_character_hp_and_mana(char)[3]
    ability_points = calculate_ability_points(char.get("level"),
                                              char.get("past_life_1"),
                                              char.get("past_life_2"))
    atk = calculate_attack(char)
    strength = calculate_str(char)
    dexterity = calculate_dex(char)
    magic = calculate_mag(char)

    total_phys_def_buff = 0
    total_mag_def_buff = 0

    if any("Passive Defense 8" in x for x in char.get("active_buffs")):
        total_phys_def_buff = total_phys_def_buff + 0.64
    if any("Passive Defense 8" in x for x in char.get("active_buffs")):
        total_mag_def_buff = total_mag_def_buff + 0.64

    def_stats = calculate_def_stats(char, vitality, strength, magic, total_phys_def_buff, total_mag_def_buff)
    speed = calculate_speed(char)
    attack_rate = calc_atk_rate(char)
    crit_rate = crit_calc(char)
    accuracy = calc_accuracy(char)
    evasion = calc_evasion(char)
    casting_time = calc_channeling(char)
    atk_level = calc_atk_level(char)
    def_level = calc_def_level(char)
    stealth_level = calc_stealth_level(char)
    detection_level = calc_detection_level(char)
    spirit = calc_spirit(char)
    slaying_level = calc_slaying_level(char)
    warding_level = calc_warding_level(char)
    phys_penetration = calc_phys_pen(char)
    mag_penetration = calc_mag_pen(char)
    soulforce = calc_soulforce(char)


    character = Character(char_class=char.get("char_class"),
                          level=char.get("level"),
                          past_life_1=char.get("past_life_1"),
                          past_life_2=char.get("past_life_2"),
                          ability_points= ability_points,
                          vitality=vitality,
                          strength=strength,
                          dexterity=dexterity,
                          magic=magic,
                          hp=hp,
                          mana=mp,
                          atk=atk,
                          phys_def=def_stats.get("phys_def"),
                          mag_def=def_stats.get("mag_def"),
                          atk_rate=attack_rate,
                          speed=speed,
                          accuracy=accuracy,
                          evasion=evasion,
                          crit_rate=crit_rate,
                          atk_level=atk_level,
                          def_level=def_level,
                          spirit=spirit,
                          soulforce=soulforce,
                          stealth_level=stealth_level,
                          detection_level=detection_level,
                          slaying_level=slaying_level,
                          warding_level=warding_level,
                          phys_penetration=phys_penetration,
                          mag_penetration=mag_penetration,
                          casting_time=casting_time,
                          reputation=char.get("reputation")
                          )
    return character
