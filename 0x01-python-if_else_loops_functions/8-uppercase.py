#!/usr/bin/python3


def uppercase(str):
    for char in str:
        ASCII = char
        if (ord(char) >= ord('a') and ord(char) <= ord('z')):
            ASCII = chr(ord(char) - 32)
        print(ASCII, end='')
    print()
