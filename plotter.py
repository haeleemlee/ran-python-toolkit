# plotter.py

import matplotlib.pyplot as plt
import numpy as np
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


def plot_tput_cdf(df, outpath="tput_cdf.png"):
    """THroughput의 경험적 CDF(누적분포함수)를 그리고 T_5%(5 percentile 처리율)를 구한다.
    
    SLS에서 쓰는 cell-edge 성능 지표 (T_5%)와 같은 개념.
    "사용자의 95%가 이 값 이상의 처리율을 낸다"는 하한선 
    """

    data = np.sort(df["tput"].values)
    cdf = np.arange(1, len(data) + 1) / len(data)
    t5 = np.interp(0.05, cdf, data)

    plt.figure()
    plt.plot(data, cdf)
    plt.axhline(0.05, color="red", linestyle="--", label="5%-tile")
    plt.axvline(t5, color="red", linestyle=":")
    plt.xlabel("Throughput (Mbsp)")
    plt.ylabel("CDF")
    plt.title(f"Throughput CDF (T_5% \u2248 {t5:.1f} Mbps)")
    plt.legend()
    plt.savefig(outpath, dpi=150)
    print(f"Saved: {outpath} (T_5% = {t5:.1f} Mbps)")
    return t5

def plot_summary(df, outpath="summary.png"):
    """Throughput와 BLER 추이를 2단 subplot 한 장으로 요약한다."""

    fig, axes = plt.subplots(2, 1, figsize=(8, 8))
    axes[0].plot(df["tput"].values)
    axes[0].set_title("Throughput")
    axes[1].semilogy(df["bler"].values)
    axes[1].set_title("BLER")
    fig.tight_layout()
    fig.savefig(outpath, dpi=150)
    print(f"Saved: {outpath}")

if __name__ == "__main__":
    df = build_dataframe()
    print(df.shape)
    print(df.columns)
    plot_bler_curve(df)
    plot_tput_cdf(df)
    plot_summary(df)