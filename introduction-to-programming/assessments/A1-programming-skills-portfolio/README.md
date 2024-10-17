
# Assessment 1: Programming Skills Portfolio
This portfolio contains 10 exercises showcasing the projects and programs I've created for this assessment. Below is my thought process from when I was coding these programs, highlighting my hurdles and solutions to these problems.

## Exercise 1: Coding is Cool
[View Source Code](https://github.com/beansebrrr/creative-computing/blob/main/introduction-to-programming/assessments/A1-programming-skills-portfolio/01-CodingIsCool.py)

The first activity provides 3 *variables*, `word1`, `word2`, and `word3`. I must output **"Coding is Cool"** to the terminal. I simply assigned each variable with their respective word.
```
word1 = "Coding"
word2 = "is"
word3 = "Cool"
```
... and then I used `print()` to output the variables into the terminal. There will be more comments in the source code.

## Exercise 2: Simple Sums
[View Source Code](https://github.com/beansebrrr/creative-computing/blob/main/introduction-to-programming/assessments/A1-programming-skills-portfolio/02-SimpleSums.py)

For the second activity, two variables: `num1` and `num2`, are assigned with the numbers `8` and `10` respectively. A third variable, `sum` equates to the sum of `num1` and `num2`. The sum is then printed into the terminal, which fulfills the requirements for this activity.

## Exercise 3: Biography
[View Source Code](https://github.com/beansebrrr/creative-computing/blob/main/introduction-to-programming/assessments/A1-programming-skills-portfolio/03-Biography.py)

This activity revolves around *dictionaries*, a data structure which contains a *key-value pair*. I created one, appropriately named `biography` wherein the *keys* are named `name`, `hometown`, and `age`; and the *values* contain the data within the *keys*. The contents of `biography` is then printed onto the terminal.

This is the first activity which prompts optional **Advanced Requirements**. The first of which is to have the user input their name instead of hard-coding the values. This can easily be achieved by replacing the current *values* with an `input()` function, which returns a *string* typed by the user. One problem with this is that since `input()` returns a *string*, that means value of `age` will be treated as a *string*, and that's not the appropriate data type for an age. As a temporary solution, I used `int(input())` so that it will only accept *integers*. I soon updated the code with a solution I call [get_int](#get_int) which I have continued to use throughout my other activities.

## Exercise 4: Primitive Quiz
[View Source Code](https://github.com/beansebrrr/creative-computing/blob/main/introduction-to-programming/assessments/A1-programming-skills-portfolio/04-PrimitiveQuiz.py)

This one was fun to figure out. I have two iterations of this code, but I will start with explaining [my first version](https://github.com/beansebrrr/creative-computing/blob/2b2c99bd76cfcca31bd1e422421846f7263d71bd/introduction-to-programming/assessments/A1-programming-skills-portfolio/04-PrimitiveQuiz.py).
I started with a variable `response` which prompts for user-input, saying "What is the capital of France?". To then check for correctness, I have another variable `answerKey` which contains the correct answer, and will be compared to `response`. If they are identical, the answer is correct. And if not, the answer is wrong. 

Moving onto the **Advanced Requirements**. To address the case-sensitiveness: I made `answerKey` lowercase, and used the `str.lower()` function on `response` so that both variables will be in lowercase when compared to each other. Next, I have to expand the program by asking for the capitals of **10** European countries. I realize I'd have to compare strings multiple times, and it'd be tedious to copy multiple *if-else* statements. Now if I learned anything from studying *C*, it's that I can create my own functions and call them as many times as I want. I created a new function `check()` that will compare the user's input with `answerKey` which its value changes every time before `check()` is called. For fun, I also added a `score` variable, which is displayed when all 10 questions are completed. 

Now, let's talk about the current code. I didn't like the look of copy-pasting, so I wanted to change it up. When I was playing around with another project outside of my assessments, I learned I could use *for loops* to cycle through a *dictionary*. So I created a dict `CountriesAndCapitals` with the country as the `key` and its capital as the `value`. I then used a *for loop* with the items in the *dictionary* and used them as arguments for the function `ask()`, which is derived from the original `check()` function. I renamed it to `ask()` since it also now asks the question within the function along with checking the answer. With this, I was able to shorten the amount of code, as well as eliminate any repetitiveness.

## Exercise 5: Days of the Month
[View Source Code](https://github.com/beansebrrr/creative-computing/blob/main/introduction-to-programming/assessments/A1-programming-skills-portfolio/05-DaysOfTheMonth.py)

This one was also a lot of fun to make. I first made a *dictionary* with the *keys* as numbers that correspond to a month, and the *values* as the number of days in those months. I reused [get_int](#get_int) to get user input for an *int*, and added a few more conditions so that it would only accept values from `1` to `12`. The program then prints out the number of days there are in a specific month.

The **Advanced Requirements** stated to make the program account for leap years. I started with an *if statement* to check if the selected month is `2` (February), only then will this part of the code take action. I made the program accept `y` or `n` when asking if it's a leap year, but I also added another feature. If the user inputs an *int*, the program will treat it as a `year`, and calculates if the `year` given is a leap year or not. If the program verifies that it's dealing with a leap year (either through `y` or an *int* divisible by `4`), it will modify February's value from `28` to `29`. Otherwise, the program will resume without change.

## Exercise 6: Brute Force Attack
[View Source Code](https://github.com/beansebrrr/creative-computing/blob/main/introduction-to-programming/assessments/A1-programming-skills-portfolio/06-BruteForceAttack.py)

This program utilizes the same fundamentals as exercise 4, using *if conditions* to compare two strings. A string variable `password` contains the correct password, I'm treating it as a *string* since I do not have to perform arithmetic equations on it. In fact, I do not want it to change. The program will prompt the user to enter a password. If the `passwordInput` is the same as , then the program will print "Access Granted" onto the terminal. Otherwise, it will print out "Access Denied" instead.

To comply with the **Advanced Requirements**, I started with creating a new variable `attempts`. I then put all of the code into a *while loop* which will keep running until the user runs out of attempts. Once attempts reach 0, it prints a different line to the terminal, telling the user "The authorities are on their way" (they're not actually coming, don't worry).

## Exercise 7: Some Counting
[View Source Code](https://github.com/beansebrrr/creative-computing/blob/main/introduction-to-programming/assessments/A1-programming-skills-portfolio/07-SomeCounting.py)

This is the first proper introduction to *for loops* and additionally, the `range()` function. *for loops* will run lines of code a specified number of times, which can be configured by adding arguments to `range()`. For fun, I also added a navigation screen so that the user can pick what *for loop* they want to see. Additionally, I deliberately added some delay to the count functions to make it look ✨cool✨.

## Exercise 8: Simple Search
[View Source Code](https://github.com/beansebrrr/creative-computing/blob/main/introduction-to-programming/assessments/A1-programming-skills-portfolio/08-SimpleSearch.py)

Searching within a *list* made me use *if statements* again. This one is quite simple. I first create a *list* containing different names. I then created the *if statement* which prints out whether the name is present in `name_list`. The **Advanced Requirements** made me turn the hard-coded variable `name` into a *user input* so that the user can decide what name to find in `name_list`. Additionally, I eliminated case-sensitiveness just by using `str.capitalize()` on `name`.

To add to my program, I implemented a function `new_name()` to add new names to the list, as well as `print_list` to print out the whole list of names. They can be called by inputting `NEW` or `LIST` respectively. This made the program feel much more complete to me.

## Exercise 9: Hello
[View Source Code](https://github.com/beansebrrr/creative-computing/blob/main/introduction-to-programming/assessments/A1-programming-skills-portfolio/09-Hello.py)

At its core, the code behind this is quite simple. But this also is the first proper introduction to *functions*, a block of code separate from the *main* function, which can be called and reused multiple times. In this case, I created a *function* `hello()`, which prints "hello" to the terminal. And then in `main()`, I can use `hello()` to run the code without having to type it all over again.

There are no **Advanced Requirements** this time, so I could add a few more features to the program. I gave the user the option to input their name, so `hello()` can also print the user's name.

## Exercise 10: Is it Even?
[View Source Code](https://github.com/beansebrrr/creative-computing/blob/main/introduction-to-programming/assessments/A1-programming-skills-portfolio/10-IsItEven.py)

For our final activity, the program will ask for a number `num` using [get_int](#get_int) once again. I then made a function to determine whether the `num` is an odd or even number. I did this using the *modulo operator*, only returning `True` if the remainder of `num` divided by `2` is equal to `0`.

This activity seemed a little plain, so I added another function, `isPrime()`, which does what it says: it checks if the number given is a prime number. I made use of a *for loop* and *modulo* to get the remainder `num` when divided by every number between `2` and `num`. if any of the numbers is a factor of `num`, it returns `False`.

## Sololearn: Introduction to Python
![Introduction to Python Certificate](introduction_to_python_certificate.jpg)

One more requirement for this assessment is to take and complete the [Introduction to Python](https://www.sololearn.com/en/learn/courses/python-introduction) course from **Sololearn**. This certificate above serves as proof of my completion of the course.

## Others
This space is for extra bits of information that I can't find a place for.

### get_int
the `input()` function is super useful for when you need, well, user input. One flaw is that it will always return as a *string*, which means I need to prefix `input()` with `int()` to convert *strings* into an *int*, like so:
```
age = int(input("How old are you? "))
```
This, however, has one big flaw that kept bothering me. If I input a *string* that cannot be turned into an *int* (for example, "Eighteen"), it will return an error and break the program. I want to find a way to get integer input from the user, so I did some research. I first need to make a condition if the input can be turned into an *int*. There's a *string operation* called `str.isdecimal()`, which returns `True` if the user's input only contains *decimal values*.
```
age = input("How old are you? )

if age.isdecimal() == True:
    age = int(age)
```
Now this has its own issue. Since `str.isdecimal()` returns `True` if the string has **only** numbers, it can't work on negative *int*s. This is when I learned about *try-except*, which I used like this:
```
age = input("How old are you? )

try:
    age = int(age)
except ValueError:
    print("Invalid Input")
```
I'm satisfied with this function now, but I want to now reprompt the user whenever they give an invalid input. The one way I can think of is to use a loop.
```
age = input("How old are you? )

while True:
    try:
        age = int(age)
        break
    except ValueError:
        age = input("How old are you? ")
```
This block of code above is what I've used and reused all across my activities which need *int* inputs, and I've added extra conditions to parts that required such.