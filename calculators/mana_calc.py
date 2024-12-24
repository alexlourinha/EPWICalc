import sqlite3

database = "data/calc_db"


def calculate_mana(level, char_class, mag, buff_total, equip_mana, equip_perc_increase):
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
			return buffed_mana

	except sqlite3.OperationalError as e:
		print(e)
