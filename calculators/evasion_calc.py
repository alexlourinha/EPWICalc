import sqlite3

from calculators.stat_point_calc import calculate_dex, calculate_equip_evasion, calculate_equip_evasion_perc

database = "data/calc_db"


def calc_evasion(character):
	try:
		with sqlite3.connect(database) as conn:
			cursor = conn.cursor()
			cursor.execute('SELECT * FROM classes WHERE name = ?', (character.get("char_class"),))
			class_data = cursor.fetchone()
			base_evasion = class_data[6]
			evasion_per_dex = class_data[12]
			buff_total = 0
			equip_increase = calculate_equip_evasion(character)
			equip_perc_increase = calculate_equip_evasion_perc(character)

			dex = calculate_dex(character)

			unbuffed_evasion = base_evasion + ((dex -5) * evasion_per_dex) + equip_increase
			modifier = 1 +  buff_total + equip_perc_increase
			buffed_evasion = round(unbuffed_evasion * modifier)

			return buffed_evasion

	except sqlite3.OperationalError as e:
		print(e)