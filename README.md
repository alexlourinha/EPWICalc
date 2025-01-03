# EPWICalc

## A PWI character calculator tailored for Evolved Perfect World

### Make sure to install dependencies:

#### pip install fastapi
#### pip install uvicorn

## API expected query schema:

```
{
  "char_class": "Barbarian",
  "level": 105,
  "past_life_1": 103,
  "past_life_2": 103,
  "vitality": 409,
  "strength": 200,
  "dexterity": 10,
  "magic": 5,
  "boundary": ["Shifting Sky", 10],
  "meridian": {
    "hp": 329,
    "mag_atk": 0,
    "mag_def": 94,
    "phys_atk": 75,
    "phys_def": 141
  },
  "weapon": {
    "name": "Might of the Dominator",
    "type": "melee",
    "refine": 12,
    "gear_type": "weapon",
    "atk_rate": 0.91,
    "weapon_range": 3.50,
    "req_class": "Barbarian",
    "req_str": 300,
    "req_dex": 50,
    "req_mag": 0,
    "req_rep": 300000,
    "mag_atk_min": 0,
    "mag_atk_max": 0,
    "phys_atk_min": 2180,
    "phys_atk_max": 3058,
    "attributes": {
      "def_level": 27,
      "acc_perc": 0.41,
      "magic": 17,
      "phys_def": 252,
      "vitality": 37
    }
  },
  "head": {
    "name": "Crown of Madness",
    "gear_type": "armor",
    "refine": 12,
    "requirements": [
      {
        "req_class": "",
        "req_level": 60,
        "req_str": 75,
        "req_dex": 0,
        "req_mag": 0,
        "req_rep": 0
      }
    ],
    "stats": {
      "hp": 2850,
      "mp": 600,
      "atk_level": 2,
      "def_level": 2,
      "mag_def": 200,
      "phys_def": 200,
      "speed": 0.10,
      "vitality": 48,
      "phys_atk": 150,
      "crit_rate": 1
    }
  },
  "chest": {
    "name": "Chieftain's Breastplate(PVE)",
    "gear_type": "armor",
    "refine": 12,
    "requirements": [
      {
        "req_class": "Barbarian",
        "req_level": 101,
        "req_str": 255,
        "req_dex": 55,
        "req_mag": 0,
        "req_rep": 300000
      }
    ],
    "stats": {
      "hp": 3030,
      "slaying_level": 30,
      "warding_level": 30,
      "mag_def": 1611,
      "phys_def": 2719,
      "max_hp": 0.05,
      "crit_rate": 2,
      "vitality": 63
    }
  },
  "legs": {
    "name": "Chieftain's Greaves(PVE)",
    "gear_type": "armor",
    "refine": 12,
    "requirements": [
      {
        "req_class": "Barbarian",
        "req_level": 101,
        "req_str": 255,
        "req_dex": 55,
        "req_mag": 0,
        "req_rep": 300000
      }
    ],
    "stats": {
      "hp": 3030,
      "int": -0.05,
      "slaying_level": 30,
      "warding_level": 30,
      "mag_def": 1354,
      "phys_def": 2343,
      "strength": 15,
      "crit_rate": 2,
      "vitality": 48
    }
  },
  "feet": {
    "name": "Chieftain's Boots(PVE)",
    "gear_type": "armor",
    "refine": 12,
    "requirements": [
      {
        "req_class": "Barbarian",
        "req_level": 101,
        "req_str": 255,
        "req_dex": 55,
        "req_mag": 0,
        "req_rep": 300000
      }
    ],
    "stats": {
      "hp": 3150,
      "reduce_mag_dmg": 0.05,
      "slaying_level": 30,
      "warding_level": 30,
      "mag_def": 726,
      "phys_def": 1588,
      "speed": 0.30,
      "vitality": 63
    }
  },
  "arms": {
    "name": "Chieftain's Bracers(PVE)",
    "gear_type": "armor",
    "refine": 12,
    "requirements": [
      {
        "req_class": "Barbarian",
        "req_level": 101,
        "req_str": 255,
        "req_dex": 55,
        "req_mag": 0,
        "req_rep": 300000
      }
    ],
    "stats": {
      "hp": 3150,
      "int": -0.10,
      "slaying_level": 30,
      "warding_level": 30,
      "mag_def": 570,
      "phys_def": 1213,
      "strength": 30,
      "vitality": 48
    }
  },
  "robe": {
    "name": "Wings of Ascension",
    "gear_type": "armor",
    "refine": 12,
    "requirements": [
      {
        "req_class": "",
        "req_level": 60,
        "req_str": 0,
        "req_dex": 0,
        "req_mag": 0,
        "req_rep": 0
      }
    ],
    "stats": {
      "evasion": 600,
      "hp": 1687,
      "speed": 0.20,
      "reduce_phys_dmg": 0.04,
      "mag_def": 400,
      "phys_def": 500,
      "def_level": 2,
      "vitality": 74
    }
  },
  "belt": {
    "name": "Chieftain's Pendant(PVE)",
    "gear_type": "ornament",
    "refine": 12,
    "requirements": [
      {
        "req_class": "Barbarian",
        "req_level": 101,
        "req_str": 0,
        "req_dex": 0,
        "req_mag": 0,
        "req_rep": 300000
      }
    ],
    "stats": {
      "soulforce": 1500,
      "slaying_level": 10,
      "warding_level": 10,
      "mag_def": 1935,
      "phys_def": 1935,
      "strength": 10,
      "vitality": 90
    }
  },
  "necklace": {
    "name": "Badge of the Cube: Defiance",
    "gear_type": "ornament",
    "refine": 12,
    "requirements": [
      {
        "req_class": "",
        "req_level": 80,
        "req_str": 0,
        "req_dex": 0,
        "req_mag": 0,
        "req_rep": 0
      }
    ],
    "stats": {
      "max_hp": 0.05,
      "mag_def": 2075,
      "atk_level": 5,
      "def_level": 8,
      "dexterity": 10,
      "crit_rate": 3,
      "vitality": 85
    }
  },
  "ring_1": {
    "name": "Star's Destiny",
    "gear_type": "ornament",
    "refine": 12,
    "requirements": [
      {
        "req_class": "",
        "req_level": 100,
        "req_str": 0,
        "req_dex": 0,
        "req_mag": 0,
        "req_rep": 0
      }
    ],
    "stats": {
      "phys_atk": 156,
      "phys_def": 1687,
      "acc_perc": 0.50,
      "crit_rate": 3,
      "atk_level": 5,
      "def_level": 3,
      "vitality": 20
    }
  },
  "ring_2": {
    "name": "Star's Destiny",
    "gear_type": "ornament",
    "refine": 12,
    "requirements": [
      {
        "req_class": "",
        "req_level": 100,
        "req_str": 0,
        "req_dex": 0,
        "req_mag": 0,
        "req_rep": 0
      }
    ],
    "stats": {
      "phys_atk": 156,
      "phys_def": 1687,
      "acc_perc": 0.50,
      "crit_rate": 3,
      "atk_level": 5,
      "def_level": 3,
      "vitality": 20
    }
  },
  "blessing": {
    "name": "O'Malley's Blessing",
    "requirements": [
      {
        "req_class": "",
        "req_level": 0,
        "req_str": 0,
        "req_dex": 0,
        "req_mag": 0,
        "req_rep": 0
      }
    ],
    "stats": {
      "atk_level": 15,
      "def_level": 15
    }
  },
  "tome": {
    "name": "Necronomicon",
    "gear_type": "tome",
    "requirements": [
      {
        "req_class": "",
        "req_level": 0,
        "req_str": 0,
        "req_dex": 0,
        "req_mag": 0,
        "req_rep": 0
      }
    ],
    "stats": {
      "strength": 55,
      "dexterity": 55,
      "magic": 55,
      "vitality": 45,
      "crit_rate": 5,
      "channeling": 5,
      "int": -0.05,
      "hp": 400
    }
  },
  "constellation": {
    "phys_def_1": 175,
    "phys_def_2": 62,
    "phys_def_3": 225,
    "phys_def_4": 15,
    "phys_def_5": 46,
    "phys_def_6": 42,
    "phys_def_7": 24,
    "mag_def_1": 0,
    "mag_def_2": 0,
    "mag_def_3": 0,
    "mag_def_4": 0,
    "mag_def_5": 0,
    "mag_def_6": 0,
    "mag_def_7": 0,
    "hp_1": 467,
    "hp_2": 207,
    "hp_3": 191,
    "hp_4": 198,
    "hp_5": 218,
    "hp_6": 199,
    "hp_7": 203,
    "atk_level_1": 0,
    "atk_level_2": 0,
    "atk_level_3": 0,
    "atk_level_4": 0,
    "atk_level_5": 0,
    "atk_level_6": 0,
    "atk_level_7": 0,
    "def_level_1": 0,
    "def_level_2": 0,
    "def_level_3": 0,
    "def_level_4": 0,
    "def_level_5": 0,
    "def_level_6": 0,
    "def_level_7": 0
  },
  "title_stats": {
    "accuracy": 6,
    "evasion": 0,
    "mag_atk": 12,
    "mag_def": 0,
    "phys_atk": 0,
    "phys_def": 0
  },
  "glyph_1": {
    "level": 8,
    "hp": 300,
    "spirit": 18,
    "mag_atk": 99,
    "mag_def": 432,
    "phys_atk": 99,
    "phys_def": 573,
    "atk_level": 0,
    "def_level": 0
  },
  "glyph_2": {
    "level": 6,
    "hp": 264,
    "spirit": 0,
    "mag_atk": 55,
    "mag_def": 326,
    "phys_atk": 55,
    "phys_def": 432,
    "atk_level": 0,
    "def_level": 0
  },
  "glyph_3": {
    "level": 6,
    "hp": 264,
    "spirit": 0,
    "mag_atk": 55,
    "mag_def": 326,
    "phys_atk": 55,
    "phys_def": 432,
    "atk_level": 0,
    "def_level": 0
  },
  "glyph_4": {
    "level": 6,
    "hp": 264,
    "spirit": 0,
    "mag_atk": 55,
    "mag_def": 326,
    "phys_atk": 55,
    "phys_def": 432,
    "atk_level": 0,
    "def_level": 0
  },
  "glyph_5": {
    "level": 6,
    "hp": 264,
    "spirit": 0,
    "mag_atk": 55,
    "mag_def": 326,
    "phys_atk": 55,
    "phys_def": 432,
    "atk_level": 0,
    "def_level": 0
  },
  "glyph_6": {
    "level": 6,
    "hp": 264,
    "spirit": 0,
    "mag_atk": 55,
    "mag_def": 326,
    "phys_atk": 55,
    "phys_def": 432,
    "atk_level": 0,
    "def_level": 0
  },
  "set_bonus": {
    "slaying_level": 10,
    "crit_rate": 5,
    "int": -0.05

  },
  "reputation": 300000,
  "active_buffs": [
    "Beast King's Inspiration - Sage",
    "Passive HP 3",
    "Passive Defense 8",
    "Tiger Form - Sage",
    "Axe and Hammer Mastery - Sage",
    "Copper Paperweight",
    "Strength of the Titans"
  ]
}
```

## API response schema:

```
{
  "char_class": "Barbarian",
  "level": 105,
  "past_life_1": 103,
  "past_life_2": 103,
  "ability_points": 604,
  "vitality": 1050,
  "strength": 310,
  "dexterity": 75,
  "magic": 77,
  "hp": 93093,
  "mana": 2595,
  "atk": {
    "phys_atk": [
      15884,
      20248
    ],
    "mag_atk": [
      840,
      840
    ]
  },
  "phys_def": 50465,
  "mag_def": 28620,
  "atk_rate": 1.18,
  "speed": 10.1,
  "accuracy": 1460,
  "evasion": 1200,
  "crit_rate": 28,
  "atk_level": 17,
  "def_level": 45,
  "spirit": 847,
  "soulforce": 58335,
  "stealth_level": 0,
  "detection_level": 105,
  "slaying_level": 140,
  "warding_level": 130,
  "phys_penetration": 0,
  "mag_penetration": 0,
  "casting_time": 5,
  "reputation": 300000
}
```