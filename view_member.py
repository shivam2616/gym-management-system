import sqlite3

conn = sqlite3.connect("gym.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM members")
members = cursor.fetchall()

for m in members:
    print(m)

conn.close()

input("Press Enter to continue...")