#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = [0, 0]
    b = [0, 0]
    for i in range(len(tuple_a)):
        a[i] = tuple_a[i]
    for j in range(len(tuple_b)):
        b[j] = tuple_b[j]
    c = a[0] + b[0]
    d = a[1] + b[1]
    return (c, d)
