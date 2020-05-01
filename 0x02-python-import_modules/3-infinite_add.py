#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argc = len(sys.argv)
    sum = 0
    if argc > 1:
        for index in range(1, argc):
            sum += int(sys.argv[index])
    print('{:d}'.format(sum))
