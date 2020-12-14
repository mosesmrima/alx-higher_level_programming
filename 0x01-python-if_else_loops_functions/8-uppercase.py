#!/usr/bin/python3
def islower(c):
    for i in c[:]:
        if 97 <= ord(i) <= 122:
            m = ord(i)
            m = m - 32
            i = m
            print(chr(i).format(), end="")
        else:
            print(i.format(), end="")
