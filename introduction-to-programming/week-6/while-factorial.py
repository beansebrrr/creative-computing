"""
Get the factorial
"""
def get_int(prompt):
    num = input(prompt)
    while True:
        try:
            num = int(num)
            break
        except ValueError:
            num = input(prompt)
    return num

def get_factorial():
    num = get_int("What is the factorial of...? ")
    factorial = 1
    j = 1
    while j <= num:
        factorial *= j
        j += 1
    print(f"The factorial of {num} is {factorial}.")
    return factorial

get_factorial()
    