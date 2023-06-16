#!/usr/bin/python3
def weighted_average(lst):
    if not lst:
        return 0

    numerator = sum(x * w for x, w in lst)
    denominator = sum(w for _, w in lst)

    return numerator / denominator
