# Day 4 - Function

def check_bler(bler, threshold=0.10):
    """BLER이 임계값 이하면 PASS"""
    return "PASS" if bler < threshold else "FAIL"

print(check_bler(0.08)) # PASS
print(check_bler(0.25)) # FAIL

print(check_bler(0.08, 0.01))
print(check_bler(0.08, 0.08))
print(check_bler(0.08, 0.0800001))
print(check_bler(0.09))
print(check_bler(0.099))
print(check_bler(0.10))