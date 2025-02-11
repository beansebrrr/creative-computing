"""
Vince Matthew C. Caballero
Exercise 4: Primitive Quiz

Here's a quiz about the capitals of different European countries.
This might be my best work so far.
"""

def quiz():
    global score
    score = 0   # Initializing score variable. I'm making a score counter for fun!

    # This is a makeshift introduction screen.
    # I learned here that triple quotes are NOT limited to comments.
    # This is actually amazing.
    input("""
$==========o Let's have a little Quiz! o==========$
        
I will ask you 10 questions about the capitals of
countries around Europe, and if you get 5 points
and above, you pass! Don't worry, your answers
won't to be case sensitive. Anyways, are you ready? 

$============o Press Enter to begin. o============$
""")

    # Is a dict with the country as the key, and capital as the value.
    CountriesAndCapitals = {
        "Norway" : "oslo",
        "France" : "paris",
        "The United Kingdom" : "london",
        "The Netherlands" : "amsterdam",
        "Switzerland" : "bern",
        "Germany" : "berlin",
        "Austria" : "vienna",
        "Poland" : "warsaw",
        "Sweden" : "stockholm",
        "Belgium" : "brussels"
    }

    # Loops through the key-value pairs in CountriesAndCapitals and uses
    # them as variables to the ask() function
    for country, capital in CountriesAndCapitals.items():
        ask(country, capital)

    # Prints an appropriate response upon completing the quiz.
    if score > 4:
        print(f"Congratulations! You passed with score of {score}/10.")
    else:
        print(f"Aww, you got {score}/10. Let's do better next time!")


# This is a separate function to ask the question and
# check the answers. This is to avoid copy-pasting.
def ask(country, capital):
    global score    # Modifies the score variable from outsize the function
    response = input(f"What is the capital of {country}? ")

    if response.lower() == capital:  # I use an if-else statement in comparing the two strings.
        print("Correct!\n")             # The 'str.lower' function is used to remove caps-sensitiveness.
        score += 1
        return
    print(f"Wrong. The correct answer is {capital.capitalize()}.\n")   # using 'str.capitalize' for aesthetic purposes

if __name__ == "__main__":
    quiz()


"""
Comments:

I had a lot of fun making this quiz. It took me a while to
figure out a lot of things.

1.  Just some background info, I have some knowledge in using C, which
    is a nightmare to use when you want to manage strings. So when I found
    out comparing strings in Python was just as simple as using "==", I
    lost my mind.

2.  Python has built-in operations for strings, which saves me from a lot
    of pain. Mainly, I used 'str.lower()' to convert the user input into
    lowercase, so that when it's compared to the answer key, which is also
    lowercase, there won't be any issues with case-sensitiveness. I also
    made use of 'str.capitalize()', but that's mostly for aesthetics.

3.  When I finished the code meant to check the answers, I realized I'd have
    to reuse this again and again. Instead of copying and pasting mindlessly,
    I turned 'check' into its own function. This clears a significant amount
    of clutter, so I'm glad I did that.

4.  I made a score-counter for fun, as you've noticed. When I implemented it
    at first, I faced an issue where the score wouldn't update. After some
    searching, I learned that Python creates local variables within functions,
    which was a problem since I was manipulating 'score' inside the 'check'
    function. Luckily, all I had to do was to tell the program to manipulate
    'score' in a global scope by simply typing "global score" in line 10 and
    line 56.
"""