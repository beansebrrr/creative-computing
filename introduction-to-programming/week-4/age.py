age = input("How old are you? ")

while True:
    if str.isdecimal(age):
        age = int(age)
        break
    age = input("Bruh how old are you? ")

if age > 49:
    print("\nSure unc.\n")
elif age > 3:
    print("\nOkay go to school dumbahh.\n")
else:
    print("\nGoo goo ga ga stinky.\n")
