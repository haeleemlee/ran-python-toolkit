# Day 2 - List and Loop

bler_list = [0.02, 0.05, 0.12, 0.08, 0.25]
for i, b in enumerate(bler_list):
    status = "PASS" if b <= 0.10 else "FAIL"
    print(f"Test {i+1}: BLER={b:.2%} -> {status}")
