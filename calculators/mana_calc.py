import sqlite3

from calculators.stat_point_calc import calculate_mag, calculate_mana_equip_stat, calculate_max_mana

database = "data/calc_db"


def calculate_mana(character):
	level = character.get("level")
	char_class = character.get("char_class")
	mag = calculate_mag(character)
	equip_mana = calculate_mana_equip_stat(character)
	max_mana = calculate_max_mana(character)
	total_mana_buff = 0
	buff_total = round(total_mana_buff, 2)
	equip_mana = equip_mana
	equip_perc_increase = round(max_mana, 2)
	try:
		with sqlite3.connect(database) as conn:	
			cursor = conn.cursor()
			cursor.execute('SELECT * FROM classes WHERE name = ?', (char_class,))
			class_data = cursor.fetchone()
			base_mana = class_data[4]
			mana_per_mag = class_data[9]
			mana_per_level = class_data[10]
			
			unbuffed_mana = base_mana + equip_mana + ((level-1)*mana_per_level) + ((mag-5)*mana_per_mag)
			buffed_mana = round(unbuffed_mana * (1+ buff_total + equip_perc_increase))
			return buffed_mana, mag

	except sqlite3.OperationalError as e:
		print(e)
