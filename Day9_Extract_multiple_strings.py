# Day 9 - Extract multiple strings or values

import re
line = "[00:00:02] Cell-1 MCS=22 BLER=0.08 TPUT=245.3"

pattern = r"(Cell-\d+) MCS=(\d+) BLER=([\d.]+) TPUT=([\d.]+)"
m = re.search(pattern, line)
if m:
    cell, mcs, bler, tput = m.groups()
    print(cell, int(mcs), float(bler), float(tput)) 


pattern2 = r"(?P<cell>Cell-\d+) MCS=(?P<mcs>\d+) BLER=(?P<bler>[\d.]+) TPUT=(?P<tput>[\d.]+)"
m2 = re.search(pattern2, line)
print(m2.group("bler"))
print(m2.groupdict())
