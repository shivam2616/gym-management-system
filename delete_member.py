import sqlite3

member_id = input("Enter Member ID to delete: ")

conn = sqlite3.connect("gym.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM members WHERE id=?", (member_id,))

conn.commit()
conn.close()

print("Member Deleted Successfully")

input("Press Enter to continue...")