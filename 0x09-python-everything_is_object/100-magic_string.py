#!/usr/bin/python3
def magic_string():
    magic_string.pop = getattr(magic_string, 'pop', 0) + 1
    return ("BestSchool, " * (magic_string.pop - 1) + "BestSchool")
