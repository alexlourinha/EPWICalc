import sqlite3

from calculators.stat_point_calc import calculate_dex, calculate_equip_acc_perc, calculate_equip_acc

database = "data/calc_db"


def calc_accuracy(character):
	try:
		with sqlite3.connect(database) as conn:	
			cursor = conn.cursor()
			cursor.execute('SELECT * FROM classes WHERE name = ?', (character.get("char_class"),))
			class_data = cursor.fetchone()
			base_acc = class_data[5]
			acc_per_dex = class_data[11]
			buff_total = 0
			equip_increase = calculate_equip_acc(character)
			equip_perc_increase = calculate_equip_acc_perc(character)

			dex = calculate_dex(character)

			unbuffed_acc = base_acc + ((dex -5) * acc_per_dex) + equip_increase
			modifier = 1 +  buff_total + equip_perc_increase
			buffed_acc = round(unbuffed_acc * modifier)

			return buffed_acc

	except sqlite3.OperationalError as e:
		print(e)
