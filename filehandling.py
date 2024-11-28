"""
Nov 28, 2024
File Handling
"""

import os
from pathlib import Path

# Root directory
root_dir = Path(__file__).resolve().parent

"""Error handling"""
print("+----------------------------------------+")
try: 
    real_file = open(root_dir/"real_file.txt", "r")
    print(real_file.read())
except FileNotFoundError:
    print("File not found.")
else:
    real_file.close()


"""Read lines as an array"""
print("+----------------------------------------+")
with open(root_dir/"filehandling.txt") as txt:
    print(txt.readlines())


"""Index them"""
print("+----------------------------------------+")
with open(root_dir/"filehandling.txt") as txt:
    print(txt.readlines(1))

    # Look how the tuple is incomplete now
    # like it got sliced or smth
    print(txt.readlines())


"""Loop"""
print("+----------------------------------------+")
with open(root_dir/"filehandling.txt") as txt:
    for line in txt:
        print(line)

"""Append"""
print("+----------------------------------------+")
with open(root_dir/"filehandling.txt", "a") as txt:
    txt.write("\n" + input("Input Text: "))
    print("Text Appended")


"""Delete File"""
print("+----------------------------------------+")
file_to_delete = root_dir/"delete_file.txt"
if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
else:
    print("File does not exist. Try making a file called \"delete_file.txt\"")