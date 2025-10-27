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

# To print content of all method use "pytest -s"

import pytest

@pytest.fixture(scope="module")
def preTest():
    print("This is module instance..") 
      
def test_firstMethod(preTest):
    print("This is First test..")

def test_secondMethod(preSetup):
    print("This is Second test..")
