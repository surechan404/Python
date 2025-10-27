
import pytest


@pytest.fixture(scope="session")
def preSetup():
    print("This is session instance (Only)...") 