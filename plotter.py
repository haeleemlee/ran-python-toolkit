# plotter.py

import matplotlib.pyplot as plt
from analyzer import build_dataframe

def plot_bler_curve(df, outpath="bler_curve.png"):
    """MCS별 SINR-BLER 그래프를 로그 스케일로 그려 파일로 저장한다
    
    outpath를 안 주면 실행한 디렉터리에 bler_curve.png로 지정된다. 
    """

    plt.figure(figsize = (8, 5))
    for mcs, g in df.groupby("mcs"):
        plt.semilogy(g["sinr"], g["bler"], marker="o", label=f"MCS{mcs}")
    plt.axhline(0.1, color="red", linestyle="--", label="10% target")
    plt.xlabel("SINR (dB)")
    plt.ylabel("BLER")
    plt.legend()
    plt.grid(True, which="both")
    plt.savefig("bler_curve.png", dpi=150)
    print(f"Saved: {outpath}")

if __name__ == "__main__":
    df = build_dataframe()
    print(df.shape)
    print(df.columns)
    plot_bler_curve(df)
    