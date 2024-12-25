import sqlite3

database = 'calc_db'
create_table = """CREATE TABLE IF NOT EXISTS boundary (
            id INTEGER PRIMARY KEY, 
            name TEXT NOT NULL, 
            '1' INTEGER NOT NULL,
            '2' INTEGER NOT NULL,
            '3' INTEGER NOT NULL,
            '4' INTEGER NOT NULL,
            '5' INTEGER NOT NULL,
            '6' INTEGER NOT NULL,
            '7' INTEGER NOT NULL,
            '8' INTEGER NOT NULL,
            '9' INTEGER NOT NULL,
            '10' INTEGER NOT NULL
        );"""
sql = ''' INSERT INTO boundary(name, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
              VALUES(?,?,?,?,?,?,?,?,?,?,?) '''

a = ('Arcane Sky', 10, 12, 15, 19, 24, 30, 37, 45, 54, 64)
b = ('Mirage Sky', 75, 87, 100, 114, 129, 145, 162, 180, 199, 219)
c = ('Astral Sky', 240, 262, 285, 309, 334, 360, 387, 415, 444, 474)
d = ('Shifting Sky', 505, 537, 570, 604, 639, 675, 712, 750, 789, 829)

data = [a, b, c, d]

try:
	with sqlite3.connect(database) as conn:
		cursor = conn.cursor()
		cursor.execute(create_table)
		conn.commit
		for c in data:
			cursor.execute(sql, c)
		conn.commit
		cursor.execute('SELECT * FROM boundary')
		rows = cursor.fetchall()
		for row in rows:
			print(row)

except sqlite3.OperationalError as e:
	print(e)
