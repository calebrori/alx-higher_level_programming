#!/usr/bin/python3
def to_subtract(olnum):
    to_sub = 0
    a_list = max(olnum)

    for n in olnum:
        if a_list > n:
            to_sub += n

    return (a_list - to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    r_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ol_keys = list(r_num.keys())

    num = 0
    finrom = 0
    olnum = [0]

    for c in roman_string:
        for r_num in ol_keys:
            if r_num == c:
                if r_num.get(c) <= finrom:
                    num += to_subtract(olnum)
                    olnum = [r_num.get(c)]
                else:
                    olnum.append(r_num.get(c))

                finrom = r_num.get(c)

    num += to_subtract(olnum)

    return (num)
