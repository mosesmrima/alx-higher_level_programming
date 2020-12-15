#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= len(str):
        return str
    str1 = list(str)
    str1[n] = ""
    rstr = ""
    for i in str1:
        rstr += i
    return rstr
