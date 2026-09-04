# test_analyzer.py
import pytest
from analyzer import max_tput_by_mcs

def test_records_fixture_reaches_other_file(records):
    """ conftest.py의 records fixture가 이 파일에서도 import 없이 그대로 쓰인다."""
    assert len(records) == 15

@pytest.mark.parametrize("mcs, min_tput", [
    (10, 50.0),
    (22, 200.0),
    (27, 350.0)
])

def test_tput_by_mcs(df, mcs, min_tput):
    actual = max_tput_by_mcs(df, mcs)
    assert actual >= min_tput, \
        f"MCS{mcs}: max_tput {actual} < 기준 {min_tput}"
