#!/usr/bin/python3


def uniq_add(my_list=[]):
    uniq_add = 0
    for num in list(set(my_list)):
        uniq_add += num
    return (uniq_add)
