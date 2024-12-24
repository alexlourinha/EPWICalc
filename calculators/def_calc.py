from calculators.stat_point_calc import calculate_phys_def, calculate_mag_def


def calculate_def_stats(character, vit, strength, mag, total_phys_def_buff, total_mag_def_buff):

	phys_def_stats = calculate_phys_def(character)
	mag_def_stats = calculate_mag_def(character)

	phys_def = round((vit + strength - 2) / 4)
	mag_def = round((vit + mag - 2) / 4)

	phys_def_mod = 1 + round((((2 * vit) + (3 * strength)) / 25)) / 100
	mag_def_mod = 1 + round((((2 * vit) + (3 * mag)) / 25)) / 100
	phys_def_buff = total_phys_def_buff
	mag_def_buff = total_mag_def_buff

	gear__phys_def_calc = round(phys_def_stats * (phys_def_mod + phys_def_buff)) + 1
	gear_mag_def_calc = round(mag_def_stats * (mag_def_mod + mag_def_buff))

	phys_def_result = phys_def + gear__phys_def_calc + 1
	mag_def_result = mag_def + gear_mag_def_calc

	print(phys_def, phys_def_stats)

	return {"phys_def": round(phys_def_result), "mag_def": round(mag_def_result)}


#physical defense = Round{ ( Vit + Str - 2 ) / 4 } + Round{ Def * ( 1 + Round{ ( ( 2 * Vit ) + ( 3 * Str ) ) / 25 } / 100 ) } + 1
#magic resistance = Round{ ( Vit + Mag - 2 ) / 4 } + Round{ Res * ( 1 + Round{ ( ( 2 * Vit ) + ( 3 * Mag ) ) / 25 } / 100 ) }