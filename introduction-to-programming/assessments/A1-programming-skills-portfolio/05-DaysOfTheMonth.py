"""
Vince Matthew C. Caballero
Exercise 5: Days of the Month

Asks for a number representing a month, then tells how many days there are in said month.
I'm going to overcomplicate the leap-year requirement. Instead of asking whether or not it's
a leap year, I'll let the user input the year, and the program will determine if it's a leap
year or not.
"""

# I am going to abuse this format i love it so much
input("""
$===========o The day-of-the-month-inator o===========$
      
To use this tool, you must enter the number of the
month, for example, '1' for January. And then it will
tell you the number of days there are in this month!

$==============o Press Enter to begin. o==============$
""")

# Create an array: the keys are month numbers, and the values are the number of days in each month.
daysInAMonth = {
    1 : 31,     # January
    2 : 28,     # February
    3 : 31,     # March
    4 : 30,     # April
    5 : 31,     # May
    6 : 30,     # June
    7 : 31,     # July
    8 : 31,     # August
    9 : 30,     # September
    10 : 31,    # October
    11 : 30,    # November
    12 : 31}    # December

# Prompts the user for a number of a month.
month = input("Give me the number of a month (e.g. '1' for January): ")

while True: # Detects for a valid output to avoid errors.
    try:
        month = int(month)          # Tries to turn the input into an int
        if (month in range(1,13)):  # If 'month' is between 1 to 12, exits the loop and continues.
            break
    except ValueError:
        print("That's not an integer, dummy.")  
    month = input("Give me the number of a month (e.g. '1' for January): ") # If it doesn't work, reprompts the user.

if (month == 2):    # If the month given is 2, therefore february, this function takes leap years into account.
    leap = input("""
On leap years, February has 29 days. To take this into account, please type Y if it
is a leap year, and N if it isn't. If you don't know, you may simply type what year
it is, and I will do the calculation for you.

>>> """)

    while True: # Detects for a valid output to avoid errors.
        try:
            leap = int(leap)            # If the user inputs a number, determines whether it is a leap year.
            if (leap % 4 == 0):         # A leap year is a year which is divisible by 4.
                daysInAMonth[2] = 29    # If the remainder of 'year' divided by 4 is equal to 0, it changes the number of days in February to 29.
            break
        except ValueError:
            if (str.lower(leap) == "y"):    # Detects if the user had typed Y or N.
                daysInAMonth[2] = 29        # str.lower is used to remove case-sensitiveness.
                break
            elif (str.lower(leap) == "n"):
                break
        leap = input("\nPlease type Y if it's a leap year, or N if it isn't.\nOr you can type what year it is, and I'll do the rest: ")
    
print(f"""
$========o The day-of-the-month-inator says o=========$

           There are {daysInAMonth[month]} days in this month!

$=====================================================$
""")

"""
Comments:

Oh boy, I have a lot of explaining to do.

1.  I wanted to emulate a 'do-while' loop which I used when coding in C.
    It looked like the closest I could get was using 'while True', and use
    'break' once the condition has been met. In this case, I made the
    program repeatedly ask for an input as long as the input isn't valid.
    I eventually used this knowledge to improve my code in Exercise 3:
    Biography.

2.  After reading about it some more, I found some ways to combat the
    'input()' function's nature of always returning a string. I learned
    how to use the 'try-except' blocks. See line 41 and line 58. The
    program will first attempt to turn the user's input into an int,
    but if it returns an error, it skips that and runs the code under
    the 'except' block.

3.  As for the advanced requirements, which take leap years into account.
    I made an extra-complicated system. You can input Y or N for whether
    or not it's a leap year, but I also added another functionality. If
    you input a number, the program will treat that as a year, and will
    calculate if it's a leap year or not! This was so fun (and painful) to
    implement, but I think it was absolutely worth it.
"""