# Week1_basics.py

mcs = 22
bler = 0.08
cell = "Cell-1"
print(f"{cell}: MCS = {mcs}, BLER = {bler:.2%}")

bler_list = [0.02, 0.05, 0.12, 0.08, 0.25]
for i, b in enumerate(bler_list):
    status = "PASS" if b < 0.10 else "FAIL"
    print(f"Test {i+1}: BLER = {b:.2%} -> {status}")

result = {"cell": "Cell-1", "mcs": 22, "bler": 0.08, "tput": 245.3}
print(f"Tput is {result["tput"]}Mbps")
for key, value in result.items():
    print(f"{key:10s} = {value}")

def check_bler(bler, threshold = 0.10):
    """If BLER is equal or less than threshold, then PASS"""
    return "PASS" if bler <= threshold else "FAIL"

print(check_bler(0.08)) # PASS
print(check_bler(0.25)) # FAIL

with open ("du.log", "r") as f:
    for line in f:
        if "PRACH" in line:
            print(line.strip())

