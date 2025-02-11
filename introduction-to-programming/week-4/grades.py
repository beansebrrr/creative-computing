mark1 = int(input("Marks 1: "))
mark2 = int(input("Marks 2: "))
mark3 = int(input("Marks 3: "))
mark4 = int(input("Marks 4: "))
mark5 = int(input("Marks 5: "))

average = (mark1 + mark2 + mark3 + mark4 + mark5) / 5

if mark1 > 50 and mark2 > 50 and mark3 > 50 and mark4 > 50 and mark5 > 50:
    print(f"Passed with an average of {average}")
    
    if (average >= 90 and average <= 100):
        print("Grade: A")
    elif (average >= 80 and average <= 89):
        print("Grade: B")
    elif (average >= 70 and average <= 79):
        print("Grade: C")
    elif (average >= 60 and average <= 69):
        print("Grade: D")
    else:
        print("Grade: E")
else:
    print("Fail.")