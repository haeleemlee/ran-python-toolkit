# conftest.py

import pytest
from log_parser import parse_all
from analyzer import build_dataframe

@pytest.fixture
def records():
    print("\n[setup] Start log parsing...")
    data = parse_all()
    yield data
    print("[teardown] Finished the test and wrapping up now...")

@pytest.fixture
def df():
    return build_dataframe()
