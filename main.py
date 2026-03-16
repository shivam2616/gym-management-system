import os

while True:
    print("\n===== Gym Management System =====")
    print("1. Add Member")
    print("2. View Members")
    print("3. Delete Member")
    print("4. Search Member")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        os.system("python add_member.py")

    elif choice == "2":
        os.system("python view_member.py")

    elif choice == "3":
        os.system("python delete_member.py")

    elif choice == "4":
        os.system("python search_member.py")

    elif choice == "5":
        print("Exiting Program")
        break

    else:
        print("Invalid Choice")