import sqlite3

database = "../data/calc_dbb"


def current_hp(level, char_class, vit, buff_total, equip_hp, equip_perc_increase):
	try:
		with sqlite3.connect(database) as conn:	
			cursor = conn.cursor()
			cursor.execute('SELECT * FROM classes WHERE name = ?', (char_class,))
			class_data = cursor.fetchone()
			base_hp = class_data[3]
			hp_per_vit = class_data[7]
			hp_per_level = class_data[8]
			
			unbuffed_hp = base_hp + equip_hp + ((level-1)*hp_per_level) + ((vit-5)*hp_per_vit)
			buffed_hp = round(unbuffed_hp * (1+ buff_total + equip_perc_increase))
			return buffed_hp

	except sqlite3.OperationalError as e:
		print(e)
		
		
current_hp(105, "Barbarian", 1115, 1.15, (19253+1584), 0.15)

#buff 70 (40 beast king) 15 equip 15 passive 10 105 pill
#hp 19253 (18980 + 273)
#52764 expected unbuffed
#glyps 1556
#need all passives plus 4 lvl 7 and 2 lvl 8 glyphs for 100k hp or (1584 1736) 152 hp base from somewhere (merid 47)
