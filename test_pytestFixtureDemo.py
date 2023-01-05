import pytest
@pytest.fixture()
def setup():
    print(" execute once before every test method")
def testMethod1(setup):
    print("this is test method 1")

def testMethod2(setup):
    print("this is test method 2")


# pytest -v -s test_pytestFixtureDemo.py