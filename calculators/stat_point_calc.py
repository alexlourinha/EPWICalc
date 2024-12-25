from helper.valid_stats_processor import add_valid_stats


def calculate_ability_points(level, past_life_1, past_life_2):
    past_life_stat_per_level = {100: 20, 101: 25, 102: 32, 103: 42, 104: 56, 105: 76}
    base_points = (level - 1) * 5
    life_points = past_life_stat_per_level[past_life_1] + past_life_stat_per_level[past_life_2]
    return base_points + life_points


def calculate_str(character):
    strength_stats = [character.get("weapon").get("attributes").get("strength"),
                      character.get("head").get("stats").get("strength"),
                      character.get("chest").get("stats").get("strength"),
                      character.get("legs").get("stats").get("strength"),
                      character.get("feet").get("stats").get("strength"),
                      character.get("arms").get("stats").get("strength"),
                      character.get("robe").get("stats").get("strength"),
                      character.get("belt").get("stats").get("strength"),
                      character.get("necklace").get("stats").get("strength"),
                      character.get("ring_1").get("stats").get("strength"),
                      character.get("ring_2").get("stats").get("strength"),
                      character.get("set_bonus").get("strength"),
                      character.get("tome").get("stats").get("strength")]

    base_strength = character.get("strength")
    other_strength = add_valid_stats(strength_stats)
    result = base_strength + other_strength
    return result


def calculate_dex(character):
    dexterity_stats = [character.get("weapon").get("attributes").get("dexterity"),
                       character.get("head").get("stats").get("dexterity"),
                       character.get("chest").get("stats").get("dexterity"),
                       character.get("legs").get("stats").get("dexterity"),
                       character.get("feet").get("stats").get("dexterity"),
                       character.get("arms").get("stats").get("dexterity"),
                       character.get("robe").get("stats").get("dexterity"),
                       character.get("belt").get("stats").get("dexterity"),
                       character.get("necklace").get("stats").get("dexterity"),
                       character.get("ring_1").get("stats").get("dexterity"),
                       character.get("ring_2").get("stats").get("dexterity"),
                       character.get("set_bonus").get("dexterity"),
                       character.get("tome").get("stats").get("dexterity")]

    base_dexterity = character.get("dexterity")
    other_dexterity = add_valid_stats(dexterity_stats)
    result = base_dexterity + other_dexterity
    return result


def calculate_mag(character):
    magic_stats = [character.get("weapon").get("attributes").get("magic"),
                   character.get("head").get("stats").get("magic"),
                   character.get("chest").get("stats").get("magic"),
                   character.get("legs").get("stats").get("magic"),
                   character.get("feet").get("stats").get("magic"),
                   character.get("arms").get("stats").get("magic"),
                   character.get("robe").get("stats").get("magic"),
                   character.get("belt").get("stats").get("magic"),
                   character.get("necklace").get("stats").get("magic"),
                   character.get("ring_1").get("stats").get("magic"),
                   character.get("ring_2").get("stats").get("magic"),
                   character.get("set_bonus").get("magic"),
                   character.get("tome").get("stats").get("magic")]

    base_magic = character.get("magic")
    other_magic = add_valid_stats(magic_stats)
    result = base_magic + other_magic
    return result


def calculate_vit(character):
    vitality_stats = [character.get("weapon").get("attributes").get("vitality"),
                      character.get("head").get("stats").get("vitality"),
                      character.get("chest").get("stats").get("vitality"),
                      character.get("legs").get("stats").get("vitality"),
                      character.get("feet").get("stats").get("vitality"),
                      character.get("arms").get("stats").get("vitality"),
                      character.get("robe").get("stats").get("vitality"),
                      character.get("belt").get("stats").get("vitality"),
                      character.get("necklace").get("stats").get("vitality"),
                      character.get("ring_1").get("stats").get("vitality"),
                      character.get("ring_2").get("stats").get("vitality"),
                      character.get("set_bonus").get("vitality"),
                      character.get("tome").get("stats").get("vitality")]

    base_vitality = character.get("vitality")
    other_vitality = add_valid_stats(vitality_stats)
    result = base_vitality + other_vitality
    return result


def calculate_mana_equip_stat(character):
    equip_mp_stats = [character.get("weapon").get("attributes").get("mp"),
                      character.get("head").get("stats").get("mp"),
                      character.get("chest").get("stats").get("mp"),
                      character.get("legs").get("stats").get("mp"),
                      character.get("feet").get("stats").get("mp"),
                      character.get("arms").get("stats").get("mp"),
                      character.get("robe").get("stats").get("mp"),
                      character.get("belt").get("stats").get("mp"),
                      character.get("necklace").get("stats").get("mp"),
                      character.get("ring_1").get("stats").get("mp"),
                      character.get("ring_2").get("stats").get("mp"),
                      character.get("set_bonus").get("mp"),
                      character.get("tome").get("stats").get("mp")]
    result = add_valid_stats(equip_mp_stats)
    return result


def calculate_max_mana(character):
    max_mp_stats = [character.get("weapon").get("attributes").get("max_mp"),
                    character.get("head").get("stats").get("max_mp"),
                    character.get("chest").get("stats").get("max_mp"),
                    character.get("legs").get("stats").get("max_mp"),
                    character.get("feet").get("stats").get("max_mp"),
                    character.get("arms").get("stats").get("max_mp"),
                    character.get("robe").get("stats").get("max_mp"),
                    character.get("belt").get("stats").get("max_mp"),
                    character.get("set_bonus").get("max_mp"),
                    character.get("necklace").get("stats").get("max_mp"),
                    character.get("ring_1").get("stats").get("max_mp"),
                    character.get("ring_2").get("stats").get("max_mp")]

    result = add_valid_stats(max_mp_stats)

    return result


def calculate_hp_equip_stat(character):
    equip_hp_stats = [character.get("weapon").get("attributes").get("hp"),
                      character.get("head").get("stats").get("hp"),
                      character.get("chest").get("stats").get("hp"),
                      character.get("legs").get("stats").get("hp"),
                      character.get("feet").get("stats").get("hp"),
                      character.get("arms").get("stats").get("hp"),
                      character.get("robe").get("stats").get("hp"),
                      character.get("belt").get("stats").get("hp"),
                      character.get("necklace").get("stats").get("hp"),
                      character.get("ring_1").get("stats").get("hp"),
                      character.get("ring_2").get("stats").get("hp"),
                      character.get("set_bonus").get("hp"),
                      character.get("constellation").get("hp_1"),
                      character.get("constellation").get("hp_2"),
                      character.get("constellation").get("hp_3"),
                      character.get("constellation").get("hp_4"),
                      character.get("constellation").get("hp_5"),
                      character.get("constellation").get("hp_6"),
                      character.get("constellation").get("hp_7"),
                      character.get("glyph_1").get("hp"),
                      character.get("glyph_2").get("hp"),
                      character.get("glyph_3").get("hp"),
                      character.get("glyph_4").get("hp"),
                      character.get("glyph_5").get("hp"),
                      character.get("glyph_6").get("hp"),
                      character.get("meridian").get("hp"),
                      character.get("tome").get("stats").get("hp")]
    result = add_valid_stats(equip_hp_stats)
    return result


def calculate_max_hp(character):
    constellation_hp_buff = 0

    if all(character.get("constellation").get(f"phys_def_{i}") > 0 for i in range(1, 8)):
        constellation_hp_buff = 0.05

    max_hp_stats = [character.get("weapon").get("attributes").get("max_hp"),
                    character.get("head").get("stats").get("max_hp"),
                    character.get("chest").get("stats").get("max_hp"),
                    character.get("legs").get("stats").get("max_hp"),
                    character.get("feet").get("stats").get("max_hp"),
                    character.get("arms").get("stats").get("max_hp"),
                    character.get("robe").get("stats").get("max_hp"),
                    character.get("belt").get("stats").get("max_hp"),
                    character.get("necklace").get("stats").get("max_hp"),
                    character.get("ring_1").get("stats").get("max_hp"),
                    character.get("ring_2").get("stats").get("max_hp"),
                    character.get("set_bonus").get("max_hp"),
                    constellation_hp_buff]

    result = add_valid_stats(max_hp_stats)

    return result


def phys_atk_total_excl_weapon(character):
    phys_atk_stats = [character.get("head").get("stats").get("phys_atk"),
                      character.get("chest").get("stats").get("phys_atk"),
                      character.get("legs").get("stats").get("phys_atk"),
                      character.get("feet").get("stats").get("phys_atk"),
                      character.get("arms").get("stats").get("phys_atk"),
                      character.get("robe").get("stats").get("phys_atk"),
                      character.get("belt").get("stats").get("phys_atk"),
                      character.get("necklace").get("stats").get("phys_atk"),
                      character.get("ring_1").get("stats").get("phys_atk"),
                      character.get("ring_2").get("stats").get("phys_atk"),
                      character.get("set_bonus").get("phys_atk"),
                      character.get("glyph_1").get("phys_atk"),
                      character.get("glyph_2").get("phys_atk"),
                      character.get("glyph_3").get("phys_atk"),
                      character.get("glyph_4").get("phys_atk"),
                      character.get("glyph_5").get("phys_atk"),
                      character.get("glyph_6").get("phys_atk"),
                      character.get("meridian").get("phys_atk"),
                      character.get("title_stats").get("phys_atk"),
                      character.get("tome").get("stats").get("phys_atk")]

    result = add_valid_stats(phys_atk_stats)

    return result


def mag_atk_total_excl_weapon(character):
    mag_atk_stats = [character.get("head").get("stats").get("mag_atk"),
                     character.get("chest").get("stats").get("mag_atk"),
                     character.get("legs").get("stats").get("mag_atk"),
                     character.get("feet").get("stats").get("mag_atk"),
                     character.get("arms").get("stats").get("mag_atk"),
                     character.get("robe").get("stats").get("mag_atk"),
                     character.get("belt").get("stats").get("mag_atk"),
                     character.get("necklace").get("stats").get("mag_atk"),
                     character.get("ring_1").get("stats").get("mag_atk"),
                     character.get("ring_2").get("stats").get("mag_atk"),
                     character.get("set_bonus").get("mag_atk"),
                     character.get("glyph_1").get("mag_atk"),
                     character.get("glyph_2").get("mag_atk"),
                     character.get("glyph_3").get("mag_atk"),
                     character.get("glyph_4").get("mag_atk"),
                     character.get("glyph_5").get("mag_atk"),
                     character.get("glyph_6").get("mag_atk"),
                     character.get("meridian").get("mag_atk"),
                     character.get("title_stats").get("mag_atk"),
                     character.get("tome").get("stats").get("mag_atk")]

    result = add_valid_stats(mag_atk_stats)

    return result


def calculate_phys_def(character):
    phys_def_stats = [character.get("weapon").get("attributes").get("phys_def"),
                      character.get("head").get("stats").get("phys_def"),
                      character.get("chest").get("stats").get("phys_def"),
                      character.get("legs").get("stats").get("phys_def"),
                      character.get("feet").get("stats").get("phys_def"),
                      character.get("arms").get("stats").get("phys_def"),
                      character.get("robe").get("stats").get("phys_def"),
                      character.get("belt").get("stats").get("phys_def"),
                      character.get("necklace").get("stats").get("phys_def"),
                      character.get("ring_1").get("stats").get("phys_def"),
                      character.get("ring_2").get("stats").get("phys_def"),
                      character.get("set_bonus").get("phys_def"),
                      character.get("constellation").get("phys_def_1"),
                      character.get("constellation").get("phys_def_2"),
                      character.get("constellation").get("phys_def_3"),
                      character.get("constellation").get("phys_def_4"),
                      character.get("constellation").get("phys_def_5"),
                      character.get("constellation").get("phys_def_6"),
                      character.get("constellation").get("phys_def_7"),
                      character.get("glyph_1").get("phys_def"),
                      character.get("glyph_2").get("phys_def"),
                      character.get("glyph_3").get("phys_def"),
                      character.get("glyph_4").get("phys_def"),
                      character.get("glyph_5").get("phys_def"),
                      character.get("glyph_6").get("phys_def"),
                      character.get("meridian").get("phys_def"),
                      character.get("title_stats").get("phys_def"),
                      character.get("tome").get("stats").get("phys_def")]

    result = add_valid_stats(phys_def_stats)

    return result


def calculate_mag_def(character):
    mag_def_stats = [character.get("weapon").get("attributes").get("mag_def"),
                     character.get("head").get("stats").get("mag_def"),
                     character.get("chest").get("stats").get("mag_def"),
                     character.get("legs").get("stats").get("mag_def"),
                     character.get("feet").get("stats").get("mag_def"),
                     character.get("arms").get("stats").get("mag_def"),
                     character.get("robe").get("stats").get("mag_def"),
                     character.get("belt").get("stats").get("mag_def"),
                     character.get("necklace").get("stats").get("mag_def"),
                     character.get("ring_1").get("stats").get("mag_def"),
                     character.get("ring_2").get("stats").get("mag_def"),
                     character.get("set_bonus").get("mag_def"),
                     character.get("constellation").get("mag_def_1"),
                     character.get("constellation").get("mag_def_2"),
                     character.get("constellation").get("mag_def_3"),
                     character.get("constellation").get("mag_def_4"),
                     character.get("constellation").get("mag_def_5"),
                     character.get("constellation").get("mag_def_6"),
                     character.get("constellation").get("mag_def_7"),
                     character.get("glyph_1").get("mag_def"),
                     character.get("glyph_2").get("mag_def"),
                     character.get("glyph_3").get("mag_def"),
                     character.get("glyph_4").get("mag_def"),
                     character.get("glyph_5").get("mag_def"),
                     character.get("glyph_6").get("mag_def"),
                     character.get("meridian").get("mag_def"),
                     character.get("title_stats").get("mag_def"),
                     character.get("tome").get("stats").get("mag_def")]

    result = add_valid_stats(mag_def_stats)

    return result


def calculate_equip_speed(character):
    constellation_speed_buff = 0

    if all(character.get("constellation").get(f"hp_{i}") > 0 for i in range(1, 8)):
        constellation_speed_buff = 0.20

    speed_stats = [character.get("weapon").get("attributes").get("speed"),
                   character.get("head").get("stats").get("speed"),
                   character.get("chest").get("stats").get("speed"),
                   character.get("legs").get("stats").get("speed"),
                   character.get("feet").get("stats").get("speed"),
                   character.get("arms").get("stats").get("speed"),
                   character.get("robe").get("stats").get("speed"),
                   character.get("belt").get("stats").get("speed"),
                   character.get("necklace").get("stats").get("speed"),
                   character.get("ring_1").get("stats").get("speed"),
                   character.get("ring_2").get("stats").get("speed"),
                   character.get("set_bonus").get("speed"),
                   character.get("constellation").get("speed"),
                   character.get("constellation").get("speed"),
                   character.get("constellation").get("speed"),
                   character.get("constellation").get("speed"),
                   character.get("constellation").get("speed"),
                   character.get("constellation").get("speed"),
                   character.get("constellation").get("speed"),
                   character.get("glyph_1").get("speed"),
                   character.get("glyph_2").get("speed"),
                   character.get("glyph_3").get("speed"),
                   character.get("glyph_4").get("speed"),
                   character.get("glyph_5").get("speed"),
                   character.get("glyph_6").get("speed"),
                   character.get("meridian").get("speed"),
                   character.get("title_stats").get("speed"),
                   character.get("tome").get("stats").get("speed"),
                   constellation_speed_buff]

    result = add_valid_stats(speed_stats)

    return result


def calculate_interval(character):
    int_stats = [character.get("weapon").get("attributes").get("int"),
                 character.get("head").get("stats").get("int"),
                 character.get("chest").get("stats").get("int"),
                 character.get("legs").get("stats").get("int"),
                 character.get("feet").get("stats").get("int"),
                 character.get("arms").get("stats").get("int"),
                 character.get("robe").get("stats").get("int"),
                 character.get("belt").get("stats").get("int"),
                 character.get("necklace").get("stats").get("int"),
                 character.get("ring_1").get("stats").get("int"),
                 character.get("ring_2").get("stats").get("int"),
                 character.get("set_bonus").get("int"),
                 character.get("blessing").get("stats").get("int"),
                 character.get("tome").get("stats").get("int")]

    result = add_valid_stats(int_stats)

    return -result


def calculate_equip_crit(character):
    crit_stats = [character.get("weapon").get("attributes").get("crit_rate"),
                     character.get("head").get("stats").get("crit_rate"),
                     character.get("chest").get("stats").get("crit_rate"),
                     character.get("legs").get("stats").get("crit_rate"),
                     character.get("feet").get("stats").get("crit_rate"),
                     character.get("arms").get("stats").get("crit_rate"),
                     character.get("robe").get("stats").get("crit_rate"),
                     character.get("belt").get("stats").get("crit_rate"),
                     character.get("necklace").get("stats").get("crit_rate"),
                     character.get("ring_1").get("stats").get("crit_rate"),
                     character.get("ring_2").get("stats").get("crit_rate"),
                     character.get("set_bonus").get("crit_rate"),
                     character.get("tome").get("stats").get("crit_rate")]

    result = add_valid_stats(crit_stats)

    return result

def calculate_equip_acc(character):
    acc_stats = [character.get("weapon").get("attributes").get("accuracy"),
                     character.get("head").get("stats").get("accuracy"),
                     character.get("chest").get("stats").get("accuracy"),
                     character.get("legs").get("stats").get("accuracy"),
                     character.get("feet").get("stats").get("accuracy"),
                     character.get("arms").get("stats").get("accuracy"),
                     character.get("robe").get("stats").get("accuracy"),
                     character.get("belt").get("stats").get("accuracy"),
                     character.get("necklace").get("stats").get("accuracy"),
                     character.get("ring_1").get("stats").get("accuracy"),
                     character.get("ring_2").get("stats").get("accuracy"),
                     character.get("set_bonus").get("accuracy"),
                     character.get("meridian").get("accuracy"),
                     character.get("title_stats").get("accuracy"),
                     character.get("tome").get("stats").get("accuracy")]

    result = add_valid_stats(acc_stats)

    return result

def calculate_equip_acc_perc(character):
    acc_stats = [character.get("weapon").get("attributes").get("acc_perc"),
                     character.get("head").get("stats").get("acc_perc"),
                     character.get("chest").get("stats").get("acc_perc"),
                     character.get("legs").get("stats").get("acc_perc"),
                     character.get("feet").get("stats").get("acc_perc"),
                     character.get("arms").get("stats").get("acc_perc"),
                     character.get("robe").get("stats").get("acc_perc"),
                     character.get("belt").get("stats").get("acc_perc"),
                     character.get("necklace").get("stats").get("acc_perc"),
                     character.get("ring_1").get("stats").get("acc_perc"),
                     character.get("ring_2").get("stats").get("acc_perc"),
                     character.get("set_bonus").get("acc_perc"),
                     character.get("meridian").get("acc_perc"),
                     character.get("title_stats").get("acc_perc"),
                     character.get("tome").get("stats").get("acc_perc")]

    result = add_valid_stats(acc_stats)

    return result

def calculate_equip_evasion(character):
    evasion_stats = [character.get("weapon").get("attributes").get("evasion"),
                     character.get("head").get("stats").get("evasion"),
                     character.get("chest").get("stats").get("evasion"),
                     character.get("legs").get("stats").get("evasion"),
                     character.get("feet").get("stats").get("evasion"),
                     character.get("arms").get("stats").get("evasion"),
                     character.get("robe").get("stats").get("evasion"),
                     character.get("belt").get("stats").get("evasion"),
                     character.get("necklace").get("stats").get("evasion"),
                     character.get("ring_1").get("stats").get("evasion"),
                     character.get("ring_2").get("stats").get("evasion"),
                     character.get("set_bonus").get("evasion"),
                     character.get("meridian").get("evasion"),
                     character.get("title_stats").get("evasion"),
                     character.get("tome").get("stats").get("evasion")]

    result = add_valid_stats(evasion_stats)

    return result

def calculate_equip_evasion_perc(character):
    evasion_stats = [character.get("weapon").get("attributes").get("evasion_perc"),
                     character.get("head").get("stats").get("evasion_perc"),
                     character.get("chest").get("stats").get("evasion_perc"),
                     character.get("legs").get("stats").get("evasion_perc"),
                     character.get("feet").get("stats").get("evasion_perc"),
                     character.get("arms").get("stats").get("evasion_perc"),
                     character.get("robe").get("stats").get("evasion_perc"),
                     character.get("belt").get("stats").get("evasion_perc"),
                     character.get("necklace").get("stats").get("evasion_perc"),
                     character.get("ring_1").get("stats").get("evasion_perc"),
                     character.get("ring_2").get("stats").get("evasion_perc"),
                     character.get("set_bonus").get("evasion_perc"),
                     character.get("meridian").get("evasion_perc"),
                     character.get("title_stats").get("evasion_perc"),
                     character.get("tome").get("stats").get("evasion_perc")]

    result = add_valid_stats(evasion_stats)

    return result

def calculate_equip_channeling_perc(character):
    evasion_stats = [character.get("weapon").get("attributes").get("channeling"),
                     character.get("head").get("stats").get("channeling"),
                     character.get("chest").get("stats").get("channeling"),
                     character.get("legs").get("stats").get("channeling"),
                     character.get("feet").get("stats").get("channeling"),
                     character.get("arms").get("stats").get("channeling"),
                     character.get("robe").get("stats").get("channeling"),
                     character.get("belt").get("stats").get("channeling"),
                     character.get("necklace").get("stats").get("channeling"),
                     character.get("ring_1").get("stats").get("channeling"),
                     character.get("ring_2").get("stats").get("channeling"),
                     character.get("set_bonus").get("channeling"),
                     character.get("meridian").get("channeling"),
                     character.get("title_stats").get("channeling"),
                     character.get("tome").get("stats").get("channeling")]

    result = add_valid_stats(evasion_stats)

    return result

def calculate_atk_level(character):
    atk_level_stats = [character.get("weapon").get("attributes").get("atk_level"),
                     character.get("head").get("stats").get("atk_level"),
                     character.get("chest").get("stats").get("atk_level"),
                     character.get("legs").get("stats").get("atk_level"),
                     character.get("feet").get("stats").get("atk_level"),
                     character.get("arms").get("stats").get("atk_level"),
                     character.get("robe").get("stats").get("atk_level"),
                     character.get("belt").get("stats").get("atk_level"),
                     character.get("necklace").get("stats").get("atk_level"),
                     character.get("ring_1").get("stats").get("atk_level"),
                     character.get("ring_2").get("stats").get("atk_level"),
                     character.get("set_bonus").get("atk_level"),
                     character.get("constellation").get("atk_level_1"),
                     character.get("constellation").get("atk_level_2"),
                     character.get("constellation").get("atk_level_3"),
                     character.get("constellation").get("atk_level_4"),
                     character.get("constellation").get("atk_level_5"),
                     character.get("constellation").get("atk_level_6"),
                     character.get("constellation").get("atk_level_7"),
                     character.get("glyph_1").get("atk_level"),
                     character.get("glyph_2").get("atk_level"),
                     character.get("glyph_3").get("atk_level"),
                     character.get("glyph_4").get("atk_level"),
                     character.get("glyph_5").get("atk_level"),
                     character.get("glyph_6").get("atk_level"),
                     character.get("meridian").get("atk_level"),
                     character.get("title_stats").get("atk_level"),
                     character.get("tome").get("stats").get("atk_level")]

    result = add_valid_stats(atk_level_stats)

    return result

def calculate_def_level(character):
    def_level_stats = [character.get("weapon").get("attributes").get("def_level"),
                     character.get("head").get("stats").get("def_level"),
                     character.get("chest").get("stats").get("def_level"),
                     character.get("legs").get("stats").get("def_level"),
                     character.get("feet").get("stats").get("def_level"),
                     character.get("arms").get("stats").get("def_level"),
                     character.get("robe").get("stats").get("def_level"),
                     character.get("belt").get("stats").get("def_level"),
                     character.get("necklace").get("stats").get("def_level"),
                     character.get("ring_1").get("stats").get("def_level"),
                     character.get("ring_2").get("stats").get("def_level"),
                     character.get("set_bonus").get("def_level"),
                     character.get("constellation").get("def_level_1"),
                     character.get("constellation").get("def_level_2"),
                     character.get("constellation").get("def_level_3"),
                     character.get("constellation").get("def_level_4"),
                     character.get("constellation").get("def_level_5"),
                     character.get("constellation").get("def_level_6"),
                     character.get("constellation").get("def_level_7"),
                     character.get("glyph_1").get("def_level"),
                     character.get("glyph_2").get("def_level"),
                     character.get("glyph_3").get("def_level"),
                     character.get("glyph_4").get("def_level"),
                     character.get("glyph_5").get("def_level"),
                     character.get("glyph_6").get("def_level"),
                     character.get("meridian").get("def_level"),
                     character.get("title_stats").get("def_level"),
                     character.get("tome").get("stats").get("def_level")]

    result = add_valid_stats(def_level_stats)

    return result

def calculate_spirit(character):
    constellation_spirit = 0
    def_orbs = 0

    if all(character.get("constellation").get(f"mag_def_{i}") > 0 for i in range(1, 8)):
        constellation_spirit = constellation_spirit + 100

    for i in range(1, 8):
        if character.get("constellation").get(f"atk_level_{i}") > 0:
            def_orbs += 1

    for i in range(1, 8):
        if character.get("constellation").get(f"def_level_{i}") > 0:
            def_orbs += 1

    if def_orbs == 7:
        constellation_spirit = constellation_spirit + 100


    spirit_stats = [character.get("weapon").get("attributes").get("spirit"),
                     character.get("head").get("stats").get("spirit"),
                     character.get("chest").get("stats").get("spirit"),
                     character.get("legs").get("stats").get("spirit"),
                     character.get("feet").get("stats").get("spirit"),
                     character.get("arms").get("stats").get("spirit"),
                     character.get("robe").get("stats").get("spirit"),
                     character.get("belt").get("stats").get("spirit"),
                     character.get("necklace").get("stats").get("spirit"),
                     character.get("ring_1").get("stats").get("spirit"),
                     character.get("ring_2").get("stats").get("spirit"),
                     character.get("set_bonus").get("spirit"),
                     character.get("tome").get("stats").get("spirit"),
                    constellation_spirit]

    result = add_valid_stats(spirit_stats)

    return result


def calculate_slaying_level(character):
    slaying_level_stats = [character.get("weapon").get("attributes").get("slaying_level"),
                     character.get("head").get("stats").get("slaying_level"),
                     character.get("chest").get("stats").get("slaying_level"),
                     character.get("legs").get("stats").get("slaying_level"),
                     character.get("feet").get("stats").get("slaying_level"),
                     character.get("arms").get("stats").get("slaying_level"),
                     character.get("robe").get("stats").get("slaying_level"),
                     character.get("belt").get("stats").get("slaying_level"),
                     character.get("necklace").get("stats").get("slaying_level"),
                     character.get("ring_1").get("stats").get("slaying_level"),
                     character.get("ring_2").get("stats").get("slaying_level"),
                     character.get("set_bonus").get("slaying_level"),
                     character.get("tome").get("stats").get("slaying_level")]

    result = add_valid_stats(slaying_level_stats)

    return result

def calculate_warding_level(character):
    warding_level_stats = [character.get("weapon").get("attributes").get("warding_level"),
                     character.get("head").get("stats").get("warding_level"),
                     character.get("chest").get("stats").get("warding_level"),
                     character.get("legs").get("stats").get("warding_level"),
                     character.get("feet").get("stats").get("warding_level"),
                     character.get("arms").get("stats").get("warding_level"),
                     character.get("robe").get("stats").get("warding_level"),
                     character.get("belt").get("stats").get("warding_level"),
                     character.get("necklace").get("stats").get("warding_level"),
                     character.get("ring_1").get("stats").get("warding_level"),
                     character.get("ring_2").get("stats").get("warding_level"),
                     character.get("set_bonus").get("warding_level"),
                     character.get("tome").get("stats").get("warding_level")]

    result = add_valid_stats(warding_level_stats)

    return result

def calculate_phys_penetration(character):
    phys_penetration_stats = [character.get("weapon").get("attributes").get("phys_penetration"),
                     character.get("head").get("stats").get("phys_penetration"),
                     character.get("chest").get("stats").get("phys_penetration"),
                     character.get("legs").get("stats").get("phys_penetration"),
                     character.get("feet").get("stats").get("phys_penetration"),
                     character.get("arms").get("stats").get("phys_penetration"),
                     character.get("robe").get("stats").get("phys_penetration"),
                     character.get("belt").get("stats").get("phys_penetration"),
                     character.get("necklace").get("stats").get("phys_penetration"),
                     character.get("ring_1").get("stats").get("phys_penetration"),
                     character.get("ring_2").get("stats").get("phys_penetration"),
                     character.get("set_bonus").get("phys_penetration"),
                     character.get("tome").get("stats").get("phys_penetration")]

    result = add_valid_stats(phys_penetration_stats)

    return result

def calculate_mag_penetration(character):
    mag_penetration_stats = [character.get("weapon").get("attributes").get("mag_penetration"),
                     character.get("head").get("stats").get("mag_penetration"),
                     character.get("chest").get("stats").get("mag_penetration"),
                     character.get("legs").get("stats").get("mag_penetration"),
                     character.get("feet").get("stats").get("mag_penetration"),
                     character.get("arms").get("stats").get("mag_penetration"),
                     character.get("robe").get("stats").get("mag_penetration"),
                     character.get("belt").get("stats").get("mag_penetration"),
                     character.get("necklace").get("stats").get("mag_penetration"),
                     character.get("ring_1").get("stats").get("mag_penetration"),
                     character.get("ring_2").get("stats").get("mag_penetration"),
                     character.get("set_bonus").get("mag_penetration"),
                     character.get("tome").get("stats").get("mag_penetration")]

    result = add_valid_stats(mag_penetration_stats)

    return result

def calculate_soulforce(character):
    soulforce_stats = [character.get("weapon").get("attributes").get("soulforce"),
                     character.get("head").get("stats").get("soulforce"),
                     character.get("chest").get("stats").get("soulforce"),
                     character.get("legs").get("stats").get("soulforce"),
                     character.get("feet").get("stats").get("soulforce"),
                     character.get("arms").get("stats").get("soulforce"),
                     character.get("robe").get("stats").get("soulforce"),
                     character.get("belt").get("stats").get("soulforce"),
                     character.get("necklace").get("stats").get("soulforce"),
                     character.get("ring_1").get("stats").get("soulforce"),
                     character.get("ring_2").get("stats").get("soulforce"),
                     character.get("set_bonus").get("soulforce"),
                     character.get("tome").get("stats").get("soulforce")]

    result = add_valid_stats(soulforce_stats)

    return result

