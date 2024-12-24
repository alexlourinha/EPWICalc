from calculators.def_calc import calculate_def_stats
from calculators.mana_calc import calculate_mana
from calculators.stat_point_calc import calculate_ability_points, calculate_vit, calculate_hp_equip_stat, \
    calculate_max_hp, \
    calculate_str, calculate_dex, calculate_mag, calculate_mana_equip_stat, calculate_max_mana
from calculators.attack_calc import calculate_attack
from calculators.hp_calc import calculate_hp
from classes.character import Character


def calculate_character_hp_and_mana(char):

    total_hp_buff = 0
    total_mana_buff = 0

    total_vit = calculate_vit(char)
    total_mag = calculate_mag(char)

    equip_hp = calculate_hp_equip_stat(char)
    max_hp = calculate_max_hp(char)
    equip_mana = calculate_mana_equip_stat(char)
    max_mana = calculate_max_mana(char)

    if any("Beast King's Inspiration - Sage" in x for x in char.get("active_buffs")):
        total_hp_buff = total_hp_buff + 0.40
    if any("Passive HP 3" in x for x in char.get("active_buffs")):
        total_hp_buff = total_hp_buff + 0.15
    if any("Tiger Form - Sage" in x for x in char.get("active_buffs")):
        total_hp_buff = total_hp_buff + 0.40
    if any("Copper Paperweight" in x for x in char.get("active_buffs")):
        total_hp_buff = total_hp_buff + 0.10

    hp = calculate_hp(level=char.get("level"),
                 char_class=char.get("char_class"),
                 vit=total_vit,
                 buff_total=round(total_hp_buff, 2),
                 equip_hp=equip_hp,
                 equip_perc_increase=round(max_hp, 2))

    mp = calculate_mana(level=char.get("level"),
                 char_class=char.get("char_class"),
                 mag=total_mag,
                 buff_total=round(total_mana_buff, 2),
                 equip_mana=equip_mana,
                 equip_perc_increase=round(max_mana, 2))

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
                          atk_rate=0,
                          speed=0,
                          accuracy=0,
                          evasion=0,
                          crit_rate=0,
                          atk_level=0,
                          def_level=0,
                          spirit=0,
                          soulforce=0,
                          stealth_level=0,
                          detection_level=0,
                          slaying_level=0,
                          warding_level=0,
                          phys_penetration=0,
                          mag_penetration=0,
                          casting_time=0,
                          reputation=char.get("reputation")
                          )
    return character
