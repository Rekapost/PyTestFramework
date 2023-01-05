import pytest
@pytest.yield_fixture()
def setup():
    print("execute once before every test method")
    yield
    print("execute once after every test method")

def testMethod1(setup):
    print("this is test Method1")
def testMethod2(setup):
    print("this is test Method 2")

# pytest -v -s test_pytestYieldFiixture.py