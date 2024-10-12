"""
Vince Matthew C. Caballero
Exercise 10: Is it Even

int main(void) part 2
"""

def isEven(j):  # Bool function, will explain below.
    if (j % 2 == 0):
        return True
    return False

def isPrime(j):
    for i in range(2, j):
        if j % i == 0:
            return False
    return True

def main():
    num = input("Please input a number: ")
    while True: # Converts num into an int, but reprompts if fails.
        try:
            num = int(num)
            break
        except ValueError:
            num = input("Please input a number: ")
    
    if isEven(num):
        print(f"\n{num} is an Even number!")
    else:
        print(f"\n{num} is an Odd number!")
    
    if isPrime(num):
        print(f"{num} is also a Prime number!\n")
    else:
        print(f"{num} is not a Prime number!\n")

if __name__ == "__main__":
    main()

"""
Okay, I have to admit, this might be the cleanest that my code
has ever been (probably because I don't have an oversized text
box but eh). I'm kind of tempted to redo all my last activities
so that they have a main(), but that seems like a lot of work.

Anyways, i made 'isEven' a bool function. To determine whether
or not a number is even, I used the modulo operation in line 9.
This performs division on two numbers (in this case, 'j' and 2)
and outputs the remainder. Since all even numbers are divisible
by 2, I use the modulo operator to check ifor a remainder. If
the remainder is 0, then it returns True, hence, it's an even
number. Otherwise, it'll return false, meaning it's an odd
number.

I added a new 'isPrime' function, which uses the same modulo
operator as 'isEven', but in a different application.
"""