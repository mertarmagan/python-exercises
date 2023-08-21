# -*- coding: utf-8 -*-
import pytest

from python_exercises.basic_exercise_for_beginners.exercise_5 import solution


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1], True),
        ([1, 2, 1], True),
        ([-1, -1], True),
        ([1, 2], False),
        ([1, 2, 3], False),
        ([1, 1, 2], False),
    ],
)
def test_solution(numbers, expected):
    assert solution(numbers) == expected
