# -*- coding: utf-8 -*-
import pytest

from python_exercises.basic_exercise_for_beginners.exercise_9 import solution


@pytest.mark.parametrize(
    "num, expected",
    [
        (1, True),
        (12, False),
        (121, True),
        (1232144, False),
        (9999, True),
        (12344321, True),
        (123454321, True),
    ],
)
def test_solution(num, expected):
    assert solution(num) == expected
