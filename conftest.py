import os

import pytest

@pytest.fixture
def get_test_name():
    test_name = os.environ.get("PYTEST_CURRENT_TEST")
    print(test_name)
    return test_name
