import sqlite3

database = 'data/calc_db'
create_table = """CREATE TABLE IF NOT EXISTS classes (
            id INTEGER PRIMARY KEY, 
            name TEXT NOT NULL, 
            speed REAL NOT NULL,
            hp_init INTEGER NOT NULL,
            mana_init INTEGER NOT NULL,
            acc_init INTEGER NOT NULL,
            eva_init INTEGER NOT NULL,
            hp_vit INTEGER NOT NULL,
            hp_level INTEGER NOT NULL,
            mana_mag INTEGER NOT NULL,
            mana_level INTEGER NOT NULL,
            acc_dex INTEGER NOT NULL,
            eva_dex INTEGER NOT NULL
        );"""
sql = ''' INSERT INTO classes(name, speed, hp_init, mana_init,	acc_init,	eva_init, hp_vit,	hp_level, mana_mag,	mana_level,	acc_dex, eva_dex)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?) '''

archer = ('Archer', 5.2, 65, 55, 40, 30, 13, 26, 11, 22, 8, 6)
assassin = ('Assassin', 5.2, 65, 50, 40, 30, 13, 26, 11, 22, 8, 6)
barbarian = ('Barbarian', 4.9, 85, 35, 40, 40, 17, 34, 7, 14, 8, 8)
blademaster = ('Blademaster', 5.0, 75, 45, 50, 50, 15, 30, 9, 18, 10, 10)
cleric = ('Cleric', 4.8, 50, 70, 25, 10, 10, 20, 14, 28, 5, 2)
duskblade = ('Cleric', 4.8, 65, 55, 40, 30, 13, 26, 11, 22, 8, 6)
edgerunner = ('Edgerunner', 5.0, 75, 45, 50, 50, 15, 30, 9, 18, 10, 10)
mystic = ('Mystic', 4.8, 50, 70, 25, 10, 10, 20, 14, 28, 5, 2)
psychic = ('Psychic', 4.8, 50, 70, 25, 10, 10, 20, 14, 28, 5, 2)
seeker = ('Seeker', 5.0, 75, 45, 50, 50, 15, 30, 9, 18, 10, 10)
stormbringer = ('Stormbringer', 4.8, 50, 70, 25, 10, 10, 20, 14, 28, 5, 2)
technician = ('Technician', 5.2, 65, 55, 40, 30, 13, 26, 11, 22, 8, 6)
venomancer = ('Venomancer', 5.1, 60, 60, 35, 30, 12, 24, 12, 24, 7, 6)
wizard = ('Wizard', 4.8, 50, 70, 25, 10, 10, 20, 14, 28, 5, 0)

classes_data = [archer, assassin, barbarian, blademaster, cleric, duskblade, edgerunner, mystic, psychic, seeker, stormbringer, technician, venomancer, wizard]

try:
	with sqlite3.connect(database) as conn:	
		cursor = conn.cursor()
		cursor.execute(create_table)
		conn.commit
		for c in classes_data:
			cursor.execute(sql, c)
		conn.commit
		cursor.execute('SELECT * FROM classes')
		rows = cursor.fetchall()
		for row in rows:
			print(row)

except sqlite3.OperationalError as e:
	print(e)

