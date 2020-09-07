#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    b = my_list[:]
    if idx < 0:
        return b
    elif idx > (len(my_list) - 1):
        return b
    else:
        b[idx] = element
        return b
