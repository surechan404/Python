# To print content of all method use "pytest -s"
# Create a new file conftest.py to share fixtures across multiple test files.

import pytest

def test_thirdMethod(preSetup):
    print("This is Third test..")

