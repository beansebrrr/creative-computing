"""
Vince Matthew C. Caballero
Exercise 7: Some Counting

Time to use for-loops.
"""
from time import sleep  # Just for funsies

def oneToFifty():   # Counts 1 to 50 in increments of 1
    for j in range(50): # Loops from 0 to 49
        print(j + 1)    # Prints numbers (0 + 1) to (49 + 1)
        sleep(0.01)     # Slows down the counting for dramatic effect

def fiftyToOne():   # Counts down 50 to 1 in increments of 1
    for j in range(50, 0, -1):  # "-1" represents the increments in counting
        print(j)
        sleep(0.01)

def thirtyToFifty():    # Counts from 30 to 50 in increments of 1
    for j in range(30, 51): # "30" is the starting number
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

isValid = True
print("\n$========o Initiating the Count-inator... o========$\n")
sleep(1)

# Depending what the user had typed prior, it will run
# the appropriate function containing the loop.
if (count == "1"):
    oneToFifty()
elif (count == "2"):
    fiftyToOne()
elif (count == "3"):
    thirtyToFifty()
elif (count == "4"):
    fiftyToTen()
elif (count == "5"):
    oneHundredToTwoHundred()
else:
    print("\n$=======o No valid input detected. Exited. o=======$\n")
    isValid = False

if isValid == True:
    print("\n$=====o Thank you for using the Count-inator o=====$\n")

"""
Comments:

1.  In line 11, I could've done "for j in range (1, 51)" so that I could
    simply type "print(j)". But I opted to do "for j in range(50)" and
    printed out "print(j + 1)". There's no wrong way, I just preferred
    this one.

2.  There's another way I could've done line 15, by simply using the
    "reversed()" function on the range. Although, like I said, there
    is no wrong method.

3.  After coding the last three loops, I can say with complete
    confidence that "range()" simply emulates for-loops that can be
    found in C, which is typed like so:
    > for (int i = 0; i < 10; i++)

    which, in Python, it would look like:
    > for i in range(10)

    Both functions would count up from 0 as until it's no longer less
    than 10. This explains why it stops at 9 rather than 10, because
    10 is not less than 10. Mind-blowing reveal.

4.  To make things easier to navigate, I made a menu. Now whenever we
    run the program, we can decide which loop we'd like to be 
    demonstrated.

5.  At line 55, I initially wanted to use something similar to
    "switch statements", so that I didn't have to use "elif" multiple
    times. There seemed to be an existing "match" and "case" function
    in more recent versions of Python, however, I skipped on using it
    because I had concerns regarding compatibility, since match-case
    was only introduced since Python 3.10

For those curious, I would've made the match-case version like so by replacing lines 55-67 with:

match count:
    case "1":
        oneToFifty()
    case "2":
        fiftyToOne()
    case "3":
        thirtyToFifty()
    case "4":
        fiftyToTen()
    case "5":
        oneHundredToTwoHundred()
    case _:
        print("\n$=======o No valid input detected. Exited. o=======$\n")
        isValid = False
"""