# -*- coding: utf-8 -*-
"""Exercise 6: Display numbers divisible by 5 from a list

Iterate the given list of numbers and print only those numbers which are divisible by 5
"""


def solution(numbers):
    return [num for num in numbers if num % 5 == 0]
