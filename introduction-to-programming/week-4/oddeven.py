
num = input("Please input a number: ")

while True:
    try:
        num = int(num)
        break
    except ValueError:
        num = input("Error! please input in numbers only: ")

if num % 2 == 0:
    print(f"{num} is an Even number!")
else:
    print(f"{num} is an Odd number!")
