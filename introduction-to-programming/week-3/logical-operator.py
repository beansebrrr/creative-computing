"""
Logical Operator
"""

print("\nLogical Operator o======================$\n")

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

print("\n$=======================================$\n")

# For the program to print True:
print(num1 > num2 and num1 != num2)     # All conditions must be met
print(num1 > num2 or num1 < num2)       # Atleast one condition must be met
print(not num1 > num2 or num1 != num2)  # Condition must NOT be met.

print("\n$=======================================$\n")