"""
Vince Matthew C. Caballero
Exercise 8: Simple Search

Searching lets gooooooo
"""
nameList = ["jake", "zac", "ian", "ron", "sam", "dave"] # I'll start by creating a list of names.

name = input("\nPlease enter a name: ") # For the advanced requirements, I let the user input what name the program should search for.

if str.lower(name) in nameList: # If the user's inputted name is within the array of names, it will declare that the name is found.
    print("\nName Found!\n")
else:
    print("\nName does not exist in the list...\n")

"""
This was way easier than when I would do this in C.

I initially turned the search code into a separate
function, but after completing it, I realized I didn't
have to do that. So I just put it back where it belongs.

Additionally, in line 11, I decided to remove
case-sensitiveness. This led me to set all the names in
"nameList" to lowercase. If I wanted, I could've also
changed line 15 into:
> if str.capitalize(str.lower(name))
and it would also have removed case-sensitiveness
without having to manipulate the list. In the end, I
just settled on the current method.
"""