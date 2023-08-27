# -*- coding: utf-8 -*-
import pytest

from python_exercises.basic_exercise_for_beginners.exercise_12 import solution


@pytest.mark.parametrize(
    "income, expected_tax",
    [
        (0, 0),
        (10_000, 0),
        (11_000, 100),
        (20_000, 1000),
        (25_000, 2000),
        (45_000, 6000),
    ],
)
def test_solution(income, expected_tax):
    assert solution(income) == expected_tax
