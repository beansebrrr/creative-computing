"""
Vince Matthew C. Caballero
Exercise 8: Simple Search

Searching lets gooooooo
"""
# I'll start by creating a list of names.
name_list = ["Dave", "Ian", "Ron", "Sam", "Jake", "Zac"]

# Function to look for name
def find_name(name):
    name = name.capitalize()
    if name in name_list:
        return True
    return False

# Extra feature: print all names in the list
def print_list():
    name_list.sort()
    print("\n+-------- List of Names --------+")
    for j in range(len(name_list)):
        print(f"{j+1}. {name_list[j]}")
    print("+-------------------------------+")

# Extra feature: add a new name to the list
def new_name():
    name = input("\nWhose name would you like to add? ")
    name = name.capitalize()

    if find_name(name):
        print(name, "already exists in the list.")
    name_list.append(name)
    print(name, "has been added to the list!")


input("""$==========o Namelist o==========$
    
Simply enter a name which you'd
like to look for. You can type
'NEW' to add a new name to the
list, or type 'LIST' to show
the entire list.
    
$=====o Hit Enter to begin o=====$""")

while True:
    name = input("\nFind a name (leave blank to exit): ")
    if name == 'NEW':
        new_name()
        continue
    elif name == 'LIST':
        print_list()
        continue
    elif name == '':
        print("Exited the program.")
        break

    if find_name(name):
        print(name.capitalize(), "is found in the list!")
    else:
        print(name.capitalize(), "is not in the list.")

"""
Manipulating arrays is very fun

I turned the search code into a function. I also
created a function to add new names to the list,
as well as a function to print the entire list in
alphabetical order.
"""