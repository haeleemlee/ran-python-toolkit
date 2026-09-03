# Day 11- Log Parser Function

import re

KPI_PATTERN = re.compile(
    r"(?P<cell>Cell-\d+) MCS=(?P<mcs>\d+) "
    r"BLER=(?P<bler>[\d.]+) TPUT=(?P<tput>[\d.]+)"
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
            records.append(d)
    return records

if __name__ == "__main__":
    records = parse_log("du.log")
    print(f"{len(records)} records parsed")
    for r in records:
        print(r)