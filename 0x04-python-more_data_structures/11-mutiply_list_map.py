#!/usr/bin/python3


def mutiply_list_map(my_list=[], number=0):
    new_list = list(map(lambda x, num: x * num, my_list, len(my_list) * [number]))
    return new_list
