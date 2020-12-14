#!/usr/bin/python3
def uppercase(str):
    for i in str[:]:
        if 97 <= ord(i) <= 122:
            m = ord(i)
            m = m - 32
            i = m
            i = chr(i)
        print(i.format(), end="")
    print('\n'.format(), end="")
