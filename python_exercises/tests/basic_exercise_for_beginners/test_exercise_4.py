# -*- coding: utf-8 -*-
import pytest

from python_exercises.basic_exercise_for_beginners.exercise_4 import solution


@pytest.mark.parametrize(
    "text, n, expected",
    [
        ("armagan", 2, "magan"),
        ("armagan", 5, "an"),
        ("a", 1, ""),
    ],
)
def test_solution(text, n, expected):
    assert solution(text, n) == expected
