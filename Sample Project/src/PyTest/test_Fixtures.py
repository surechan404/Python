# 2 Fixtures

# Fixtures - A fixture in Pytest is a reusable piece of code that runs before (and optionally after) a test function.
# It’s mainly used to set up test data, test environments, or resources like browsers, databases, or files.

# In Fixture method, we set the scope of the fixture to function, class, module, or session.
# The default scope is function, meaning the fixture is invoked before every test function.
# The module scope means the fixture is invoked once per module, and the session scope means it’s invoked once per test session.
# The class scope means the fixture is invoked once per class.
"""
Scope	When it runs
function	Before each test function (default)
class	Once per test class
module	Once per module (file)
package	Once per package (pytest 8+)
session	Once per test session/execution """

# Notes:
# 1. To print content of all method use "pytest -s"
# 2. In terminal, move to the directory where the test file is located and run the command:
# 3. pytest test_Fixtures.py -s
# 4. yield keyword is used to define teardown code that runs after the test function completes.
# 5. Create a new file conftest.py to share fixtures across multiple test files.
# 6. Use @pytest.mark.skip to skip a test method.
# 7. Use @pytest.mark.finalM to mark a test method (custom marker) to group/filter and run specific test methods.

import pytest

@pytest.fixture(scope="module")
def test_preTest():
    print("This is module instance..") 
    return "pass"
      
@pytest.fixture(scope="function")
def test_secondPreTest():
    print("This is Second Pre-instance..") 
    yield
    print("This is Second Post-instance..")


def test_firstMethod(preTest, secondPreTest):
    print("This is First test..")
    assert preTest == "pass"

@pytest.mark.skip
def test_secondMethod(preSetup, secondPreTest):
    print("This is Second test..")

@pytest.mark.finalM
def test_finalMethod():
    print("This is Final method..")    

@pytest.mark.finalM
def test_finalMethod2():
    print("This is Final method2..")    

