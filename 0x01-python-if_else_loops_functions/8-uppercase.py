#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) in range(97, 123):
            str[i]=chr(ord(str[i]) - 32)
    return str
