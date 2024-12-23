from calculators.hp_calc import calculate_hp

def add_valid_stats(stats):
    result = 0
    for stat in stats :
        if stat is not None:
            result = result + stat
    return result



def calculate_character_hp(char):

    total_hp_buff = 0
    constellation_hp_buff = 0

    if all(char.get("constellation").get(f"phys_def_{i}") > 0 for i in range(1, 8)):
        constellation_hp_buff = 0.05

    equip_hp_stats = [char.get("weapon").get("attributes").get("hp"),
                char.get("head").get("stats").get("hp"),
                char.get("chest").get("stats").get("hp"),
                char.get("legs").get("stats").get("hp"),
                char.get("feet").get("stats").get("hp"),
                char.get("arms").get("stats").get("hp"),
                char.get("robe").get("stats").get("hp"),
                char.get("belt").get("stats").get("hp"),
                char.get("necklace").get("stats").get("hp"),
                char.get("ring_1").get("stats").get("hp"),
                char.get("ring_2").get("stats").get("hp"),
                char.get("constellation").get("hp_1"),
                char.get("constellation").get("hp_2"),
                char.get("constellation").get("hp_3"),
                char.get("constellation").get("hp_4"),
                char.get("constellation").get("hp_5"),
                char.get("constellation").get("hp_6"),
                char.get("constellation").get("hp_7"),
                char.get("glyph_1").get("hp"),
                char.get("glyph_2").get("hp"),
                char.get("glyph_3").get("hp"),
                char.get("glyph_4").get("hp"),
                char.get("glyph_5").get("hp"),
                char.get("glyph_6").get("hp"),
                char.get("meridian").get("hp"),
                char.get("tome").get("stats").get("hp")]
    max_hp_stats = [char.get("weapon").get("attributes").get("max_hp"),
              char.get("head").get("stats").get("max_hp"),
              char.get("chest").get("stats").get("max_hp"),
              char.get("legs").get("stats").get("max_hp"),
              char.get("feet").get("stats").get("max_hp"),
              char.get("arms").get("stats").get("max_hp"),
              char.get("robe").get("stats").get("max_hp"),
              char.get("belt").get("stats").get("max_hp"),
              char.get("necklace").get("stats").get("max_hp"),
              char.get("ring_1").get("stats").get("max_hp"),
              char.get("ring_2").get("stats").get("max_hp"),
              constellation_hp_buff]
    vit_stats = [char.get("vitality"),
                 char.get("weapon").get("attributes").get("vitality"),
                 char.get("head").get("stats").get("vitality"),
                 char.get("chest").get("stats").get("vitality"),
                 char.get("legs").get("stats").get("vitality"),
                 char.get("feet").get("stats").get("vitality"),
                 char.get("arms").get("stats").get("vitality"),
                 char.get("robe").get("stats").get("vitality"),
                 char.get("belt").get("stats").get("vitality"),
                 char.get("necklace").get("stats").get("vitality"),
                 char.get("ring_1").get("stats").get("vitality"),
                 char.get("ring_2").get("stats").get("vitality"),
                 char.get("tome").get("stats").get("vitality")]


    total_vit = add_valid_stats(vit_stats)

    equip_hp = add_valid_stats(equip_hp_stats)

    max_hp = add_valid_stats(max_hp_stats)

    if any("Beast King's Inspiration - Sage" in x for x in char.get("active_buffs")):
        total_hp_buff = total_hp_buff + 0.40
    if any("Passive HP 3" in x for x in char.get("active_buffs")):
        total_hp_buff = total_hp_buff + 0.15
    if any("Tiger Form - Sage" in x for x in char.get("active_buffs")):
        total_hp_buff = total_hp_buff + 0.40

    print(round(total_hp_buff, 2))
    print(equip_hp)
    print(round(max_hp, 2))
    print(total_vit)
    print(char.get("level"))
    print(char.get("char_class"))

    hp = calculate_hp(level=char.get("level"),
                 char_class=char.get("char_class"),
                 vit=total_vit,
                 buff_total=round(total_hp_buff, 2),
                 equip_hp=equip_hp,
                 equip_perc_increase=round(max_hp, 2))

    print(hp)

    return hp

def calculate_character_stats(char):
    hp = calculate_character_hp(char)
    return hp
