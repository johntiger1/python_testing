import pytest

@pytest.fixture(scope="module")
def function_to_inject():
    print("\n")
    print("There is a leap of faith. We patch names, and this must be done by string matching."
          "fixtures are run first. this function will be injected. you can return some mocked data, that will be useful for later on")

    myobj = lambda x : None
    myobj.return_value = "OK"
    return myobj