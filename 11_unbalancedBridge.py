# ZJU 非平衡电桥
t = [30, 35, 40, 45, 50, 55, 60, 65]  # ℃
U = [40.0, 45.5, 51.2, 56.8, 62.7, 67.5, 72.8, 78.0]  # mV
eta = 1.3 * 1000  # mV
stand_alpha = 0.00428  # ℃^-1


def get_avg(lt):
    return sum(lt) / len(lt)


def get_alpha(t, U):
    return 4 * U / (t * (eta - 2 * U))


alphas = [get_alpha(ti, Ui) for ti, Ui in zip(t, U)]
avg_alpha = get_avg(alphas)
print(alphas, avg_alpha)
# [0.004371584699453552, 0.004301075268817204, 0.0042752171008684035, 0.0042556379710796425, 0.004270389919972757, 0.004213811939133828, 0.004204204204204204, 0.004195804195804196] 0.004260965662416723
E1 = abs(avg_alpha - stand_alpha) / stand_alpha * 100
print(f"E1: {E1:.5f}%")

R = [56.81, 57.90, 58.99, 60.10, 61.15, 62.28, 63.31, 64.35]

from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt


def line(x, a, b):
    return a * x + b


popt, _ = curve_fit(line, t, R)
a, b = popt
print(f"Rt = {a:.2f}t + {b:.2f}")
print(a, b)
t_fit = np.linspace(30, 65, 100)
R_fit = line(t_fit, a, b)
alpha_ = a / b
print(f"alpha_: {alpha_:.5f}")
E2 = abs(alpha_ - stand_alpha) / stand_alpha * 100
print(f"E2: {E2:.5f}%")
plt.figure(figsize=(10, 6))
plt.plot(t, R, "bo", label="Measured data")
plt.plot(t_fit, R_fit, "r-", label="Fitted line")
plt.xlabel("Temperature (°C)")
plt.ylabel("Resistance (Ω)")
plt.legend()
plt.title("$R_t$-t Curve")
# 添加拟合的直线的公式
plt.text(
    0.3,
    0.6,
    f"$R_t$ = {a:.2f}t + {b:.2f}",
    transform=plt.gca().transAxes,
    fontsize=12,
    verticalalignment="top",
)
plt.grid(True)
plt.savefig("11_R-t.png")
