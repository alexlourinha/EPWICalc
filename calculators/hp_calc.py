import sqlite3

from calculators.stat_point_calc import calculate_vit, calculate_hp_equip_stat, calculate_max_hp

database = "data/calc_db"

def calculate_hp(character):

	total_vit = calculate_vit(character)
	equip_hp = calculate_hp_equip_stat(character)
	max_hp = calculate_max_hp(character)
	total_hp_buff = 0
	level=character.get("level")
	char_class=character.get("char_class")
	vit=total_vit

	if any("Beast King's Inspiration - Sage" in x for x in character.get("active_buffs")):
		total_hp_buff =  + 0.40
	if any("Passive HP 3" in x for x in character.get("active_buffs")):
		total_hp_buff = total_hp_buff + 0.15
	if any("Tiger Form - Sage" in x for x in character.get("active_buffs")):
		total_hp_buff = total_hp_buff + 0.40
	if any("Copper Paperweight" in x for x in character.get("active_buffs")):
		total_hp_buff = total_hp_buff + 0.10

	buff_total=round(total_hp_buff, 2)
	equip_hp=equip_hp
	equip_perc_increase=round(max_hp, 2)

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
			return buffed_hp, vit

	except sqlite3.OperationalError as e:
		print(e)
