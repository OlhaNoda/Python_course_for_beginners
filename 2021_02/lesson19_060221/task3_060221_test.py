# task3
"""
Task 3 (Optional)
Pytest fixtures with context manager
Create a simple function, which performs any logic of your choice with text data,
which it obtains from a file object, passed to this function ( def test(file_obj) ).
Create a test case for this function using pytest library (https://docs.pytest.org/en/latest/contents.html).
Create pytest fixture, which uses your implementation of the context manager to return a file object,
which could be used inside your function.
"""

import pytest
import math


@pytest.mark.square
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


@pytest.mark.square
def test_square():
    num = 7
    assert 7*7 == 40


@pytest.mark.others
def test_equality():
    assert 10 == 11
