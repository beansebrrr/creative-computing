def get_int(prompt):
    num = input(prompt)
    while True:
        try:
            num = int(num)
            break
        except ValueError:
            num = input(prompt)
    return num

product = 1
for j in range(3):
    multiplier = get_int(f"Num {j+1}: ")
    product *= multiplier

print(product)