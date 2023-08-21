# -*- coding: utf-8 -*-
import pytest

from python_exercises.basic_exercise_for_beginners.exercise_3 import solution


@pytest.mark.parametrize(
    "text, expected",
    [
        ("abcdefg", ["a", "c", "e", "g"]),
        ("armagansari", ["a", "m", "g", "n", "a", "i"]),
        ("", []),
        ("a", ["a"]),
        ("aa", ["a"]),
    ],
)
def test_solution(text, expected):
    assert solution(text) == expected
