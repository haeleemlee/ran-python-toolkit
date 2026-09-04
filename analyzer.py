# analyzer.py

import pandas as pd
from log_parser import parse_all

def build_dataframe(logdir=None):
    """로그 디렉토리를 읽어 KPI DataFrame으로 반환한다"""
    records = parse_all(logdir)
    return pd.DataFrame(records)

def add_pass_fail(df, threshold=0.10):
    """BLER 기준으로 PASS/FAIL column을 추가하고 pass rate를 함께 반환한다"""
    df = df.copy()
    df["result"] = df["bler"].apply(lambda b: "PASS" if b <= 0.10 else "FAIL")
    pass_rate = (df["result"] == "PASS").mean()
    return df, pass_rate

def summarize_by_mcs(df):
    """MCS별 평균 BLER, 최대 TPUT, 표본 수를 요약한다."""
    summary = df.groupby("mcs").agg(
        avg_bler = ("bler", "mean"),
        max_tput = ("tput", "max"),
        samples = ("bler", "count"),
    )
    return summary

def max_tput_by_mcs(df, mcs):
    """특정 MCS에서 기록된 최대 throughput을 변환한다."""
    return df[df["mcs"] == mcs]["tput"].max()

if __name__== "__main__":
    df = build_dataframe()
    print(df.shape)

    print(df.head())
    print(df.info())
    print(df.describe())

    fails = df[df["bler"] > 0.10]
    fails_index = df["bler"] > 0.10
    high_mcs = df[(df["mcs"] >= 21) & (df["tput"] < 210)]
    
    print(fails)
    print(fails_index)
    print(high_mcs)

    df, pass_rate = add_pass_fail(df)
    print(f"Pass rate: {pass_rate:.1%}")

    summary = summarize_by_mcs(df)    
    print(summary) 

    maxTputByMcs = max_tput_by_mcs(df, 15)
    print(f"Max Tput by MCS=15: {maxTputByMcs}")
   # df.to_csv("results.csv", index=False)
   # df.to_excel("results.xlsx", index=False)