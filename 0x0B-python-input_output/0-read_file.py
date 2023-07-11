#!/usr/bin/python3
"""Function that reads a text file"""


def read_file(filename=""):
    with open(filename, "r", encoding="utf8") as file:
        for line in file:
            print(line, end="")
