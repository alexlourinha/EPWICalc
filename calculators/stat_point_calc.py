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

