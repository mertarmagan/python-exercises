# -*- coding: utf-8 -*-
"""Exercise 13: Print multiplication table form 1 to n

Expected Output:
n=1
1

n=2
1 2
2 4

n=3
1 2 3
2 4 6
3 6 9

n=10
1  2  3  4  5  6  7  8  9  10
2  4  6  8  10 12 14 16 18 20
3  6  9  12 15 18 21 24 27 30
4  8  12 16 20 24 28 32 36 40
5  10 15 20 25 30 35 40 45 50
6  12 18 24 30 36 42 48 54 60
7  14 21 28 35 42 49 56 63 70
8  16 24 32 40 48 56 64 72 80
9  18 27 36 45 54 63 72 81 90
10 20 30 40 50 60 70 80 90 100
"""


def solution(n, print_matrix=False):
    if n < 0:
        raise Exception("Given number n is smaller than 1!")

    matrix = []
    max_chars = len(str(n * n))
    for i in range(n):
        row = []
        for j in range(n):
            mult = (i + 1) * (j + 1)
            space = " ".ljust(max_chars - len(str(mult)))
            row.append(mult)
            if print_matrix:
                print((i + 1) * (j + 1), end=space)
        if print_matrix:
            print()
        matrix.append(row)

    return matrix
