import tkinter as tk
from tkinter import ttk
import sqlite3

# Database
conn = sqlite3.connect("gym.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS members(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age INTEGER,
phone TEXT,
membership TEXT
)
""")
conn.commit()

# Add Member
def add_member():
    cursor.execute(
        "INSERT INTO members(name,age,phone,membership) VALUES(?,?,?,?)",
        (name_var.get(), age_var.get(), phone_var.get(), member_var.get())
    )
    conn.commit()
    view_members()
    clear()

# View Members
def view_members():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM members")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)

# Delete Member
def delete_member():
    selected = tree.focus()
    values = tree.item(selected, "values")

    if values:
        cursor.execute("DELETE FROM members WHERE id=?", (values[0],))
        conn.commit()
        view_members()

# Search Member
def search_member():
    name = name_var.get()

    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM members WHERE name=?", (name,))
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)

# Clear fields
def clear():
    name_var.set("")
    age_var.set("")
    phone_var.set("")
    member_var.set("")

# Window
root = tk.Tk()
root.title("Gym Management System")
root.geometry("650x500")

title = tk.Label(root, text="Gym Management System", font=("Arial",20))
title.pack(pady=10)

# Variables
name_var = tk.StringVar()
age_var = tk.StringVar()
phone_var = tk.StringVar()
member_var = tk.StringVar()

# Form
frame = tk.Frame(root)
frame.pack()

tk.Label(frame,text="Name").grid(row=0,column=0)
tk.Entry(frame,textvariable=name_var).grid(row=0,column=1)

tk.Label(frame,text="Age").grid(row=1,column=0)
tk.Entry(frame,textvariable=age_var).grid(row=1,column=1)

tk.Label(frame,text="Phone").grid(row=2,column=0)
tk.Entry(frame,textvariable=phone_var).grid(row=2,column=1)

tk.Label(frame,text="Membership").grid(row=3,column=0)
tk.Entry(frame,textvariable=member_var).grid(row=3,column=1)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame,text="Add",width=12,command=add_member).grid(row=0,column=0,padx=5)
tk.Button(btn_frame,text="View",width=12,command=view_members).grid(row=0,column=1,padx=5)
tk.Button(btn_frame,text="Delete",width=12,command=delete_member).grid(row=0,column=2,padx=5)
tk.Button(btn_frame,text="Search",width=12,command=search_member).grid(row=0,column=3,padx=5)

# Table
tree = ttk.Treeview(root, columns=("ID","Name","Age","Phone","Membership"), show="headings")

tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("Phone", text="Phone")
tree.heading("Membership", text="Membership")

tree.pack(fill="both", expand=True)

view_members()

root.mainloop()