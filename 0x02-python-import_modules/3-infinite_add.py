#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv)
    sum = 0
    i = 1
    for i in range(1, argc):
        arg = int(argv[i])
        sum += arg
    print("{}".format(sum))
