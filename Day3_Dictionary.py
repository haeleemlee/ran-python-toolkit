# Day 3 - Dictionary

result = {"cell":"Cell-1", "mcs":22, "bler":0.08, "tput":245.3}
print(result["tput"])
for key, value in result.items():
    print(f"{key:10s} = {value}")