class Weapon:
	def __init__(self, name, weapon_type,atk_rate, weapon_range, req_class, req_str, req_dex, req_mag, req_rep,
				 mag_atk_min, mag_atk_max, phys_atk_min, phys_atk_max, attributes):
		self.name = name
		self.weapon_type = weapon_type
		self.atk_rate = atk_rate
		self.weapon_range = weapon_range
		self.req_class = req_class
		self.req_str = req_str
		self.req_dex = req_dex
		self.req_mag = req_mag
		self.req_rep = req_rep
		self.mag_atk_min = mag_atk_min
		self.mag_atk_max = mag_atk_max
		self.phys_atk_min = phys_atk_min
		self.phys_atk_max = phys_atk_max
		self.attributes = attributes
