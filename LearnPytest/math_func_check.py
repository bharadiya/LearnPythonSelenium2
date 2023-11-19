from LearnPytest.doMathFunctions import doAddition, doMul, doSub
import pytest

@pytest.mark.parametrize('a,b,sum',
                         [
                             (5, 5, 10),
                             (2, 3, 5),
                             (5, 6, 11)
                         ]
                         )
def test_check_addition(a, b, sum):
    assert doAddition(a, b) == sum

def test_check_additionOfFloatingNumbers():
    assert doAddition(5.5, 5.5) == 11.0

def test_check_isMultiplicationCorrect():
    assert doMul(5, 5) == 25

def test_check_isNumberGreaterThan0():
    assert doSub(6, 5) >= 0


def setup_module(module):
    print("------------------------set up method-----------------------")
def teardown_module(module):
    print("-----------------Tear down method-----------------------------")
# - Every particular method is test case
# - v  > Detailed  information
# - k  > will run test case according to method signature name eg - pytest math_func_check.py -k "add and Mul" -v

