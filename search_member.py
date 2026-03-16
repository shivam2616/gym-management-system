import sqlite3

name = input("Enter Member Name to search: ")

conn = sqlite3.connect("gym.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM members WHERE name=?", (name,))
result = cursor.fetchall()

for r in result:
    print(r)

conn.close()

input("Press Enter to continue...")