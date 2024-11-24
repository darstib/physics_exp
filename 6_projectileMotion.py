# 作图代码来自: https://github.com/TonyCrane/ZJU-General-Physics-Experiment-I/blob/master/%E6%8A%9B%E5%B0%84%E4%BD%93%E8%BF%90%E5%8A%A8%E7%9A%84%E7%85%A7%E7%9B%B8%E6%B3%95%E7%A0%94%E7%A9%B6/code.py

import matplotlib.pyplot as plt
import numpy as np

plt.rc("font", family="Source Han Serif CN", size=13, weight="bold")
plt.figure(figsize=(10, 10))

# xs = [0.8, 7.6, 14.0, 21.0, 27.6, 34.2, 41.0, 47.2, 54.3, 61.0, 67.0]
# ys = [20.8, 13.9, 8.9, 5.1, 3.4, 3.1, 5.0, 8.5, 13.5, 18.9, 26.8]
xs = [4.0, 10.8, 17.5, 24.5, 31.5, 38.5, 45.5, 52.5, 59.2, 66.3, 73.1]
ys = [5.3, 3.0, 2.4, 3.5, 6.5, 11.0, 17.0, 25.1, 34.6, 45.7, 58.7]

assert len(xs) == len(ys)
length = len(xs)
vxs = [round(b - a, 1) for a, b in zip(xs, xs[1:])]
vys = [round(b - a, 1) for a, b in zip(ys, ys[1:])]
ays = [round(b - a, 1) for a, b in zip(vys, vys[1:])]
print(xs, ys, vxs, vys, ays, sep="\n")
ts = list(range(length))

plt.subplot(321)
plt.scatter(range(len(xs)), xs)
plt.title("x-t", weight="bold", size=20)
# plt.xlabel("t/T", weight="bold", size=16)
plt.ylabel("x/cm", weight="bold", size=16)
plt.grid(True)

linear_model = np.polyfit(ts, xs, 1)
print(f"x-t: x = {linear_model[0]} * t + {linear_model[1]}")
linear_model_fn = np.poly1d(linear_model)
equation_x = f"x = {linear_model[0]:.1f}t + {linear_model[1]:.1f}"
plt.xlabel(f"t/T\n{equation_x}", weight="bold", size=16)
t_s = np.arange(0, length)
plt.plot(t_s, linear_model_fn(t_s), color="orange", linestyle="--")

plt.subplot(322)
plt.scatter(range(len(ys)), ys)
plt.title("y-t", weight="bold", size=20)
# plt.xlabel("t/T", weight="bold", size=16)
plt.ylabel("y/cm", weight="bold", size=16)
plt.grid(True)

linear_model = np.polyfit(ts, ys, 2)
print(f"x-t: y = {linear_model[0]} * t^2 + {linear_model[1]} * t + {linear_model[2]}")
linear_model_fn = np.poly1d(linear_model)
equation_y = (
    f"y = {linear_model[0]:.1f}t² + {linear_model[1]:.1f}t + {linear_model[2]:.1f}"
)
plt.xlabel(f"t/T\n{equation_y}", weight="bold", size=16)
t_s = np.arange(0, length)
plt.plot(t_s, linear_model_fn(t_s), color="orange", linestyle="--")

plt.subplot(323)
plt.scatter(np.arange(0.5, len(vxs) + 0.5), vxs)
plt.title("$v_x$-t", weight="bold", size=20)
# plt.xlabel("t/T", weight="bold", size=16)
plt.ylabel("$v_x$/(cm/T)", weight="bold", size=16)
plt.grid(True)

linear_model = np.polyfit(np.arange(0.5, len(vxs) + 0.5), vxs, 1)
print(f"vx-t: vx = {linear_model[0]} * t + {linear_model[1]}")
linear_model_fn = np.poly1d(linear_model)
equation_vx = f"$v_x$ = {linear_model[0]:.1f}t + {linear_model[1]:.1f}"
plt.xlabel(f"t/T\n{equation_vx}", weight="bold", size=16)
t_s = np.arange(0, length)
plt.plot(t_s, linear_model_fn(t_s), color="orange", linestyle="--")
plt.ylim(0, length)

plt.subplot(324)
plt.scatter(np.arange(0.5, len(vys) + 0.5), vys)
plt.title("$v_y$-t", weight="bold", size=20)
# plt.xlabel("t/T", weight="bold", size=16)
plt.ylabel("$v_y$/(cm/T)", weight="bold", size=16)
plt.grid(True)

linear_model = np.polyfit(np.arange(0.5, len(vys) + 0.5), vys, 1)
print(f"vy-t: vy = {linear_model[0]} * t + {linear_model[1]}")
linear_model_fn = np.poly1d(linear_model)
equation_vy = f"$v_y$ = {linear_model[0]:.1f}t + {linear_model[1]:.1f}"
plt.xlabel(f"t/T\n{equation_vy}", weight="bold", size=16)
t_s = np.arange(0, length)
plt.plot(t_s, linear_model_fn(t_s), color="orange", linestyle="--")
# plt.ylim(0, length)

plt.subplot(325)
plt.scatter(np.arange(1, len(ays) + 1), ays)
plt.title("$a_y$-t", weight="bold", size=20)
# plt.xlabel("t/T", weight="bold", size=16)
plt.ylabel("$a_y$/(cm/T^2)", weight="bold", size=16)
plt.grid(True)

linear_model = np.polyfit(np.arange(1, len(ays) + 1), ays, 1)
print(f"ay-t: ay = {linear_model[0]} * t + {linear_model[1]}")
linear_model_fn = np.poly1d(linear_model)
equation_ay = f"$a_y$ = {linear_model[0]:.3f}t + {linear_model[1]:.3f}"
plt.xlabel(f"t/T\n{equation_ay}", weight="bold", size=16)
t_s = np.arange(0, length)
plt.plot(t_s, linear_model_fn(t_s), color="orange", linestyle="--")
plt.ylim(0, length)

a_ = sum(ays) / len(ays)
g_ = a_ * 24 * 24 / 100
g = 9.793
E = abs(g_ - g) / g
print(f"average of ay: {a_} cm/T^2\ng = {g_} m/s^2\nE = {E*100}%")

plt.tight_layout()
plt.savefig("6_projectileMotion.png")

"""
[4.0, 10.8, 17.5, 24.5, 31.5, 38.5, 45.5, 52.5, 59.2, 66.3, 73.1]
[5.3, 3.0, 2.4, 3.5, 6.5, 11.0, 17.0, 25.1, 34.6, 45.7, 58.7]
[6.8, 6.7, 7.0, 7.0, 7.0, 7.0, 7.0, 6.7, 7.1, 6.8]
[-2.3, -0.6, 1.1, 3.0, 4.5, 6.0, 8.1, 9.5, 11.1, 13.0]
[1.7, 1.7, 1.9, 1.5, 1.5, 2.1, 1.4, 1.6, 1.9]
x-t: x = 6.9327272727272735 * t + 3.8272727272727387
x-t: y = 0.8416083916083923 * t^2 + -3.0697202797202876 * t + 5.237762237762258
vx-t: vx = 0.007878787878787505 * t + 6.870606060606062
vy-t: vy = 1.6872727272727275 * t + -3.096363636363632
ay-t: ay = 0.0016666666666665874 * t + 1.6916666666666673
average of ay: 1.7000000000000002 cm/T^2
g = 9.792 m/s^2
E = 0.010211375472270457%
"""

## 计算不确定度
# d_y 表示仪器误差
d_y = 0.1  # cm/(T^2)
from math import sqrt

U_b = d_y / sqrt(3)

U_a = sqrt(sum([(a - a_) ** 2 for a in ays]) / (len(ays) - 1)) / sqrt(3)

U = sqrt(U_a**2 + U_b**2)
print(f"U_a = {U_a}, U_b = {U_b}, U = {U}")

d_E = U * 24 * 24 / 100
print(f"d_E = {d_E}")
