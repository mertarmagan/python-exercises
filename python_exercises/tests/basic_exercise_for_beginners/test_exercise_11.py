# -*- coding: utf-8 -*-
import pytest

from python_exercises.basic_exercise_for_beginners.exercise_11 import solution


@pytest.mark.parametrize(
    "num, expected",
    [
        (1, "1"),
        (12, "2 1"),
        (7536, "6 3 5 7"),
        (12345, "5 4 3 2 1"),
    ],
)
def test_solution(num, expected):
    assert solution(num) == expected
