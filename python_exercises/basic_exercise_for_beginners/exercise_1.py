# -*- coding: utf-8 -*-
"""Exercise 1: Calculate the multiplication and sum of two numbers

Given two integer numbers return their product only if the product is equal to
or lower than 1000, else return their sum.

Given 1:
number1 = 20
number2 = 30

Expected Output:
The result is 600

Given 2:
number1 = 40
number2 = 30

Expected Output:
The result is 70
"""


def solution(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2
