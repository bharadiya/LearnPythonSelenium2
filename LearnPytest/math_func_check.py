from LearnPytest.doMathFunctions import doAddition, doMul, doSub
import pytest

@pytest.mark.parametrize('a,b,sum',
                         [
                             (5, 5, 10),
                             (2, 3, 6),
                             (5, 6, 11)
                         ]
                         )
def test_check_addition(a, b, sum):
    assert doAddition(a, b) == sum

@pytest.mark.regression
def test_check_additionOfFloatingNumbers():
    assert doAddition(5.5, 5.5) == 10

def test_check_isMultiplicationCorrect():
    assert doMul(5, 5) == 24

def test_check_isNumberGreaterThan0():
    assert doSub(6, 5) >= 0


# - Every particular method is test case
# - v  > Detailed  information
# - k  > will run test case according to method signature name eg - pytest math_func_check.py -k "add and Mul" -v

