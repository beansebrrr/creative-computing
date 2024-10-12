"""
Vince Matthew C. Caballero
Exercise 3: Biography

This exercise makes use of dictionaries. It'll contain a name, hometown, and age.
"""

# Creates a dictionary containing strings called name, hometown, and age.
biography = {
    'name' : input("What's your name? "),   # Will ask for input from the user
    'hometown' : input("Where are you from? "),
    'age' : input("How old are you? ")
}

# See comments 1 and 2 in exercise 5.
while True:     # This function turns the 'age' variable into an int.
    try:
        biography['age'] = int(biography['age'])
        break
    except ValueError:  # If the user input is not an int, it will reprompt for 'age'
        biography['age'] = input("Please only type in numbers. How old are you?: ")


# Prints the contents of the biography with one print statement.
# I learned about the triple-quotation after Exercise 4.
print(f"""
$=======o Biography o=======$

Name: {biography['name']}
Hometown: {biography['hometown']}
Age: {biography['age']}
""")

"""
There's another way to print multiple lines with a single
print statement, and that's simply to type "\n" to indicate
a newline. It would look like this:

>   print(f"Name: {biography['name']}\nHometown: {biography['hometown']}\nAge: {biography['age']}")

I just prefer using the current method so it doesn't look that
messy compared to fitting it all in one line.
"""