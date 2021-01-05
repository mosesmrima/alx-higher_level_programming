#!/usr/bin/python3
def no_c(my_string):
    string = [i for i in my_string if i != 'c' and i != 'C']
    string = "".join(string)
    return string
