# -*- coding: utf-8 -*-
import pytest

from python_exercises.basic_exercise_for_beginners.exercise_10 import solution


@pytest.mark.parametrize(
    "list1, list2, expected",
    [
        ([], [], []),
        ([1], [], [1]),
        ([0, 4], [2, 3, 5], [2]),
        ([1, 2, 3], [1, 3, 5], [1, 3]),
        ([10, 20, 25, 30, 35], [40, 45, 60, 75, 90], [25, 35, 40, 60, 90]),
    ],
)
def test_solution(list1, list2, expected):
    assert solution(list1, list2) == expected
