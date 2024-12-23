import sqlite3
from classes.weapon import *

database = '../data/calc_db'

try:
	with sqlite3.connect(database) as conn:	
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM classes')
		rows = cursor.fetchall()
		for row in rows:
			print(row)

except sqlite3.OperationalError as e:
	print(e)

weap = Weapon("test", "STR", 1, 1, 1738, 3262, [])
	
def calculate_base_damage(attack_multiplier, weapon_attack):
	min_atk = round(attack_multiplier*weapon_attack["min_atk"])
	max_atk = round(attack_multiplier*weapon_attack["max_atk"])
	return (min_atk, max_atk)
		
def calculate_attack_multiplier(weapon, dex, mag, str, mastery, phys_attack_buff, mag_attack_buff):
	if weapon.type == "DEX":
		return round(1+(dex/150)+mastery+phys_attack_buff, 2)
	elif weapon.type == "STR":
		return round(1+(str/150)+mastery+phys_attack_buff, 2)
	elif weapon.type == "MAG":
		return round(1+(mag/100)+mag_attack_buff, 2)
	else:
		print("invalid weapon type")
		
def calculate_weapon_attack(weapon, phys_atk_equip, mag_atk_equip, meridian_phys_atk, meridian_mag_atk, glyphs_atk, level):
	if weapon.type == "DEX" or weapon.type == "STR":
		min_atk = weapon.phys_atk_min+phys_atk_equip+meridian_phys_atk+glyphs_atk+level
		max_atk = weapon.phys_atk_max+phys_atk_equip+meridian_phys_atk+glyphs_atk+level
		result = {"min_atk":min_atk, "max_atk":max_atk}
		print(result)
		return (result)
	elif weapon.type == "MAG":
		min_atk = weapon.mag_atk_min+mag_atk_equip+meridian_mag_atk+glyphs_atk+level
		max_atk = weapon.mag_atk_max+mag_atk_equip+meridian_mag_atk+glyphs_atk+level
		result = {"min_atk":min_atk, "max_atk":max_atk}
		print(result)
		return (result)
	else:
		print("invalid weapon type")
	return 
	


multiplier = calculate_attack_multiplier(weap, 75, 60, 320, 1.0, 0, 0)
weap_atk = calculate_weapon_attack(weap, 525, 0, 62, 0, 0, 105)
result = calculate_base_damage(multiplier, weap_atk)
print(result)
		
