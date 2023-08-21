# -*- coding: utf-8 -*-
import pytest

from python_exercises.basic_exercise_for_beginners.exercise_7 import solution


@pytest.mark.parametrize(
    "text, substring, expected",
    [
        ("Emma is good developer. Emma is a writer", "Emma", 2),
        ("Emma is good developer. Emma is a writer", "emma", 0),
        ("Emma is good developer. Emma is a writer", "writer", 1),
        ("aa", "a", 2),
        ("aa", "aa", 1),
        ("aa", "aaa", 0),
    ],
)
def test_solution(text, substring, expected):
    assert solution(text, substring) == expected
