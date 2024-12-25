import sqlite3

from calculators.stat_point_calc import calculate_soulforce

database = "data/calc_db"


def calc_soulforce(character):
    soulforce_items = [(character.get("weapon").get("gear_type"), character.get("weapon").get("refine")),
                        (character.get("head").get("gear_type"), character.get("head").get("refine")),
                        (character.get("chest").get("gear_type"), character.get("chest").get("refine")),
                        (character.get("legs").get("gear_type"), character.get("legs").get("refine")),
                          (character.get("feet").get("gear_type"), character.get("feet").get("refine")),
                           (character.get("arms").get("gear_type"), character.get("arms").get("refine")),
                           (character.get("robe").get("gear_type"), character.get("robe").get("refine")),
                           (character.get("belt").get("gear_type"), character.get("belt").get("refine")),
                           (character.get("necklace").get("gear_type"), character.get("necklace").get("refine")),
                           (character.get("ring_1").get("gear_type"), character.get("ring_1").get("refine")),
                           (character.get("ring_2").get("gear_type"), character.get("ring_2").get("refine")),
                           (character.get("tome").get("gear_type"), character.get("tome").get("refine"))]

    refine_soulforce = 0
    gear_soulforce = calculate_soulforce(character)

    try:
        with sqlite3.connect(database) as conn:
            cursor = conn.cursor()
            for item in soulforce_items:
                if item[1] is not None:
                    cursor.execute('SELECT * FROM soulforce WHERE gear_type = ?', (item[0],))
                    data = cursor.fetchone()
                    print(item[1])
                    print(data)
                    refine_soulforce = refine_soulforce + data[item[1]+2]
                    print(refine_soulforce)


    except sqlite3.OperationalError as e:
        print(e)

    print("total="+str(refine_soulforce))

    total_soulforce = (50 + character.get("level")) * character.get("level") + refine_soulforce + gear_soulforce

    return total_soulforce



