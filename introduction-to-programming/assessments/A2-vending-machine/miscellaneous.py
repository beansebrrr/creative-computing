"""
These are functions that aren't really specific
to the vending machine program, but I made use
of them anyways.

The get_int, get_float, and get_bool functions were
inspired from the functions provided by CS50 which
go by the same names.
"""

from time import sleep
from os import name, system


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
        if _ in ["y", "yes", "true", "t", "1"]:
            return True
        elif _ in ["n", "no", "false", "f", "0"]:
            return False


"""clears the text from the console"""
def clear_terminal():
    system("cls" if name == "nt" else "clear")


"""emulate a typewriter effect when printing text"""
def typewriter(text, delay=0.01, end="\n"):
    for letter in text:
        print(letter, end="", flush=True)
        sleep(delay)
    print(end, end="")