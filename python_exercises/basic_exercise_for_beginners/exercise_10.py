# -*- coding: utf-8 -*-
"""Exercise 10: Create a new list from a two list using the following condition

Create a new list from a two list using the following condition

Given a two list of numbers, write a program to create a new list such that
the new list should contain odd numbers from the first list and
even numbers from the second list.

Given:

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

Expected Output:

result list: [25, 35, 40, 60, 90]
"""


def solution(list1, list2):
    new_list1 = [n for n in list1 if n % 2 == 1]
    new_list2 = [n for n in list2 if n % 2 == 0]
    return new_list1 + new_list2
