"""
Week 6: Loops
"""

# While Loop
num = 2
while num <= 50:
    print(num)
    num += 2
# Else condition
else:
    print('done lol')

num = 0
while num < 50:
    num += 2
    if num == 36:
        print("i'm not printing this number.")
        continue # skips the loop
    print(num)
else:
    print('done lol')

num = 0
while num < 50:
    num += 2
    if num == 36:
        print("i'm not printing this number.")
        break # ends the loop
    print(num)
else:
    print('done lol')