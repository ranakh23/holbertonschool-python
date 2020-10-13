#!/usr/bin/python3
'''
method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
'''


def minOperations(n):
    result = 0
    number = n
    for i in range(2, number + 1):
        while (number % i == 0):
            result += i
            number /= i
            if number < i:
                break
    return result
