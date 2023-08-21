# -*- coding: utf-8 -*-
import pytest

from python_exercises.basic_exercise_for_beginners.exercise_1 import solution


@pytest.mark.parametrize(
    "num1, num2, expected", [(0, 0, 0), (10, 10, 100), (200, 10, 210)]
)
def test_solution(num1, num2, expected):
    assert solution(num1, num2) == expected
