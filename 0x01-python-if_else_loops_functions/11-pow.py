#!/usr/bin/python3


def pow(a, b):
    a_b = 1
    if a == 0:
        return (0)

    while b != 0:
        if b > 0:
            a_b *= a
            b -= 1
        if b < 0:
            a_b *= 1 / a
            b += 1
    return (a_b)
