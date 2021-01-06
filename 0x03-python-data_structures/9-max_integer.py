#!/usr/bin/python3
def max_integer(my_list=[]):
    if list is None:
        return None
    else:
        for i in range(len(my_list) - 1):
            num_1 = my_list[i]
            if my_list[0] < num_1:
                my_list[0] = num_1
    return my_list[0]
