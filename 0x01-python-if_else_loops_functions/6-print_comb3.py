#!/usr/bin/python3
for number in range(1, 89):
    if number % 10 > ((number // 10) % 10):
        print("{:02d}".format(number), end=', ')
print("89")
