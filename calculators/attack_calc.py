import sqlite3

from calculators.mastery_buff_calc import mastery_calc
from calculators.stat_point_calc import phys_atk_total_excl_weapon, mag_atk_total_excl_weapon, calculate_str, \
	calculate_dex, calculate_mag

database = 'data/calc_db'

def calculate_base_damage(attack_multiplier, weapon_attack):
	min_phys_atk = round(attack_multiplier[0] * weapon_attack["phys_atk"][0])
	max_phys_atk = round(attack_multiplier[0] * weapon_attack["phys_atk"][1])
	min_mag_atk = round(attack_multiplier[1] * weapon_attack["mag_atk"][0])
	max_mag_atk = round(attack_multiplier[1] * weapon_attack["mag_atk"][1])
	return {"phys_atk": [min_phys_atk, max_phys_atk], "mag_atk": [min_mag_atk, max_mag_atk]}
		
def calculate_attack_multiplier(weapon, dex, mag, strength, mastery, phys_attack_buff, mag_attack_buff):
	phys_multiplier = 0.00
	mag_multiplier = 0.00
	if weapon.get("type") == "ranged" or weapon.get("type") == "daggers":
		phys_multiplier = round(1+(dex/150)+mastery+phys_attack_buff, 2)
		mag_multiplier = round(1 + (mag / 100) + mag_attack_buff, 2)
	elif weapon.get("type") == "melee" or weapon.get("type") == "magic":
		phys_multiplier = round(1 + (strength / 150) + mastery + phys_attack_buff, 2)
		mag_multiplier = round(1 + (mag / 100) + mag_attack_buff, 2)
	else:
		print("invalid weapon type")
	return [phys_multiplier, mag_multiplier]
		
def calculate_weapon_attack(weapon, phys_atk_equip, mag_atk_equip, level):
	if weapon.get("type") != "magic":
		min_phys_atk = weapon.get("phys_atk_min") + phys_atk_equip + level
		max_phys_atk = weapon.get("phys_atk_max") + phys_atk_equip + level
		min_mag_atk = weapon.get("mag_atk_min") + mag_atk_equip + 1
		max_mag_atk = weapon.get("mag_atk_max") + mag_atk_equip + 1
	else:
		min_phys_atk = weapon.get("phys_atk_min") + phys_atk_equip
		max_phys_atk = weapon.get("phys_atk_max") + phys_atk_equip
		min_mag_atk = weapon.get("mag_atk_min") + mag_atk_equip + level
		max_mag_atk = weapon.get("mag_atk_max") + mag_atk_equip + level

	phys_atk = [min_phys_atk, max_phys_atk]
	mag_atk = [min_mag_atk, max_mag_atk]
	result = {"phys_atk": phys_atk, "mag_atk": mag_atk}
	return  result


def calculate_attack(character):
	weapon = character.get("weapon")
	mastery = mastery_calc(character)

	phys_atk_total = phys_atk_total_excl_weapon(character)
	mag_atk_total = mag_atk_total_excl_weapon(character)

	phys_attack_buff = 0
	mag_attack_buff = 0


	if any("Copper Paperweight" in x for x in character.get("active_buffs")):
		phys_attack_buff = phys_attack_buff + 0.40
		mag_attack_buff = mag_attack_buff + 0.40
	if any("Strength of the Titans" in x for x in character.get("active_buffs")):
		phys_attack_buff = phys_attack_buff + 0.50

	str_stat = calculate_str(character)
	dex_stat = calculate_dex(character)
	mag_stat = calculate_mag(character)

	multiplier = calculate_attack_multiplier(weapon,
											 dex_stat,
											 mag_stat,
											 str_stat,
											 mastery,
											 phys_attack_buff,
											 mag_attack_buff)
	weapon_atk = calculate_weapon_attack(weapon, phys_atk_total, mag_atk_total, 105)
	result = calculate_base_damage(multiplier, weapon_atk)
	return result
		
