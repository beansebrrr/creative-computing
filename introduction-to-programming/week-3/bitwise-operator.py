"""
Bitwise Operator
# I have to google this fr
"""

print("\nBitwise Operator o=======================$\n")

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

print("\n$=======================================$\n")


print("Bitwise AND:",num1 & num2)          # If both bits are on, set bit to 1
print("Bitwise OR:",num1 | num2)           # If any bits are on, set bit to 1
print("Bitwise XOR:",num1 ^ num2)          # If only one bit is on, set bit to 1
print("Bitwise NOT (num1):", ~num1 )       # Inverts bits

print("\n$=======================================$\n")