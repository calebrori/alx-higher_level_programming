#!/usr/bin/python3
for c in range(9):
    for r in range(c + 1, 10):
        if c * 10 + r < 89:
            print("{:g}{:g}".format(c, r), end=", ")
print("{:g}".format(89))
