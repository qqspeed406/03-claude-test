"""绘制标准正态分布曲线，并在曲线下方填充颜色。

输出 gaussian.png（150 dpi）。
"""

import matplotlib

# 只保存文件、不弹窗，使用非交互后端。
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

# 中文标签需要指定含 CJK 字形的字体，否则会显示为方块。
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False


def main():
    x = np.linspace(-5, 5, 500)
    y = np.exp(-(x**2) / 2) / np.sqrt(2 * np.pi)

    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(x, y, color="#1f4e79", linewidth=2)
    ax.fill_between(x, y, color="#1f4e79", alpha=0.25)

    ax.set_title("标准正态分布")
    ax.set_xlabel("x")
    ax.set_ylabel("概率密度")

    fig.tight_layout()
    fig.savefig("gaussian.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    main()
