"""
Call by value and Call by reference
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

def print_sum(a, b):
    print(a + b)
    return sum

# Call by value
print_sum(10, 23)

# Call by reference
num = [29, 54]
print_sum(num[0], num[1])