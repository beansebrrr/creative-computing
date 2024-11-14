"""
Using SQLite3
"""

import sqlite3
metadb = sqlite3.connect("C://Code//creative-computing//introduction-to-programming//week-8//metaverse.db")


def main():
    print("""+---+ Database Viewer +---+  
C: Create
R: Read
U: Update
D: Delete
E: Exit
    """)

    while True:
        match input(">>> ").upper():
            case 'C':
                print("+ Create +")
                while True:
                    create()
                    if get_bool("Would you like to add more? ") == False:
                        print("Left the Create menu.\n")
                        break   
            case 'R':
                print("? Read ?")
            case 'U':
                print("! Update !")
            case 'D':
                print("- Delete -")
            case 'E':
                print("Exited.\n")
                break
            case _:
                pass


def create():
    name = input("What's your name? ")
    age = get_int("How old are you? ")
    location = input("Where are you from? ")

    metadb.execute("INSERT INTO students(name, age, location) values(?, ?, ?)", (name, age, location))
    metadb.commit()
    print("\nEntry successful!")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


def get_bool(prompt):
    while True:
        _ = input(prompt).lower()
        if _ in ["y", "yes", "true"]:
            return True
        elif _ in ["n", "no", "false"]:
            return False


main()