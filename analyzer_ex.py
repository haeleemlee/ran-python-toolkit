# analyzer.py

import pandas as pd
#from log_parser import parse_log
from log_parser import parse_all

#records = parse_log("du.log")
records = parse_all("logs")
df = pd.DataFrame(records)
print(df.head())
print(df.info())
print(df.describe())


fails = df[df["bler"] > 0.10]
fails_index = df["bler"] > 0.10
high_mcs = df[(df["mcs"] >= 21) & (df["tput"] < 210)]
 
print(fails)
print(fails_index)
print(high_mcs)

print(fails.head())
print(fails.info())
print(fails.describe())

summary = df.groupby("mcs").agg(
    avg_bler = ("bler", "mean"),
    max_tput = ("tput", "max"),
    samples = ("bler", "count"),
)
print(summary) 

df["result"] = df["bler"].apply(lambda b: "PASS" if b <= 0.10 else "FAIL")
pass_rate = (df["result"] == "PASS").mean()
print(f"Pass rate: {pass_rate:.1%}")

df.to_csv("results.csv", index=False)
df.to_excel("results.xlsx", index=False)