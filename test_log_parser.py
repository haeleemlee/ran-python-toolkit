# test_log_parser.py

from log_parser import parse_all
import time
import pytest

def test_bler_within_target():
    for r in parse_all():
        assert r["bler"] <= 0.10, \
            f"{r['source']} {r['cell']}: BLER too high ({r['bler']:.2%})"

@pytest.mark.slow
def test_long_stability_run():
    """실제 안정성 테스트를 흉내낸 오래 걸리는 테스트 (여기선 sleep으로 대체)."""
    time.sleep(2)
    records = parse_all()
    assert len(records) > 0

def test_all_cells_present(records):
    cells = {r["cell"] for r in records}
    expected = {"Cell-1", "Cell-2", "Cell-3"}
    missing = expected - cells
    assert not missing, f"Cells did not come up: {missing}"
    