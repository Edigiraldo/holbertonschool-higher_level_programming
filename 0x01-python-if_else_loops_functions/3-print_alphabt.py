#!/usr/bin/python3
for letter in range(97, 123):
    if letter != 101 and letter != 113:  # ASCII code for 'e' and 'q'
        print(chr(letter), end='')
