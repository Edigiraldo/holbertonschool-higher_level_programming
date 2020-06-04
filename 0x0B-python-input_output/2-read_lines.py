#!/usr/bin/python3
"""Module for read_lines function."""


def read_lines(filename="", nb_lines=0):
    """function that reads n lines of a text
    file (UTF8) and prints it to stdout"""
    with open(filename, encoding='utf-8') as myfile:
        num_lines = 0
        while num_lines < nb_lines or nb_lines <= 0:
            line = myfile.readline()
            if line == "":
                break
            print("{}".format(line), end='')
            num_lines += 1
    return num_lines
