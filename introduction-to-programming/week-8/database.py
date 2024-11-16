"""
Using SQLite3
"""

import sqlite3
from prettytable import PrettyTable
metadb = sqlite3.connect("C://Code//creative-computing//introduction-to-programming//week-8//metaverse.db")
cursor = metadb.cursor()
table = PrettyTable()


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
                read()
            case 'U':
                print("! Update !")
                while True:
                    _ = get_id()
                    if _ == None:
                        break
                    update(_)
                    if get_bool("Would you like to update more? ") == False:
                        print("Left the Update menu.")
                        break
            case 'D':
                print("- Delete -")
                delete()
            case 'E':
                print("Exited.\n")
                break
            case _:
                pass


def create():
    name = input("What's your name? ")
    age = get_int("How old are you? ")
    location = input("Where are you from? ")

    metadb.execute("INSERT INTO students(name, age, location) values(?, ?, ?);", (name, age, location))
    metadb.commit()
    print("\nEntry successful!")


def read():
    cursor.execute("SELECT * FROM students;")
    rows = cursor.fetchall()
    table.field_names = [desc[0] for desc in cursor.description]
    table.add_rows(rows)
    print(table)


def update(student_id):
    bio = make_student_bio(student_id)
    print_dict(bio)

    # Which column would you like to update?
    while True:
        update_column = input("Which property you like to update? ").lower()
        if update_column in bio.keys():
            break
        print("This property does not exist.")
    
    # Updates column based on update_value
    update_value = get_update_value(bio[update_column])
    metadb.execute(f"UPDATE students SET {update_column} = ? WHERE id = ?;", (update_value, student_id))
    metadb.commit()
    print(f"\n{update_column.capitalize()} Updated Successfully!")

    # Show the newly updated student bio
    bio[update_column] = update_value
    print_dict(bio)
    

def delete():
    while True:
        student_id = get_id()
        if student_id == None:
            return
        cursor.execute("SELECT name FROM students WHERE id = ?;", str(student_id))
        student_name = cursor.fetchone()[0]

        # Show student info before asking for confirmation
        print_dict(make_student_bio(student_id))
        if get_bool(f"Are you sure you want to delete {student_name}'s entire Profile? "):
            break
    
    metadb.execute("DELETE FROM students WHERE id = ?;", str(student_id))
    metadb.commit()
    print(f"{student_name} has been removed from the database.")


# Only returns a valid id
def get_id():
    cursor.execute("SELECT id FROM students;")
    retrieve = cursor.fetchall()
    student_ids = []
    for id_no in retrieve:
        student_ids.append(id_no[0])
    # What do you want to update?
    while True:
        update_id = get_int("Please enter the student's ID (0 to exit): ")
        if update_id == 0:
            return None
        elif update_id in student_ids:
            break
        
        print(f"Student with ID {update_id} does not exist in the database.\n")
    return update_id


def make_student_bio(student_id):
    cursor.execute("SELECT * FROM students WHERE id = ?;", str(student_id))
    return dict(zip([desc[0] for desc in cursor.description], cursor.fetchone()))


def print_dict(dictionary):
    print("\n+---+ Student's Information +---+")
    for header, content in dictionary.items():
        print(f" {header}: {content}")
    print("+-------------------------------+\n")


# To avoid entering strings into an int column for example.
def get_update_value(old_value):
    while True:
        _ = input("New Value: ")
        try:
            return type(old_value)(_)
        except ValueError:
            print("Please enter the appropriate data type.\n")


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