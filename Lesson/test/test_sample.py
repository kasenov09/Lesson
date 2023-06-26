from lesson import add_one, division, sum_
import pytest


def test_answer():
    assert add_one(3) == 4
    assert add_one(9) == 10

def test_division():
    assert division(3, 3) == 1
    assert division(9, 3) == 3

def testt_division2():
    with pytest.raises(ZeroDivisionError):
        division(9, 0)


def test_sum():
    t = [[1, 2, 3], [3, 4, 7],[8, 9, 13]]
    for s in t:
        assert  sum_(s[0],s[1] == s[2])



