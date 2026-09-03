# Day 5 - Reading Files

with open ("du.log", "r") as f:
    for line in f:
        if "PRACH" in line:
            print(line.strip())
