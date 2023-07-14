#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return new_in_list
    elif idx >= len(my_list):
        return my_list
    else:
        new_lsit = list(my_list)
        new_list[idx] =element
        return new_list
