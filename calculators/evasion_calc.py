import sqlite3

database = "../data/calc_db"


def current_hp(level, char_class, vit, buff_total, equip_hp, equip_perc_increase):
	try:
		with sqlite3.connect(database) as conn:	
			cursor = conn.cursor()
			cursor.execute('SELECT * FROM classes WHERE name = ?', (char_class,))
			class_data = cursor.fetchone()
			base_hp = class_data[3]
			hp_per_vit = class_data[7]
			hp_per_level = class_data[8]
			
			unbuffed_hp = base_hp + equip_hp + (level*hp_per_level) + (vit*hp_per_vit)
			buffed_hp = round(unbuffed_hp * (1+ buff_total + equip_perc_increase))
			print(buffed_hp)
			return buffed_hp

	except sqlite3.OperationalError as e:
		print(e)
		
		
current_hp(105, "Barbarian", 1050, 0.35, 0, 0.05)
