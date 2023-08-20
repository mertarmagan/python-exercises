# -*- coding: utf-8 -*-
"""Exercise 2: Print the sum of the current number and the previous number

Write a program to iterate the first 10 numbers, and in each iteration,
print the sum of the current and previous number.
"""


def solution(n):
    output = []
    for i in range(1, n + 1):
        output.append(i + i - 1)
        print(f"previous:{i-1} current:{i} total:{i+i-1}")

    return output
