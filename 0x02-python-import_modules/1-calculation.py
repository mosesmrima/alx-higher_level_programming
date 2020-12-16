#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5

    sum = add(a, b)
    dif = sub(a, b)
    prod = mul(a, b)
    quo = div(a, b)
    print("{} + {} = {}".format(a, b, sum))
    print("{} - {} = {}".format(a, b, dif))
    print("{} * {} = {}".format(a, b, mul))
    print("{} / {} = {}".format(a, b, div))
