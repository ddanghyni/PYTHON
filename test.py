import numpy as np
import matplotlib.pyplot as plt

# --- 예제 데이터 다시 생성 --------------------------------------
np.random.seed(42)
T = 100
X = np.sin(np.linspace(0, 8 * np.pi, T)) + 0.3 * np.random.randn(T)  # 예측변수 (X)
Y = np.roll(X, 4) + 0.2 * np.random.randn(T)  # 종속변수 (Y), 약간의 시간지연

# --- 슬라이딩 윈도우 설정 --------------------------------------
window_size = 20  # 20개 시점
stride = 2  # 2칸씩 이동
bins = 4  # 4개 bin으로 이산화

TE_list = []
time_list = []

for start in range(0, T - window_size, stride):
    end = start + window_size
    X_win = X[start:end]
    Y_win = Y[start:end]

    # 1. 이산화 (binning)
    X_bins = np.linspace(X_win.min(), X_win.max(), bins + 1)
    Y_bins = np.linspace(Y_win.min(), Y_win.max(), bins + 1)

    X_digitized = np.digitize(X_win, X_bins) - 1
    Y_digitized = np.digitize(Y_win, Y_bins) - 1

    # 2. Triplets (X_t, Y_t, Y_{t+1})
    triplets = []
    for t_ in range(window_size - 1):
        triplets.append((Y_digitized[t_ + 1], Y_digitized[t_], X_digitized[t_]))

    # 3. joint count
    counts = np.zeros((bins, bins, bins), dtype=int)
    for i, j, k in triplets:
        if (0 <= i < bins) and (0 <= j < bins) and (0 <= k < bins):
            counts[i, j, k] += 1
    N = counts.sum()

    # 4. joint probability
    p_xyz = counts / N

    # 5. conditional probabilities
    p_jk = p_xyz.sum(axis=0)
    p_j = p_jk.sum(axis=1)

    TE = 0
    for i in range(bins):
        for j in range(bins):
            for k in range(bins):
                if p_xyz[i, j, k] > 0 and p_jk[j, k] > 0 and p_j[j] > 0:
                    p1 = p_xyz[i, j, k] / p_jk[j, k]
                    p2 = p_xyz[i, j, :].sum() / p_j[j]
                    TE += p_xyz[i, j, k] * np.log2(p1 / p2)

    TE_list.append(TE)
    time_list.append(end)

# --- 결과 시각화 ----------------------------------------------
fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

axes[0].plot(X, label='X (input)', color='blue')
axes[0].legend()
axes[0].set_ylabel('X value')

axes[1].plot(Y, label='Y (target)', color='green')
axes[1].legend()
axes[1].set_ylabel('Y value')

axes[2].plot(time_list, TE_list, marker='o', label='TE(X → Y)', color='red')
axes[2].legend()
axes[2].set_ylabel('Transfer Entropy')
axes[2].set_xlabel('Time (window end point)')

plt.suptitle("X, Y,TE time series")
plt.tight_layout()
plt.show()
