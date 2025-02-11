"""
Nov 28, 2024
Exception Handling
"""

TUPLE = [10, 20, 30, 40, 50]
INTEGER = 5

"""Division by Zero"""
try:
    a = int(input("A: "))
    b = int(input("B: "))

    c = a / b
    print(c)

# except ZeroDivisionError:
except Exception as E:
    print(E)


"""Name Error"""
try:
    print(totally_real_variable)
except NameError as E:
    print(E)


"""Index Error"""
try:
    print(TUPLE[5])
except IndexError as E:
    print(E)


"""Multiple Errors"""
try:
    quotient = INTEGER / 0
    real_index = TUPLE[10]
    print(f"{quotient} and {real_index}")
except ZeroDivisionError:
    print("You can't divide by 0")
except IndexError as E:
    print(E)