import sqlite3

from calculators.stat_point_calc import calculate_equip_speed

database = "data/calc_db"


def calculate_speed(character):
    try:
        with sqlite3.connect(database) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM classes WHERE name = ?', (character.get("char_class"),))
            class_data = cursor.fetchone()
            base_speed = class_data[2]

            buff_speed = 1
            equip_speed = calculate_equip_speed(character)

            if any("Tiger Form - Sage" in x for x in character.get("active_buffs")):
                buff_speed = buff_speed + 0.9

            print(base_speed, equip_speed, buff_speed)

            buffed_base_speed = base_speed * buff_speed
            total_speed = round(buffed_base_speed + equip_speed, 1)
            return total_speed

    except sqlite3.OperationalError as e:
        print(e)
