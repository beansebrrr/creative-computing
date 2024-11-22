"""
Vince Matthew C. Caballero
Assessment 2: Vending Machine
"""

from pathlib import Path
from time import sleep
import os, sqlite3, sys

# This might need to be pip install-ed
from prettytable import from_db_cursor


# Root directory
root_dir = Path(__file__).resolve().parent

# SQLite connection
db = sqlite3.connect(root_dir/"vending-machine.db")
db.row_factory = sqlite3.Row
cursor = db.cursor()

# Global Variables
CASH = 50.00
TOTAL_SPENT = 0
TRANSACTIONS = []


def main():
    start_screen()

    while True:
        main_menu()
        match input(">>> ").upper():
            case 'P':
                make_purchase()
            case 'A':
                allowance_top_up()
            case 'R':
                restock()
            case '0':
                exit_program()
            case _:
                pass

# ============= MAIN FUNCTIONS ============= #

def make_purchase():
    while True:
        view_items()  

        print(f"\nTransaction #{len(TRANSACTIONS)+1}")
        if transaction() == None:
            break
        if not get_bool("Would you like to buy something else? (y/N): "):
            break

def allowance_top_up():
    global CASH
    while True:
        try:
            top_up = round(float(input("How much cash you need? ")), 2)
            if top_up == 0:
                break
        except:
            continue
        print("I gotchu man.\n")
        CASH += top_up
        sleep(1)
        break

def view_items():
    cursor.execute("SELECT * FROM items;")
    table = from_db_cursor(cursor)

    # Format the price to show 2 decimal values
    table.float_format = "10.2"
    print(table)


def transaction():
    while True:
        item_id = get_id()
        if item_id == 0:
            return None
        
        item = get_item_info(item_id)
        if buy(item) == None:
            continue
        return 0


def buy(item):
    global CASH, TOTAL_SPENT
    if item["stock"] < 1:
        print(f"\n{item["item"]} is out of stock!\n")
        return None
    
    while True:
        quantity = get_int(f"How many {item["item"]} would you like to purchase? ")

        if quantity == 0:
            
            return None
        elif quantity < 1:
            print(f"You cannot buy a negative number of {item["item"]}.\n")
            continue
        elif item["stock"] < quantity:
            print(f"There are not enough {item["item"]} in stock.\n")
            continue

        price = round((item["price"] * quantity), 2)
        if CASH < price:
            print(f"\nYou need AED {price:.2f}, but you only have AED {CASH:.2f}.\n")
            continue
        break
    
    # Update database
    db.execute(f"UPDATE items SET stock = stock - {quantity} WHERE id = ?;", str(item["id"]))
    db.commit()

    # Update globals
    CASH -= price
    TOTAL_SPENT += price
    update_receipt(item["item"], quantity, price)
    print("\nPurchase Successful!\n")
    return True




def restock():
    db.execute("UPDATE items SET stock = stock + 10;")
    db.execute("UPDATE items SET stock = 50 WHERE stock > 50;")
    db.commit()
    print("The vending machine has been restocked")
    sleep(1)


def update_receipt(name, quantity, price):
    global TRANSACTIONS
    for transaction in TRANSACTIONS:
        if name == transaction["name"]:
            transaction["quantity"] += quantity
            transaction["price"] += price
            return
    TRANSACTIONS.append({
        "name" : name,
        "quantity" : quantity,
        "price" : price,
    })


def print_receipt():
    sys.stdout.write("Printing your receipt")
    sys.stdout.flush()
    for i in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        sleep(0.5)

    print("\n+-----------+ RECEIPT +-----------+\n")
    for transaction in TRANSACTIONS:
        print(f"{transaction["quantity"]} {transaction["name"]}(s) : AED {transaction["price"]:.2f}")

    print(f"\nTotal: AED {TOTAL_SPENT:.2f}")
    print("\n+---------------------------------+\n")


def get_item_info(item_id):
    cursor.execute("SELECT * FROM items WHERE id = ?;", str(item_id))
    return dict(cursor.fetchone())


def get_id():
    # Super roundabout way of getting all of the valid ids.
    # Doing this got harder since I have row_factory on.
    cursor.execute("SELECT id FROM items;")
    _rows_ = cursor.fetchall()
    rows = [dict(row) for row in _rows_]
    valid_ids = [id_num for row in rows for id_num in row.values()]

    while True:
        item_id = get_int("Enter item's ID: ")
        if item_id in valid_ids or item_id == 0:
            return item_id
        print("Invalid ID.\n")


def get_int(prompt) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


def get_bool(prompt) -> bool:
    while True:
        _ = input(prompt).lower()
        if _ in ["y", "yes", "true", "t"]:
            return True
        elif _ in ["n", "no", "false", "f"]:
            return False


def start_screen():
    dialogues = [
        "Need a snack? You've come to the right\nplace!",
        "I'll get you started with AED 50, but\nif you ever need more, don't be shy.",
        "Also, you might have to call if you\nneed a restock.",
        "Lastly, if you have to leave, remember,\nthe magic number is '0'.",
        "That's all you need to know so... knock\nyourself out.",
        
    ]

    for dialogue in dialogues:
        clear_terminal()
        print(""" __     __             _ _             
 \ \   / /__ _ __   __| (_)_ __   __ _ 
  \ \ / / _ \ '_ \ / _` | | '_ \ / _` |
   \ V /  __/ | | | (_| | | | | | (_| |
  __\_/_\___|_| |_|\__,_|_|_| |_|\__, |
 |  \/  | __ _  ___| |__ (_)_ __ |___/ 
 | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \\
 | |  | | (_| | (__| | | | | | | |  __/
 |_|  |_|\__,_|\___|_| |_|_|_| |_|\___|""")
        input(f"""
+--------------------------------------+
{dialogue}

[Click 'Enter' to Continue]
""")
    main_menu()


def main_menu():
    clear_terminal()
    print(f""" __     __             _ _             
 \ \   / /__ _ __   __| (_)_ __   __ _ 
  \ \ / / _ \ '_ \ / _` | | '_ \ / _` |
   \ V /  __/ | | | (_| | | | | | (_| |
  __\_/_\___|_| |_|\__,_|_|_| |_|\__, |
 |  \/  | __ _  ___| |__ (_)_ __ |___/ 
 | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \\
 | |  | | (_| | (__| | | | | | | |  __/
 |_|  |_|\__,_|\___|_| |_|_|_| |_|\___|

+--------------------------------------+
 [P] Purchase.
 [A] Top-up allowance.
 [R] Restock on goods.
 [0] Magic number to exit.
+--------------------------------------+
Amount spent so far: AED {TOTAL_SPENT:.2f}
Allowance: AED {CASH:.2f}
""")



def exit_program():
    clear_terminal()
    sys.stdout.write("The vending machine must go")
    sys.stdout.flush()
    for i in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        sleep(0.5)
    print("")

    if len(TRANSACTIONS) != 0:
        print_receipt()
    else:
        clear_terminal()
    quit()
    

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

main()