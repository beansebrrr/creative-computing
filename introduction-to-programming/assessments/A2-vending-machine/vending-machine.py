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
    top_up = get_float("How much you need? ")
    if top_up == 0:
        return
    
    print("I gotchu man.\n")
    CASH += top_up
    sleep(1)


def restock():
    db.execute("UPDATE items SET stock = stock + 10;")
    db.execute("UPDATE items SET stock = 50 WHERE stock > 50;")
    db.commit()

    print("The vending machine has been restocked")
    sleep(1)



def view_items():
    cursor.execute("SELECT * FROM items;")
    table = from_db_cursor(cursor)

    # Format the price to show 2 decimal values
    table.float_format = "10.2"
    print(table)


# = TWO PURCHASE FUNCTIONS FOR SOME REASON = #
# ======= OTHER IMPORTANT FUNCTIONS ======== #

def transaction():
    while True:
        item_id = get_id()

        # Magic Number
        if item_id == 0:
            return
        item = get_item_info(item_id)
        if buy(item) != None:
            return 0


# Is the actual function. I don't like nesting humoungously
def buy(item):
    global CASH, TOTAL_SPENT
    if item["stock"] < 1:
        print(f"\n{item["item"]} is out of stock!\n")
        return
    
    while True:
        quantity = get_int(f"How many {item["item"]} would you like to purchase? ")
        price = round((item["price"] * quantity), 2)
                      
        # Magic Number.
        if quantity == 0:
            return
        
        # Stops user from buying if insufficient stock
        elif quantity < 1:
            print(f"You cannot buy a negative number of {item["item"]}.\n")
        elif item["stock"] < quantity:
            print(f"There are not enough {item["item"]} in stock.\n")

        # Reprompt for quantity if price is too expensive
        elif CASH < price:
            print(f"You'd need AED {price:.2f}, but you only have AED {CASH:.2f}.\n")
        else:
            break
    print(f"\nYou need to put at least AED{price:.2f} in the machine.")
    while True:
        # Ask user to insert money
        insert_cash = get_float("Insert money: ")
            # Magic Number.
        if insert_cash == 0:
            return
            
        # Reprompts for insert_cash if not enough money, or too much money
        elif insert_cash > CASH:
            print(f"You only have AED {CASH:.2f}.")
        elif insert_cash < price:
            print("You did not put enough money.")
        else:
            break

    # Update database
    db.execute(f"UPDATE items SET stock = stock - {quantity} WHERE id = ?;", str(item["id"]))
    db.commit()

    # Update global 
    CASH -= price
    TOTAL_SPENT += price
    update_receipt(item["item"], quantity, price)

    # Return successfully
    print(f"\nPurchase Successful!\nYour change: AED {(insert_cash - price):.2f}")
    return 0


# Keep track of purchased items
def update_receipt(name, quantity, price):
    global TRANSACTIONS

    # If item had already been bought previously, update old record
    for transaction in TRANSACTIONS:
        if name == transaction["name"]:
            transaction["quantity"] += quantity
            transaction["price"] += price
            return
        
    # Otherwise add new record
    TRANSACTIONS.append({
        "name" : name,
        "quantity" : quantity,
        "price" : price, })


# ============= RETRIEVE DATA ============== #

def get_id():
    # Get list of valid IDs
    cursor.execute("SELECT id FROM items;")
    _ = cursor.fetchall()
    rows = [dict(row) for row in _]
    valid_ids = [id_num for row in rows for id_num in row.values()]

    # Prompt for a valid ID
    while True:
        item_id = get_int("Enter item's ID: ")
        if item_id in valid_ids or item_id == 0:
            return item_id
        print("Invalid ID.\n")


def get_item_info(item_id):
    cursor.execute("SELECT * FROM items WHERE id = ?;", str(item_id))
    return dict(cursor.fetchone())


def print_receipt():
    # ✨Aesthetic✨ purposes
    sys.stdout.write("Printing your receipt")
    sys.stdout.flush()
    for i in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        sleep(0.5)

    # Print all transactions into receipt
    print("\n+-----------+ RECEIPT +-----------+\n")
    for transaction in TRANSACTIONS:
        print(f"{transaction["quantity"]} {transaction["name"]}(s) : AED {transaction["price"]:.2f}")

    print(f"\nTotal: AED {TOTAL_SPENT:.2f}")
    print("\n+---------------------------------+\n")


# ============= ✨AESTHETIC✨ ============= #

def start_screen():
    dialogues = [
        "Need a snack? You've come to the right\nplace!",
        "I'll get you started with AED 50, but\nif you ever need more, don't be shy.",
        "Also, you might have to call if you\nneed a restock.",
        "Lastly, if you have to leave, remember,\nthe Magic Number is '0'.",
        "That's all you need to know so... knock\nyourself out.", 
    ]

    # Iterate through the dialogues
    for dialogue in dialogues:
        clear_terminal()
        print(TITLE)
        input(f"\n{dialogue}\n\n[Click 'Enter' to Continue]")
    main_menu()


def main_menu():
    clear_terminal()
    print(f"""{TITLE}
 [P] Purchase.
 [A] Top-up allowance.
 [R] Restock on goods.
 [0] Magic (get receipt).
+--------------------------------------+
Amount spent so far: AED {TOTAL_SPENT:.2f}
Allowance: AED {CASH:.2f}
""")


def exit_program():
    # ✨Aesthetic✨ purposes
    clear_terminal()
    sys.stdout.write("The vending machine must go")
    sys.stdout.flush()
    for i in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        sleep(0.5)
    print("")

    # Only prints receipt if the user had bought anything
    if len(TRANSACTIONS) != 0:
        print_receipt()
    else:
        clear_terminal()
    quit()


# ============ UNIVERSALLY USED ============ #

def get_int(prompt) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


def get_float(prompt) -> float:
    while True:
        try:
            return round(float(input(prompt)), 2)
        except ValueError:
            pass


def get_bool(prompt) -> bool:
    while True:
        _ = input(prompt).lower()
        if _ in ["y", "yes", "true", "t", "1"]:
            return True
        elif _ in ["n", "no", "false", "f", "0"]:
            return False


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

main()