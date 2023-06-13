#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return

    large = my_list[0]
    for r in range(1, len(my_list)):
        if large < my_list[r]:
            large = my_list[r]
        else:
            continue
    return large
