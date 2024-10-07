def get_int(prompt):            # The function will first ask for an input, and then
    num = input(prompt)         # will start a while loop. If the input can't be turned
    while True:                 # to an int, it will keep on reprompting. Once the user
        try:                    # provides a valid input, it'll end the loop and return
            num = int(num)      # the variable as an int.    
            break
        except ValueError:      
            num = input(prompt) 
    return num                  

def grade(j):   # Decides the grade remarks from A+ to D
    if j >= 90 and j <= 100:
        return "A+" # If the number is between 90 and 100
    elif j >= 80 and j < 90:
        return "A"  # If the number is between 80 and 90
    elif j >= 70 and j < 80:
        return "B"  # If the number is between 70 and 80
    elif j >= 60 and j < 70:
        return "C"  # If the number is between 60 and 70
    else:   
        return "D"  # If the number is less than 60

def main():
    subCount = get_int("How many subjects are you going to grade? ")
    marks = [0]*subCount    # Initializes a list with the size of subCount
    sum = 0             # Summation of all marks
    isPassed = True     # Bool for whether or not the student has passed
    
    for j in range(subCount):
        marks[j] = get_int(f"Mark {j+1}: ") # Prompts the user for their marks
        sum += marks[j] # Adds the marks to the sum
        if marks[j] <= 50:   # If any of the marks are equal to or below 50, fails the student.
            isPassed = False
            
    genAverage = sum / subCount
    print(f"Your general Average: {genAverage:.2f}.")   # {:.2f} simply prints genAverage with 2 decimal points

    if isPassed == True:
        print(f"You passed with the remarks: {grade(genAverage)}")
        return
    print("Fail.")

if __name__ == "__main__":
    main()