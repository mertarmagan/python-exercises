# -*- coding: utf-8 -*-
import pytest

from python_exercises.basic_exercise_for_beginners.exercise_6 import solution


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8], [5]),
        ([5, 10, 15, 20, 25], [5, 10, 15, 20, 25]),
        ([-1, -2, 0, 1, 2], [0]),
        ([-1, 1, 1, 2, 3], []),
    ],
)
def test_solution(numbers, expected):
    assert solution(numbers) == expected
