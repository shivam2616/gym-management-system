import sqlite3

name = input("Enter Member Name: ")
age = input("Enter Age: ")
phone = input("Enter Phone: ")
membership = input("Enter Membership Type: ")

conn = sqlite3.connect("gym.db")
cursor = conn.cursor()

cursor.execute(
    "INSERT INTO members(name, age, phone, membership) VALUES (?, ?, ?, ?)",
    (name, age, phone, membership)
)

conn.commit()
conn.close()

print("Member Added Successfully")
input("Press Enter to continue...")