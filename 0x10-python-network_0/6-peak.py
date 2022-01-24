#!/usr/bin/python3
"""find peak of an array"""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    s = len(list_of_integers)
    if s == 1:
        return list_of_integers[0]
    elif s == 2:
        return max(list_of_integers)

    mid = int(s / 2)
    p = list_of_integers[mid]
    if p > list_of_integers[mid - 1] and p > list_of_integers[mid + 1]:
        return p
    elif p < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
