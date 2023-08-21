# -*- coding: utf-8 -*-
"""Exercise 3: Print characters from a string that are present at an even index number

Write a program to accept a string from the user and display characters
that are present at an even index number.

For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
"""


def solution(text):
    return [c for i, c in enumerate(text) if i % 2 == 0]
