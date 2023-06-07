#!/usr/bin/python3
def remove_char_at(str, c):
    if c < 0:
        return str
    else:
        str = str[0:c] + str[c+1:]
    return str
