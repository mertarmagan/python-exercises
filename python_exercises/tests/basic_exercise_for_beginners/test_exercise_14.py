# -*- coding: utf-8 -*-
import pytest

from python_exercises.basic_exercise_for_beginners.exercise_14 import solution


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, ["*"]),
        (2, ["* *", "*"]),
        (3, ["* * *", "* *", "*"]),
        (4, ["* * * *", "* * *", "* *", "*"]),
        (5, ["* * * * *", "* * * *", "* * *", "* *", "*"]),
    ],
)
def test_solution_(n, expected):
    assert solution(n) == expected
