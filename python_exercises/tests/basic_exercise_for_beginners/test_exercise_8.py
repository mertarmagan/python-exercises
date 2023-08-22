# -*- coding: utf-8 -*-
import pytest

from python_exercises.basic_exercise_for_beginners.exercise_8 import solution


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, [[1]]),
        (2, [[1], [2, 2]]),
        (3, [[1], [2, 2], [3, 3, 3]]),
        (4, [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4]]),
        (5, [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5, 5]]),
    ],
)
def test_solution(n, expected):
    assert solution(n) == expected
