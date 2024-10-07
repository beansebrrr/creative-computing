"""
Vince Matthew C. Caballero
Exercise 7: Some Counting

Time to use for-loops.
"""

from time import sleep

def oneToFifty():   # Counts 1 to 50 in increments of 1
    for j in range(50):
        print(j + 1)
        sleep(0.01)

def fiftyToOne():   # Counts down 50 to 1 in increments of 1
    for j in range(50, 0, -1):
        print(j)
        sleep(0.01)

def thirtyToFifty():    # Counts from 30 to 50 in increments of 1
    for j in range(30, 51):
        print(j)
        sleep(0.01)

def fiftyToTen():   # Counts down from 50 to 10 by increments of 2
    for j in range(50, 9, -2):
        print(j)
        sleep(0.01)

def oneHundredToTwoHundred():   # Counts from one hundred to two hundred by increments of 5
    for j in range(100, 201, 5):
        print(j)
        sleep(0.01)

# I made a simple navigation menu.
count = input("""$===========o This is the Count-inator o===========$
This program uses for-loops to count within various
ranges. Just enter a number below

    1: Count from 1 to 50
    2: Countdown from 50 to 1
    3: Count from 30 to 50
    4: Countdown from 50 to 10 by 2
    5: Count from 100 to 200 by 5

Any other input will exit the program right away.
            
>>> """)
isValid = False

try:
    count = int(count)   # Turns the 'count' variable into an int
    if count > 0 and count < 6:    # Checks if 'count' is a number between 1 to 5
        print("\n$========o Initiating the Count-inator... o========$\n")
        isValid = True
except ValueError:
    isValid = False

# Depending what the user had typed prior, it will run
# the appropriate function containing the loop.
match count:
    case 1:
        oneToFifty()
    case 2:
        fiftyToOne()
    case 3:
        thirtyToFifty()
    case 4:
        fiftyToTen()
    case 5:
        oneHundredToTwoHundred()
    case _:
        print("\n$=======o No valid input detected. Exited. o=======$\n")


if isValid == True:
    print("\n$=====o Thank you for using the Count-inator o=====$\n")

