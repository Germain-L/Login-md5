import sqlite3
import hashlib
conn = sqlite3.connect("logins.db")	
c = conn.cursor()


def check(u,p):
	hu = str(hashlib.md5(u.encode()).hexdigest())
	hp = str(hashlib.md5(p.encode()).hexdigest())

	c.execute("SELECT * FROM logins WHERE Username=? AND Password=?", (hu, hp))
	rows = c.fetchall()
	if rows == []:
		return False
	else:
		return True


def newEntry(NewU, NewP):
	newhu = str(hashlib.md5(NewU.encode()).hexdigest())
	newhp = str(hashlib.md5(NewP.encode()).hexdigest())
	c.execute("INSERT INTO logins VALUES(?,?)", (newhu, newhp))
	conn.commit()