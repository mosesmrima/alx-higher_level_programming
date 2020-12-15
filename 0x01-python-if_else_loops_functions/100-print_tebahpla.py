#!/usr/bin/python3


j = 0
for i in range(122, 96, -1):
    if j == 1:
        i -= 32
        j = 0
    else:
        j = 1
    print(chr(i).format(), end="")
