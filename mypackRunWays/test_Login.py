import pytest
@pytest.yield_fixture()
def setup():
    print(" login to url ")
    yield
    print("closing browser after login ")

def test_loginBYemail(setup):
    print("login by email test")
def test_loginBYfacebook(setup):
    print("login by facebook test ")
def test_loginBYtwitter(setup):
    print("login by twitter test")


#  pytest -v -s UnitTestFramework/mypackRunWays/test_SignUp.py