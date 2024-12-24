class Character:
    def __init__(self, char_class, level, past_life_1, past_life_2, ability_points, vitality, strength, dexterity, magic, hp, mana,
                 atk, phys_def, mag_def, atk_rate, speed, accuracy, evasion, crit_rate,
                 atk_level, def_level, spirit, soulforce, stealth_level, detection_level, slaying_level, warding_level,
                 phys_penetration, mag_penetration, casting_time, reputation):
        self.char_class = char_class
        self.level = level
        self.past_life_1 = past_life_1
        self.past_life_2 = past_life_2
        self.ability_points = ability_points
        self.vitality = vitality
        self.strength = strength
        self.dexterity = dexterity
        self.magic = magic
        self.hp = hp
        self.mana = mana
        self.atk = atk
        self.phys_def = phys_def
        self.mag_def = mag_def
        self.atk_rate = atk_rate
        self.speed = speed
        self.accuracy = accuracy
        self.evasion = evasion
        self.crit_rate = crit_rate
        self.atk_level = atk_level
        self.def_level = def_level
        self.spirit = spirit
        self.soulforce = soulforce
        self.stealth_level = stealth_level
        self.detection_level = detection_level
        self.slaying_level = slaying_level
        self.warding_level = warding_level
        self.phys_penetration = phys_penetration
        self.mag_penetration = mag_penetration
        self.casting_time = casting_time
        self.reputation = reputation