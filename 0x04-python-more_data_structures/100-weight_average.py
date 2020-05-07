#!/usr/bin/python3
def weight_average(my_list=[]):
    w_average = 0
    sum_elements = 0
    for tupl in my_list:
        w_average += tupl[0] * tupl[1]
        sum_elements += tupl[1]
    if sum_elements != 0:
        w_average /= sum_elements

    return w_average    
