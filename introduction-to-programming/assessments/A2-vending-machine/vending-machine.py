"""
Vince Matthew C. Caballero
Assessment 2: Vending Machine
"""

from datetime import date
from os import name, system
from pathlib import Path
from time import sleep
import sqlite3

# This might need to be pip install-ed.
from tabulate import tabulate

# Get database directory
root_dir = Path(__file__).resolve().parent
database = root_dir/"vending-machine.db"

# Check if database exists
if database.exists() == False:
    print("Error: No such file as vending-machine.db! Please put vending-machine.py and vending-machine.db in the same folder.")
    quit()

# SQLite connection.
conn = sqlite3.connect(database)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Global Variables.
ALLOWANCE = 50.00
TOTAL_SPENT = 0
TRANSACTIONS = []

# Get list of valid IDs, will be used later on.
with sqlite3.connect(database) as temp_conn:
    global valid_ids
    temp_cursor = temp_conn.cursor()
    temp_cursor.execute("SELECT id FROM items;")

    valid_ids = [num[0] for num in temp_cursor.fetchall()]

# I'm gonna use this a few times, but this
# won't be manipulated.
TITLE = r""" __     __             _ _             
 \ \   / /__ _ __   __| (_)_ __   __ _ 
  \ \ / / _ \ '_ \ / _` | | '_ \ / _` |
   \ V /  __/ | | | (_| | | | | | (_| |
  __\_/_\___|_| |_|\__,_|_|_| |_|\__, |
 |  \/  | __ _  ___| |__ (_)_ __ |___/ 
 | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \
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
            # Magic number.
            if item_id == 0:
                break

            item = get_item_info(item_id)
            if item["stock"] < 1:
                print(f"{item["name"]} is not in stock!")
                continue
            elif item["price"] > ALLOWANCE:
                print("You don't have enough money to even buy one!")
                continue

            quantity = get_quantity(item)
            # Magic number.
            if quantity == 0:
                continue
            
            # Proceed with buying item. 
            if buy(item, quantity) == True:
                break
        # Ask user if they want to do another purchase.
        # Also, magic number.
        if item_id == 0 or not get_bool("Would you like to buy something else? (y/N): "):
            break


"""Is the checkout part. This is the
chonkiest function in the program"""
def buy(item, quantity):
    global ALLOWANCE, TOTAL_SPENT
    
    while True:
        # Calculate price.
        price = round((item["price"] * quantity), 2)
        if price <= ALLOWANCE:
            break
        # If too expensive, reprompt for quantity and recalculate price.
        print(f"You need AED {price:,.2f}, but you only have AED {ALLOWANCE:,.2f}.\n")
        quantity = get_quantity(item)
        # Magic number.
        if quantity == 0:
            print("Transaction terminated.\n")
            return

    # Prompt user to pay to machine
    cash_paid = pay(price)
    # Magic number.
    if cash_paid == 0:
        print("Transaction terminated.\n")
        return 

    # Update database
    conn.execute(f"UPDATE items SET stock = stock - {quantity} WHERE id = ?;", (item["id"],))
    conn.commit()

    # Update globals
    ALLOWANCE -= price
    TOTAL_SPENT += price
    update_receipt(item["name"], quantity, price)

    # Purchase successful
    print("\n+---+ Purchase Successful! +---+\n")
    sleep(0.25)
    
    print_typewriter("The machine returned", f"AED {(cash_paid - price):,.2f}", delay=0.075)
    sleep(0.5)
    print_typewriter("Your new allowance", f"AED {ALLOWANCE:,.2f}", delay=0.075)
    return True


"""Ask for quantity"""
def get_quantity(item):
    while True:
        # Ask how many to buy
        quantity = get_int(f"How many {item["name"]} would you like to purchase? ")
        # Stops user from buying if insufficient stock
        if quantity < 0:
            print(f"You cannot buy {quantity} {item["name"]}(s).\n")
        elif item["stock"] < quantity:
            print(f"There are not enough {item["name"]} in stock.\n")
        else:
            return quantity


"""Prompts user to insert money until they add enough"""    
def pay(price):
    typewriter(f"\nPlease pay at least AED {price:,.2f} in the machine.")
    sleep(0.75)

    while True:
        # Ask user to insert money
        cash = get_float("Insert money >>> ")

        # Reprompts for cash if not enough money
        # Also allow user to input 0
        if cash > ALLOWANCE and cash != 0:
            print(f"You only have AED {ALLOWANCE:,.2f}.")
        elif cash < price and cash != 0:
            print("You did not put enough money.")
        else:
            return cash


"""Increase the ALLOWANCE of the user. Has a
little message if the user is a little greedy."""
def allowance_top_up():
    global ALLOWANCE

    print("You call your dad to give you more money...\n", flush=True)
    sleep(0.25)
    print_typewriter("Dad", "So, how much do you need?")
    sleep(0.5)
    top_up = get_float(">>> ")
    # Magic number.
    if top_up == 0:
        return
    
    if top_up >= 70:
        print_typewriter("Dad", "Don't you think that's a little too much?", end=" ")
        sleep(0.35)
        typewriter("Well, here you go anyways...", 0.025)
    else:
        print_typewriter("Dad", "Here you go buddy.", 0.025)
    
    sleep(0.5)
    ALLOWANCE += top_up
    sleep(1)


"""Add 10 to the stock of each item with a limit of 50."""
def restock():
    print(r"""
.-------.___
| ||||| |[_o\_
| ^^^^^ |- `  )
'-()------()-
""", flush=True)
    
    sleep(0.5)
    typewriter("The restock truck has arrived!")

    conn.execute("UPDATE items SET stock = stock + 10;")
    conn.execute("UPDATE items SET stock = 50 WHERE stock > 50;")
    conn.commit()
    
    sleep(1)
    typewriter("The vending machine has been restocked!")
    sleep(1)


"""Keep track of purchased items."""
def update_receipt(name, quantity, price):
    global TRANSACTIONS

    # If item had already been bought previously, update old record
    for transaction in TRANSACTIONS:
        if name == transaction["name"]:
            transaction["quantity"] += quantity
            transaction["price"] += price
            return
    # Otherwise add new record
    else:
        TRANSACTIONS.append({
            "name" : name,
            "quantity" : quantity,
            "price" : price,
        })


"""Only accept IDs found in valid_ids"""
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
        print("\n[Click Enter or type 'SKIP']")
        # Skip dialogue
        if input(">>> ").lower() in ["skip", "0"]:
            break


"""Initiate a cool sequence before exiting"""
def exit_program():
    # Emulate a loading sequence
    clear_terminal()
    print_typewriter("The vending machine must go", "...", separator="", delay=0.5)

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
    print_typewriter("Printing your receipt", "...", separator="", delay=0.5)

    # Print all transactions into a receipt
    print("\n+-------------+ RECEIPT +-------------+\n")
    for transaction in TRANSACTIONS:
        typewriter(f"{transaction["quantity"]} {transaction["name"]}(s) : AED {transaction["price"]:,.2f}")
    
    sleep(0.25)

    typewriter(f"\nTotal: AED {TOTAL_SPENT:,.2f}\nDate of Purchase: {date.today()}")
    print("\n+-------------------------------------+\n")




"""+-------------+ MISCELLANEOUS FUNCTIONS +-------------+"""

"""only allows an int input"""
def get_int(prompt) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


"""only allows a float input"""
# Rounded to 2 decimals since we're dealing with money
def get_float(prompt) -> float:
    while True:
        try:
            return round(float(input(prompt)), 2)
        except ValueError:
            pass


"""only allows yes or no inputs"""
def get_bool(prompt) -> bool:
    while True:
        _ = input(prompt).lower()
        if _ in ["y", "yes", "t", "true", "1"]:
            return True
        elif _ in ["n", "no", "f", "false", "0"]:
            return False


"""emulate a typewriter effect when printing text"""
def typewriter(text, delay=0.01, end="\n"):
    for char in text:
        print(char, end="", flush=True)
        sleep(delay)
    print(end, end="")


"""character dialogue, with name and text"""
def print_typewriter(printed, typewritten, delay=0.025, separator=": ", end="\n"):
    print(printed, end=separator, flush=True)
    sleep(0.25)
    typewriter(typewritten, delay=delay, end=end)


"""clears the text from the console"""
def clear_terminal():
    system("cls" if name == "nt" else "clear")


main()