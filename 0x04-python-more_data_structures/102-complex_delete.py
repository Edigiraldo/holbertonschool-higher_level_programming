#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if a_dictionary:
        delete = []
        keys = a_dictionary.keys()
        for key in keys:
            if a_dictionary[key] == value:
                delete.append(key)

        for element in delete:
            del a_dictionary[element]

    return a_dictionary
