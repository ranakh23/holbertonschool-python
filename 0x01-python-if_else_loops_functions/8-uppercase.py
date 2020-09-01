#!/usr/bin/python3
def uppercase(str):
    new = ""
    for i in range(len(str)):
        if ord(str[i]) in range(97, 123):
            new += chr(ord(str[i]) - 32)
        else:
            new += str[i]
    print("{}".format(new))
