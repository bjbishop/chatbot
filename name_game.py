#!/usr/bin/env python3

import re
from sys import argv

def name_suffix(name):
    c = name[:1]
    if c == 'a' or c == 'e' or c == 'i' or c == 'u':
        return name
    else:
        if len(name) >= 3:
            return name[2:]
        else:
            return name

def name_game_printer(name):
    print(name_game(name) + "\n")
            
def name_game(name):
    name = name.lower()
    suffix = name_suffix(name)
    string = ""
        
    string += f"{name}, {name}, bo-b{suffix}\n"
    if re.search(".+uck", name):
        string += "Banana-fana fo-....\n"
        string += "Hey, you're trying to trick me!"
    else:
        string += f"Banana-fana fo-f{suffix}\n"
        string += f"Fee-fi-mo-m{suffix}\n"
    return string

if __name__ == "__main__":
    if len(argv) == 1:
        print(name_game("Testing"))
    else:
        print(name_game(argv[1]))
