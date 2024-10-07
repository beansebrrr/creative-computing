# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 12:13:59 2024

@author: Beence
"""
name = input("Name: ")
age = input("Age: ")
city = input("City: ")
gender = input("Gender: ")

response = input(f"So your name is {name}, a {age} year-old {gender}, and you're from {city}? (Y/N) ")

if response == "Y":
    print("That's so awesomesauce!!!\n")
elif response == "N":
    print("edi wag hinayupak kang gaga ka apaka walang kwenta\n")
else:
    print("That's not Y or N dumbahh\n")


