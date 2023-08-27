# -*- coding: utf-8 -*-
import pytest

from python_exercises.basic_exercise_for_beginners.exercise_13 import solution


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, []),
        (1, [[1]]),
        (2, [[1, 2], [2, 4]]),
        (3, [[1, 2, 3], [2, 4, 6], [3, 6, 9]]),
        (4, [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]]),
    ],
)
def test_solution(n, expected):
    assert solution(n) == expected


def test_solution_raise_on_wrong_input():
    with pytest.raises(Exception):
        solution(-1)
