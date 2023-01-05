import pytest
@pytest.yield_fixture()
def setup():
    print("sign up to login")
    yield
    print("sign out to logout ")

def test_signupBYemail(setup):
    print("signup by email test")
def test_signupBYfacebook(setup):
    print("signup by facebook test")
def test_signupBYtwitter(setup):
    print("signup by twitter test")

