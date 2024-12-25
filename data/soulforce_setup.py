import sqlite3

database = 'calc_db'
create_table = """CREATE TABLE IF NOT EXISTS soulforce (
            id INTEGER PRIMARY KEY, 
            gear TEXT NOT NULL, 
            '0' INTEGER NOT NULL,
            '1' INTEGER NOT NULL,
            '2' INTEGER NOT NULL,
            '3' INTEGER NOT NULL,
            '4' INTEGER NOT NULL,
            '5' INTEGER NOT NULL,
            '6' INTEGER NOT NULL,
            '7' INTEGER NOT NULL,
            '8' INTEGER NOT NULL,
            '9' INTEGER NOT NULL,
            '10' INTEGER NOT NULL,
            '11' INTEGER NOT NULL,
            '12' INTEGER NOT NULL
        );"""
sql = ''' INSERT INTO soulforce(gear_type,'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''

a = ('armor', 0, 1, 2, 4, 10, 25, 58, 111, 213, 400, 743, 1374, 2535)
b = ('tome', 0, 1, 2, 4, 10, 25, 58, 111, 213, 400, 743, 1374, 2535)
c = ('ornament', 0, 1, 2, 4, 10, 25, 58, 111, 213, 400, 743, 1374, 2535)
d = ('weapon', 0, 1, 7, 23, 60, 150, 345, 667, 1275, 2400, 4455, 8242, 15210)

data = [a, b, c, d]

try:
	with sqlite3.connect(database) as conn:
		cursor = conn.cursor()
		cursor.execute(create_table)
		conn.commit
		for c in data:
			cursor.execute(sql, c)
		conn.commit
		cursor.execute('SELECT * FROM soulforce')
		rows = cursor.fetchall()
		for row in rows:
			print(row)

except sqlite3.OperationalError as e:
	print(e)
