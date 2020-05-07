#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        keys = list(a_dictionary.keys())
        max_int = a_dictionary[keys[0]]
        key_max_int = keys[0]
        for key in keys:
            if a_dictionary[key] > max_int:
                key_max_int = key
        return key_max_int
