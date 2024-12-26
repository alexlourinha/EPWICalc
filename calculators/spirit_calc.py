import sqlite3

from calculators.stat_point_calc import calculate_spirit

database = "data/calc_db"


def calc_spirit(character):

    boundary_char = character.get("boundary")

    try:
        with sqlite3.connect(database) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM boundary WHERE name = ?', (boundary_char[0],))
            class_data = cursor.fetchone()
            boundary_spirit = 0
            print(boundary_char)
            if boundary_char[0] != "None":
                if boundary_char[1] != 0:
                    boundary_spirit = class_data[boundary_char[1]+1]

            equip_spirit = calculate_spirit(character)
            buff_spirit = 0

            result = equip_spirit + buff_spirit + boundary_spirit

            return result

    except sqlite3.OperationalError as e:
        print(e)

