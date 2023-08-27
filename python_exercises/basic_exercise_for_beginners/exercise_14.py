# -*- coding: utf-8 -*-
"""Exercise 14: Print downward Half-Pyramid Pattern with Star (asterisk)

* * * * *
* * * *
* * *
* *
*
"""


def solution(n, char="*", print_row=False):
    rows = []
    for i in range(n, 0, -1):
        row = " ".join(char * i)
        rows.append(row)
        if print_row:
            print(row)
    return rows
