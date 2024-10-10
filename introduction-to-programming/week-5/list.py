print("$=====o LISTS o=====$\n")

EmptyList = []
intList = [25, 75, 64, 58, 33, 87, 10]
MixedList = ["Hello!", 25, 28]
NestedList = [100, 25, 75, [50, 51, 52]]

print(f"Empty: {EmptyList}\nIntegers: {intList}\nMixed Data Types: {MixedList}\nNested: {NestedList}")

def indexing():
    # $==========o INDEXING o==========$
    print("\n$ Indexing $\n")

    print(f"Positive Index: {intList[0]}\nNegative Index: {intList[-7]}")
    # They return the same thing. Positive indexing starts from the
    # first value with 0. Negative indexing starts from the last value
    # with -1. 

def slicing():
    # $==========o SLICING o==========$
    print("\n$ Slicing $")

    print(f"{intList[2:5]}\n{intList[:]}")
    # Slicing returns the items from the 2nd index to the 4th (5-1) index.
    # Defaults values are 0:-1, meaning it returns the entire list.


def sorting():
    # $==========o SORTING o==========$
    print("\n$ Sorting $")

    intList.sort()  # Does what it says.
    print(intList)
    intList.sort(reverse=True)  # Also does what it says.
    print(intList)

def mutable():
    # $==========o LISTS ARE MUTABLE o==========$
    print("\n$ Lists are Mutable $\n")
    print("Old List:", intList)

    intList[2] = 10
    print("New List:  ", intList)
    intList[4:7] = 20, 30, 40       # You can modify a slice
    print("New List 2:", intList)
    intList[5:7] = intList[0:2]     # Yeah you get it. 
    print("New List 3:", intList)

def appending():
    # $==========o APPEND o==========$
    print("\n$ Appending $\n")
    print("Old List:", intList)

    intList.append(99)  # Does what it says. 
    print("New List:  ", intList)
    intList.extend([1, 2]) # Appends a list with another list
    print("New List 2:", intList)
    intList.extend([99, 98] + NestedList[3]) # Concatenation
    print("New List 3:", intList)

def inserting():
    # $==========o INSERT o==========$
    print("\n$ Inserting $\n")
    print("Old List:", intList)

    intList.insert(1, 20)
    print("New List:", intList)

def deleting():
    # $==========o DELETE o==========$
    print("\n$ Insert $\n")
    print("Old List:", intList)
    del intList[0]
    print("New List:", intList)
    intList.pop(2)
    print("New List:", intList)

run = input("""\n$===========o I Demonstrate Lists o===========$
            
    1: Index
    2: Slice
    3: Sort
    4: Mutable
    5: Append
    6: Insert
    7: Delete

Anything Else: Exit

>>> """)

match run:
    case '1':
        indexing()
    case '2':
        slicing()
    case '3':
        sorting()
    case '4':
        mutable()
    case '5':
        appending()
    case '6':
        inserting()
    case '7':
        deleting()
    case _:
        pass