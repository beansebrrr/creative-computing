dayCount = input("How many days? ")
while True:
    if str.isdecimal(dayCount):
        dayCount = int(dayCount)
        break
    dayCount = input("Bruh how many days? ")

if dayCount == 0:   
    print("No fine.")
elif dayCount >= 1 and dayCount <= 5:               # If the dayCount is between 1 to 5
    print(f"You have a {(dayCount * 5):.2f}AED fine.")
elif dayCount >= 6 and dayCount <= 10:              # If the dayCount is between 6 to 10
    print(f"You have a {(dayCount * 10):.2f}AED fine.")
elif dayCount >= 11 and dayCount <= 15:             # If the dayCount is between 11 to 15
    print(f"You have a {(dayCount * 15):.2f}AED fine.")
else:                                               # If greater than 15
    print("Membership Cancelled.")