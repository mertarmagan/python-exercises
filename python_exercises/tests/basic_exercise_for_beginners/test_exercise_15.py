# -*- coding: utf-8 -*-
import pytest

from python_exercises.basic_exercise_for_beginners.exercise_15 import solution


@pytest.mark.parametrize(
    "base, exp, result",
    [
        (1, 2, 1),
        (2, 1, 2),
        (2, 2, 4),
        (5, 2, 25),
        (5, 4, 625),
    ],
)
def test_solution(base, exp, result):
    assert solution(base, exp) == result


@pytest.mark.parametrize(
    "base, exp",
    [
        (1.0, 1),
        (1, -1),
        (1.0, -10),
    ],
)
def test_solution_raise_on_wrong_input(base, exp):
    with pytest.raises(Exception):
        solution(base, exp)
