# -*- coding: utf-8 -*-
"""Exercise 8: Print the following pattern

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""


def solution(n):
    matrix = []
    for i in range(n + 1):
        row = []
        for j in range(i):
            print(i, end=" ")
            row.append(i)
        if len(row) != 0:
            matrix.append(row)
        print()
    return matrix
