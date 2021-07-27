# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any code should be wrapped in method only
# Method name should have sense
# -k stands for method name execution, -s logs in output, -v more info metadata
# you can run specific file with py.test
# you can mark (tag) tests @pytest.mark.smoke and then run with -m
# @pytest.mark.xfail
#
import pytest


@pytest.mark.smoke
def test_first_program(setup):
    print("Hello world!")


@pytest.mark.xfail
def test_second_creditcard():
    print("Good Morning")


def test_cross_browser(cross_browser):
    print(cross_browser)