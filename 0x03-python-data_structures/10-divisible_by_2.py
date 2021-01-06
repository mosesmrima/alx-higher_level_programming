#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for j in range(len(my_list)):
        if my_list[j] % 2 == 0:
            new_list[j] = True
        else:
            new_list[j] = False
    return new_list
