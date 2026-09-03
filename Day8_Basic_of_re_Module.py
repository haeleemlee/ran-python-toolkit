# Day 8 - Basic of re Module

import re
line = "[00:00:02] Cell-1 MCS=22 BLER=0.08 TPUT=245.3"
m = re.search(r"MCS=(\d+)", line)
print(m.group(1)) # 22

m = re.search(r"MCS=(?P<mcs>\d+) BLER=(?P<bler>[\d.]+)", line)
print(m.group("mcs"))
print(f"MCS = {m.group("mcs")}")
print(f"BLER = {m.group("bler")}")
print(f"Total match = {m.group(0)}")