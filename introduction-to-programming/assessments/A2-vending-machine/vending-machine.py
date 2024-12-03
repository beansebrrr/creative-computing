"""
Vince Matthew C. Caballero
Assessment 2: Vending Machine
"""

from datetime import date
from pathlib import Path
from time import sleep
import sqlite3

# This might need to be pip install-ed.
from tabulate import tabulate

# Miscellaneous functions.
from miscellaneous import *

# Root directory.
root_dir = Path(__file__).resolve().parent

# SQLite connection.
db = sqlite3.connect(root_dir/"vending-machine.db")
cursor = db.cursor()

# Get list of valid IDs before row_factory overcomplicates everything.
cursor.execute("SELECT id FROM items;")
valid_ids = [num[0] for num in cursor.fetchall()]

# Row factory makes it possible to return database values with their keys.
cursor.row_factory = sqlite3.Row

# Global Variables.
ALLOWANCE = 50.00
TOTAL_SPENT = 0
TRANSACTIONS = []

# I'm gonna use this a few times, but this
# won't be manipulated.
TITLE = """ __     __             _ _             
 \ \   / /__ _ __   __| (_)_ __   __ _ 
  \ \ / / _ \ '_ \ / _` | | '_ \ / _` |
   \ V /  __/ | | | (_| | | | | | (_| |
  __\_/_\___|_| |_|\__,_|_|_| |_|\__, |
 |  \/  | __ _  ___| |__ (_)_ __ |___/ 
 | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \\
 | |  | | (_| | (__| | | | | | | |  __/
 |_|  |_|\__,_|\___|_| |_|_|_| |_|\___|

+--------------------------------------+"""


def main():
    # Only show when program first runs
    start_screen()

    while True:
        # Main interface
        clear_terminal()
        print(f"""{TITLE}
 [P] Purchase.
 [A] Top-up allowance.
 [R] Restock on goods.
 [0] Magic Number (exit & get receipt).
+--------------------------------------+
Amount spent so far: AED {TOTAL_SPENT:,.2f}
Allowance: AED {ALLOWANCE:,.2f}
""")
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


"""Initiate a transaction"""
def make_purchase():
    while True:
        clear_terminal()
        view_items()

        print(f"\nTransaction #{len(TRANSACTIONS)+1}")
        while True:
            item_id = get_id()

            if item_id == 0:
                break

            item = get_item_info(item_id)
            if item["stock"] < 1:
                print(f"{item["name"]} is not in stock!")
                continue

            quantity = get_quantity(item)
            if quantity == None:
                continue

            if buy(item, quantity) == True:
                break
        
        if item_id == 0 or not get_bool("Would you like to buy something else? (y/N): "):
            break
        # elif not get_bool("Would you like to buy something else? (y/N): "):
        #     break


"""Is the actual "buying" part. This is
the chonkiest function in the program"""
def buy(item, quantity):
    global ALLOWANCE, TOTAL_SPENT
    
    while True:
        # Calculate price.
        price = round((item["price"] * quantity), 2)
        if price < ALLOWANCE:
            break
        # If too expensive, reprompt for quantity and recalculate price.
        print(f"You need AED {price:,.2f}, but you only have AED {ALLOWANCE:,.2f}.\n")
        quantity = get_quantity(item)

    # Prompt user to insert money to machine
    insert = insert_cash(price)
    if insert == None:
        print("Transaction terminated.")
        return 

    # Update database
    db.execute(f"UPDATE items SET stock = stock - {quantity} WHERE id = ?;", (item["id"],))
    db.commit()

    # Update globals
    ALLOWANCE -= price
    TOTAL_SPENT += price
    update_receipt(item["name"], quantity, price)

    # Purchase successful
    print("\n+---+ Purchase Successful! +---+\n")
    sleep(0.25)
    
    print("The machine returned: ", end="", flush=True)
    sleep(0.25)
    typewriter(f"AED {(insert - price):,.2f}", 0.075)
    sleep(0.5)

    print("You're now left with: ", end="", flush=True)
    sleep(0.25)
    typewriter(f"AED {ALLOWANCE:,.2f}", 0.075)
    return True


"""Ask for quantity"""
def get_quantity(item):
    while True:
        # Ask how many to buy
        quantity = get_int(f"How many {item["name"]} would you like to purchase? ")
        # Magic Number.
        if quantity == 0:
            return
        # Stops user from buying if insufficient stock
        elif quantity < 0:
            print(f"You cannot buy {quantity} {item["name"]}(s).\n")
        elif item["stock"] < quantity:
            print(f"There are not enough {item["name"]} in stock.\n")
        else:
            return quantity


"""Prompts user to insert money until they add enough"""    
def insert_cash(price):
    print(f"\nPlease insert at least AED {price:,.2f} in the machine.")
    sleep(0.75)

    while True:
        # Ask user to insert money
        insert_cash = get_float("Insert money >>> ")

        # Reprompts for insert_cash if not enough money
        # Also allow user to input 0
        if insert_cash > ALLOWANCE and insert_cash != 0:
            print(f"You only have AED {ALLOWANCE:,.2f}.")
        elif insert_cash < price and insert_cash != 0:
            print("You did not put enough money.")
        else:
            return insert_cash


"""Increase the ALLOWANCE of the user. Has a
little message if the user is a little greedy."""
def allowance_top_up():
    global ALLOWANCE
    clear_terminal()

    print("You call your dad to give you more money...\n")
    print("Dad: ", end="", flush=True)
    sleep(0.25)
    typewriter("So, how much do you need?", 0.025)
    sleep(0.5)
    top_up = get_float(">>> ")
    # Magic number.
    if top_up == 0:
        return
    
    print("Dad: ", end="", flush=True)
    sleep(0.25)
    if top_up >= 70:
        typewriter("Don't you think that's a little too much?", 0.025, end=" ")
        sleep(0.35)
        typewriter("Well, here you go anyways...", 0.025)
    else:
        typewriter("Here you go buddy.", 0.025)
    
    sleep(0.5)
    ALLOWANCE += top_up
    sleep(1)


"""Add 10 to the stock of each item with a limit of 50."""
def restock():
    db.execute("UPDATE items SET stock = stock + 10;")
    db.execute("UPDATE items SET stock = 50 WHERE stock > 50;")
    db.commit()

    print("The vending machine has been restocked")
    sleep(1)


"""Keep track of purchased items."""
def update_receipt(name, quantity, price):
    global TRANSACTIONS

    # If item had already been bought previously, update old record
    for transaction in TRANSACTIONS:
        if name == transaction["name"]:
            transaction["quantity"] += quantity
            transaction["price"] += price
    # Otherwise add new record
    else:
        TRANSACTIONS.append({
            "name" : name,
            "quantity" : quantity,
            "price" : price,
        })


"""Only accept IDs found in vending-machine.db"""
def get_id():
    # Prompt for a valid ID
    while True:
        item_id = get_int("Enter item's ID: ")
        if item_id in valid_ids or item_id == 0:
            return item_id
        print("Invalid ID.\n")


"""Return a dict of the item's information"""
def get_item_info(item_id):
    cursor.execute("SELECT * FROM items WHERE id = ?;", (item_id,))
    return dict(cursor.fetchone())


"""Print a table from vending-machine.db."""
def view_items():
    # Retrieve all contents of SQLite database
    cursor.execute("SELECT * FROM items;")
    _ = cursor.fetchall()
    data = [dict(row) for row in _]
    # Make all prices a floating-point value
    for row in data:
        row["price"] = round(float(row["price"]), 2)
    # Print table
    table = tabulate(data, headers="keys", floatfmt=".2f", tablefmt="psql")
    print(table)


"""Is the first thing the user is greeted to."""
def start_screen():
    dialogues = [
        "Walking across the street, you make your\nway to something you haven't seen here\nbefore...",
        "It's a new vending machine! Beside it is\na manual. You read its contents:",
        "\"Step 1: Enter the ID of the item you\nwish to purchase,\"",
        "\"Step 2: Enter how many you want to\nbuy.\"",
        "\"Step 3: Please be patient, the machine\nwill dispense your items shortly.\"",
        "\"Step 4: Enjoy your food and/or drinks!\"",
        "\"P.S.: If ever you need to go back or\nleave, just type the magic number '0'\"",
        "After reading the instructions, you take\nanother look at the machine...",
        "*Hmm... what should I get today?*"
    ]
    # Iterate through the dialogues
    for dialogue in dialogues:
        clear_terminal()
        print(TITLE)
        typewriter(dialogue)
        sleep(0.2)
        print("\n[Click 'Enter' or type 'SKIP']")
        if input(">>> ").lower() == "skip":
            break


"""Initiate a cool sequence before exiting"""
def exit_program():
    # Emulate a loading sequence
    clear_terminal()
    print("The vending machine must go", end="", flush="True")
    sleep(0.5)
    typewriter("...", 0.5)

    # Only prints receipt if the user had bought anything
    if len(TRANSACTIONS) > 0:
        print_receipt()
    else:
        clear_terminal()
    sleep(0.5)
    quit()


"""Print record of transactions"""
def print_receipt():
    # Emulates a loading sequence
    print("Printing your receipt", end="", flush=True)
    sleep(0.5)
    typewriter("...", 0.5)

    # Print all transactions into a receipt
    print("\n+-----------+ RECEIPT +-----------+\n")
    for transaction in TRANSACTIONS:
        typewriter(f"{transaction["quantity"]} {transaction["name"]}(s) : AED {transaction["price"]:,.2f}")
    
    sleep(0.25)

    typewriter(f"\nTotal: AED {TOTAL_SPENT:,.2f}\nDate of Purchase: {date.today()}")
    print("\n+---------------------------------+\n")


main()