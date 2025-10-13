# 2 Fixtures

# Fixtures - A fixture in Pytest is a reusable piece of code that runs before (and optionally after) a test function.
# It’s mainly used to set up test data, test environments, or resources like browsers, databases, or files.

# In Fixture method, we set the scope of the fixture to function, class, module, or session.
# The default scope is function, meaning the fixture is invoked once per test function.
# The module scope means the fixture is invoked once per module, and the session scope means it’s invoked once per test session.
# The class scope means the fixture is invoked once per class.

# To print content of all method use "pytest -s"

import pytest

@pytest.fixture
def preTest(scope="function"):
    print("This is from Fixture...") 
     
def test_mainMethod(preTest):
    print("Test main method execution..")

def test_secondMethod(preTest):
    print("Second test method execution..")
