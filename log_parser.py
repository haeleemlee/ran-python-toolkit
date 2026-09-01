# Day 11- Log Parser Function

import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_LOG_DIR = SCRIPT_DIR/"logs"

KPI_PATTERN = re.compile(
    r"(?P<cell>Cell-\d+) MCS=(?P<mcs>\d+) "
    r"BLER=(?P<bler>[\d.]+) TPUT=(?P<tput>[\d.]+) "
    r"SINR=(?P<sinr>-?[\d.]+)"
)

def parse_log(filepath):
    """로그 파일을 읽어 KPI 레코드 리스트를 반환한다.

    각 레코드는 {cell, mcs, bler, tput} 형태의 딕셔너리.
    패턴에 맞지 않는 줄은 무시한다.
    """
    records = []
    with open (filepath, encoding="utf-8") as f:
        for line in f:
            m = KPI_PATTERN.search(line)
            if not m:
                continue 
            d = m.groupdict()
            d["mcs"] = int(d["mcs"])
            d["bler"] = float(d["bler"])
            d["tput"] = float(d["tput"])
            d["sinr"] = float(d["sinr"])
            records.append(d)
    return records

def parse_all(logdir=None, pattern="*.log"):
    """디렉터리 내 모든 로그 파일을 파싱해 하나의 리스트로 합친다.
    
    각 레코드에 source(파일명)를 추가해 나중에 추적 가능하게 한다.
    """
    logdir = logdir or DEFAULT_LOG_DIR
    records = []
    for f in sorted(Path(logdir).glob(pattern)):
        for r in parse_log(f):
            r["source"] = f.name
            records.append(r)
    return records    

PRACH_EXPECTED = 2_000_000

PRACH_PATTERN = re.compile(
    r"(?P<cell>Cell-\d+) PRACH threshold: (?P<value>\d+)"
)

def find_prach_anomaly_all(logdir=None, pattern="*.log", tolerance=0.5):
    """디렉터리 내 모든 로그파일에서 PRACH anomaly를 찾는다.
    각 결과에 source(파일명)를 추가한다.
    """
    """PRACH threshold가 설정값 대비 비정상적으로 낮은 줄을 찾는다.

    tolerance=0.5이면 기대값의 50% 미만인 값을 비정상으로 본다.
    반환: (줄번호, 셀, 값) tuple의 list
    """

    logdir = logdir or DEFAULT_LOG_DIR
    anomalies = []
    floor = PRACH_EXPECTED * tolerance
    for f in sorted(Path(logdir).glob(pattern)):
        with open (f, encoding="utf-8") as fh:
            for lineno, line in enumerate(fh, start=1):
                m = PRACH_PATTERN.search(line)
                if not m:
                    continue
                value = int(m.group("value"))
                if value < floor:
                    anomalies.append((f.name, lineno, m.group("cell"), value))
    return anomalies


def find_prach_anomaly(filepath, tolerance=0.5):
    """PRACH threshold가 설정값 대비 비정상적으로 낮은 줄을 찾는다.

    tolerance=0.5이면 기대값의 50% 미만인 값을 비정상으로 본다.
    반환: (줄번호, 셀, 값) tuple의 list
    """

    anomalies = []
    floor = PRACH_EXPECTED * tolerance
    with open (filepath, encoding="utf-8") as f:
        for lineno, line in enumerate(f, start=1):
            m = PRACH_PATTERN.search(line)
            if not m:
                continue
            value = int(m.group("value"))
            if value < floor:
                anomalies.append((lineno, m.group("cell"), value))
    return anomalies


if __name__ == "__main__":
    #records = parse_log("du.log")
    records = parse_all()
    print(f"{len(records)} KPI records parsed")

    #anomalies = find_prach_anomaly("du.log")
    anomalies = find_prach_anomaly_all()
    print(f"\n{len(anomalies)} PRACH anomalies found")
    for source, lineno, cell, value in anomalies:
        print(f" {source} line {lineno} ({cell}): {value:,} "
              f"(expected ~{PRACH_EXPECTED:,})")

    print(f"Len(records)= {len(records)}")