"""
Vince Matthew C. Caballero
Exercise 9: Hello

int main(void) :)
"""

def hello(name = None):  # I'll make this function print hello
    print("Hello", name)

def main():     # main() will call hello()
    name = input("What is your name? (Input blank if you want to skip): ")
    hello(name)

if __name__ == "__main__":  # runs main()
    main()

"""
I'm still getting used to the structure, but it looks like main() is
simply being treated like a separate function, same as hello(). I still
can't wrap my head around line 14, though. why __name__ == "__main__"?
Is it just a pre-determined variable? Maybe. 
"""