#!/usr/bin/python3
"""say_my_name function module"""


def say_my_name(first_name, last_name=""):
    """function that prints My name is <first name> <last name>
    first_name and last_name have to be strings."""
    if (type(first_name) != str):
        raise TypeError("first_name must be a string")
    if (type(last_name) != str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
