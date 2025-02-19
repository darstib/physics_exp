# ZJU 大学物理实验
t = [30.0, 35.2, 41.0, 46.5, 52.0, 57.2, 63.0, 68.8, 74.6, 80.0]  # t 温度 ℃
R = [
    4.900,
    4.995,
    5.097,
    5.204,
    5.311,
    5.405,
    5.512,
    5.619,
    5.726,
    5.825,
]  # R 电阻 10^{-3} Ω
assert len(t) == len(R) == 10


def alpha(i):
    return (R[i + 5] - R[i]) / (R[i] * t[i + 5] - R[i + 5] * t[i])


alphas = [alpha(i) for i in range(5)]
print(f"α = {alphas}")
print(f"α_avg = {sum(alphas) / len(alphas)}")

import numpy as np
import matplotlib.pyplot as plt

# Linear fitting
coefficients = np.polyfit(t, R, 1)
a, b = coefficients

# Generate points for the fitted line
t_fit = np.linspace(min(t), max(t), 100)
R_fit = a * t_fit + b

# Create the plot
plt.figure(figsize=(10, 6))
plt.scatter(t, R, color="blue", label="Experimental Data")
plt.plot(t_fit, R_fit, color="red", label="Fitted Line")

# Customize the plot
plt.xlabel("t / °C")
plt.ylabel("$R_x$ / $10^{-3}$ Ω")
plt.title("$R_x$ - t")
plt.grid(True)
plt.legend()

# Print the fitted equation
print(f"Fitted equation: R = {a:.5f}t + {b:.5f} $(10^{-3}$ Ω)")

plt.savefig("13_doubleBridge.png")
