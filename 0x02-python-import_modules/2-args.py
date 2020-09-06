#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    n = len(argv) - 1
    if n == 1:
        print("1 argument:")
    elif n == 0:
        print("0 arguments.")
    else:
        print("{} arguments".format(n))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
