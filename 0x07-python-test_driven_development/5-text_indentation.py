#!/usr/bin/python3
"""Function that prints a text with 2 new lines"""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    b = 0
    while b < len(text) and text[b] == ' ':
        b += 1

    while b < len(text):
        print(text[b], end="")
        if text[b] == "\n" or text[b] in ".?:":
            if text[b] in ".?:":
                print("\n")
            b += 1
            while b < len(text) and text[b] == ' ':
                b += 1
            continue
        b += 1
