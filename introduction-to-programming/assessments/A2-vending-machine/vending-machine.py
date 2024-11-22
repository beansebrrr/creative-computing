"""
Vince Matthew C. Caballero
Assessment 2: Vending Machine
"""

from pathlib import Path
from prettytable import from_db_cursor
import sqlite3
import get_utility as g

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
    view_items()

    while True:
        item = get_item_info(get_id())
        purchase(item)
        if not g.get_bool("Would you like to make another purchase? "):
            break
    
    print_receipt()


def view_items():
    cursor.execute("SELECT * FROM items;")
    table = from_db_cursor(cursor)

    # Format the price to show 2 decimal values
    table.float_format = "10.2"
    print(table)


def purchase(item):
    global CASH, TOTAL_SPENT
    if item["stock"] < 1:
        print(f"\n{item["item"]} is out of stock!\n")
        return
    
    # Check stock of item
    quantity = g.get_int(f"How many {item["item"]} would you like to purchase? ")
    if quantity < 1:
        print(f"\nYou cannot buy less than 1 {item["item"]}.\nTransaction terminated.\n")
        return
    elif item["stock"] < quantity:
        print(f"\nThere are not enough {item["item"]} in stock.\n")
        return
    
    # Check if user has enough cash
    price = round((item["price"] * quantity), 2)
    if CASH < price:
        print(f"\nYou need AED {price:.2f}, but you only have AED {CASH:.2f}.\n")
        return
    
    db.execute(f"UPDATE items SET stock = stock - {quantity} WHERE id = ?;", str(item["id"]))
    db.commit()

    # Update cash
    CASH -= price
    TOTAL_SPENT += price

    update_receipt(item["item"], quantity, price)


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
    print("\n+-----------+ RECEIPT +-----------+\n")
    for transaction in TRANSACTIONS:
        print(f"{transaction["quantity"]} {transaction["name"]}(s) : AED {transaction["price"]:.2f}")

    print(f"Total: {TOTAL_SPENT}")
    print("\n+---------------------------------+\n")


def get_item_info(item_id):
    if item_id == 0:
        quit
    cursor.execute("SELECT * FROM items WHERE id = ?;", str(item_id))
    return dict(cursor.fetchone())


def get_id():
    # Super roundabout way of getting all of the valid ids.
    # Doing this got harder since I have row_factory on.
    cursor.execute("SELECT id FROM items;")
    _rows_ = cursor.fetchall()
    rows = [dict(row) for row in _rows_]
    valid_ids = [id_num for row in rows for id_num in row.values()]
    valid_ids.append(0)

    while True:
        item_id = g.get_int("Enter item's ID: ")
        if item_id in valid_ids:
            return item_id
        print("Invalid ID.\n")


# o=====================o GENERAL-USE FUNCTIONS o=====================o #

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

def view_allowance():
    print(f"\nCash onhand: AED {CASH:.2f}\n")

main()