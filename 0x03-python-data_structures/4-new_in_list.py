#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)
    elif idx > (len(my_list) - 1):
        return my_list
    else:
        list_new = [x for x in my_list]
        list_new[idx] = element
        return (list_new)