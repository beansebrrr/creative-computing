"""
Create a multiplication table
"""
def get_int(prompt):
    num = input(prompt)
    while True:
        try:
            num = int(num)
            break
        except ValueError:
            num = input(prompt)
    return num

def multiplication_table():
    table = get_int("What multiplication table would you like to generate?\n>>> ")
    table_range = get_int("How far would you like to multiply?\n>>> ")

    j = 1
    while j <= table_range:
        print(f"{j} * {table} = {j * table}")
        j += 1
    return

multiplication_table()