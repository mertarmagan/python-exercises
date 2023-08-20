# -*- coding: utf-8 -*-
from python_exercises.basic_exercise_for_beginners.exercise_2 import solution


def test_solution():
    expected = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    assert solution(10) == expected
