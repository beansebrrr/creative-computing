"""
Vince Matthew C. Caballero
Exercise 6: Brute Force Attack

Guess we're gonna emulate passwords now. Making these textboxes
really make the code look messy. I hope it looks understandable
enough, though.
"""

# Initializing the important variables.
password = "12345"
attempts = 5

while attempts > 0:
    attempts -= 1   # Deducts 1 from the number of attempts left
    passwordInput = input("\nPlease enter your password: ")

    if (passwordInput == password): # If the password is correct, prints an output showing success and ends the loop right away with 'break'.
        print("""                               
$=========o Access Granted! o=========$
              
     Welcome back to the Batcave,
             Sir Batman.
              
$=====================================$""") 
        break
    elif (attempts > 0):    # If the password is wrong, prints this message as long as the user has more than 0 remaining attempts.
        print(f"""
$=========o Wrong password. o=========$

       You have {attempts} attempts left.

$=====================================$""")
    else:    # If the password is wrong and the number of attempts is at 0, prints a fail message.
        print("""
$==========o Access Denied o==========$

    You failed to enter the correct
  password. The local police has been
  contacted and will be on their way.
      
$=====================================$
""")

  
"""
Comments:

1.  I first began this program by initializing the most important
    variables, 'password' and 'attempts'. I made sure 'password' is
    treated as a string, since we do not need to perform any
    arithmetic operations on it. Rather, it's best to prevent it.

2.  After that, I then moved on to create the password-checker by
    starting with a while loop. To satisfy the advanced requirements,
    I made it so that the loop will only run as long as attempts is
    greater than 0.

3.  The first thing that happens in every loop is to deduct 1 from
    'attempts.' This is because, logically speaking, if you're on
    your 1st of 5 attempts, you'd only have 4 tries left. It'll
    then prompt the user for a 'passwordInput'.

Lastly, the if-else statements, which my # comments above have
already done a good job in explaining their functionality.
"""