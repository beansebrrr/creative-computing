"""
Arithmetic Operator
"""

# I like making good-looking dividers.
# "\n" indicates newlines.
print("\n$========o Arithmetic Operator o========$\n")

# Obtains input from the user
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

print("\n$=======================================$\n")

# The variables are first created before using them in a print statement.
sum = num1 + num2
print(f"Your sum is {sum}.")

difference = num1 - num2
print(f"your difference is {difference}.")

product = num1 * num2
print(f"your product is {product}.")

quotient = num1 / num2
print(f"the quotient is {quotient}.")

modulo = num1 % num2
print(f"the remainder after dividing is {modulo}.")

print("\n$=======================================$\n")