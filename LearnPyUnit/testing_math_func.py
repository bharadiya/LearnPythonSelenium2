from LearnPyUnit.math_function import add, mul
import pytest


@pytest.mark.parametrize('a ,b, sum',
                         [
                             (5, 5, 10),
                             (2, 3, 5),
                             (6, 5, 11)
                         ]
                         )
def test_addition(a, b, sum):
    assert add(a, b) == sum


def test_product():
    assert mul(5, 5) == 25
