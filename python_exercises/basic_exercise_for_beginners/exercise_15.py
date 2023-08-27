# -*- coding: utf-8 -*-
"""Exercise 15: Write a function called exponent(base, exp)
that returns an int value of base raises to the power of exp.

Note here exp is a non-negative integer, and the base is an integer.

Expected output
base = 2
exponent = 5
2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)

base = 5
exponent = 4
5 raises to the power of 4 is: 625 i.e. (5 *5 * 5 *5 = 625)

"""


def solution(base, exp):
    if not isinstance(base, int):
        raise Exception("Base must be integer!")

    if exp < 0:
        raise Exception("Exp must be greater than 0!")

    return base**exp
