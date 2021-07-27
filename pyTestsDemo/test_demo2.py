# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any code should be wrapped in method only
# Method name should have sense
# -k stands for method names execution, -s for logging output, -v for giving more info metadata
# you can run specific file with py.test <filename>
# You can mark (tag) tests @pytest.mark.smoke and then run with -m
# you can skip tests with @pytest.mark.skip
# fixture is used as setUp and tearDown methods for testcases - conftest is used to generalize fixture
# and make it available to all test cases
# datadriven and parameterization can be done with return statements in tuple format
# when you define fixture scope to class only, it will run once before class initiates & ends
# py.test --html=report.html -s -v --capture=tee-sys


import pytest


@pytest.mark.smoke
# @pytest.mark.skip
def test_first_program():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings do not match"


def test_second_program_creditcard():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition do not match"
