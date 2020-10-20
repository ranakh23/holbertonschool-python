#!/usr/bin/python3
"""
0x11. UTF-8 Validation
"""


from itertools import takewhile


def to_bits(bytes):
    """
    Convert bytes to bits
    """
    for byte in bytes:
        num = []
        exp = 1 << 8
        while exp:
            exp >>= 1
            num.append(bool(byte & exp))
            yield num


def validUTF8(data):
    """
    Method that determines if a given data set
    represents a valid UTF-8 encoding.
    """
    bits = to_bits(data)
    for byte in bits:
        # single byte char
        if byte[0] == 0:
            continue

        # multi-byte character
        amount = sum(takewhile(bool, byte))
        if amount <= 1:
            return False
        if amount >= 4:
            return False

        for _ in range(amount - 1):
            try:
                byte = next(bits)
            except StopIteration:
                return False
            if byte[0:2] != [1, 0]:
                return False
    return True
