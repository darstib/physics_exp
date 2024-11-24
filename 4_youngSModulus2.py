# ZJU 动态法测量材料杨氏模量 声速的测定 数据处理脚本
# 处理 f
def get_f(fs):

    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.optimize import curve_fit

    xs = [5 * i for i in range(1, 11) if i != 7]

    # Define the quadratic function for fitting
    def quadratic(x, a, b, c):
        return a * x**2 + b * x + c

    # Perform curve fitting
    popt, _ = curve_fit(quadratic, xs, fs)
    # Generate points for smooth curve
    x_smooth = np.linspace(min(xs), max(xs), 100)
    y_smooth = quadratic(x_smooth, *popt)
    # Find the minimum point
    x_min = -popt[1] / (2 * popt[0])
    y_min = quadratic(x_min, *popt)
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.scatter(xs, fs, color="red", label="Data points")
    plt.plot(x_smooth, y_smooth, color="blue", label="Fitted curve")
    plt.plot(x_min, y_min, "go", label="Minimum point")
    plt.xlabel("x (mm)")
    plt.ylabel("Frequency (Hz)")
    plt.title("Frequency vs Distance")
    plt.legend()
    plt.grid(True)
    # Annotate the minimum point
    plt.annotate(
        f"Min: ({x_min:.2f}, {y_min:.2f})",
        xy=(x_min, y_min),
        xytext=(5, 5),
        textcoords="offset points",
    )
    plt.savefig("4_youngSModulus2.png")
    print(f"Minimum point: x = {x_min:.2f}, f = {y_min:.2f}")
    return y_min


fs = [736.4, 734.8, 733.8, 733.1, 732.5, 731.8, 732.2, 732.3, 732.5]
# f_fix = get_f(fs)
f_fix = 731.86

##### 处理读数 #####
d0 = -0.015  # 螺旋测微器零点读数 单位: mm
ds = [5.950, 5.945, 5.948, 5.955, 5.952]  # 单位: mm
Ls = [160.5, 160.1, 160.2, 160.1, 160.1]  # 单位: mm
ms = [37.338, 37.337, 37.336, 37.337, 37.337]  # 单位: g，可以只测一次，自己设置 m_avg

from math import sqrt


def get_avg(li):
    return sum(li) / len(li)


d_avg = get_avg(ds) - d0
L_avg = get_avg(Ls)
m_avg = get_avg(ms)
print("d_avg:", d_avg, "L_avg:", L_avg, "m_avg:", m_avg)


# dl 为仪器误差
def get_U(li, dl):
    # get U_a
    n = len(li)
    i_avg = get_avg(li)
    U_a = sqrt(sum([(i - i_avg) ** 2 for i in li]) / (n * (n - 1)))
    U_b = dl / sqrt(3)
    U = sqrt(U_a**2 + U_b**2)
    return U_a, U_b, U


# L 不确定度
dL = 0.2
dd = 0.004
dm = 0.001
df = 0.1
L_a, L_b, U_L = get_U(Ls, dL)
print("L_a:", L_a, "L_b:", L_b, "U_L:", U_L)
# d 不确定度
d_a, d_b, U_d = get_U(ds, dd)
print("d_a:", d_a, "d_b:", d_b, "U_d:", U_d)

E = [
    1.6067 * (L**3) * m * (f_fix**2) / (d**4) / (1e11) for L, m, d in zip(Ls, ms, ds)
]  # 单位: 10**11 N/m^2

E_avg = get_avg(E)
print("E_avg: ", E_avg)

E = 1.6067 * (L_avg**3) * m_avg * (f_fix**2) / (d_avg**4) / (1e11)
print("E:", E)
# 计算相对不确定度
dE = E_avg * sqrt(
    (
        (3 * dL / L_avg) ** 2
        + (4 * dd / d_avg) ** 2
        + (dm / m_avg) ** 2
        + (2 * df / f_fix) ** 2
    )
)

print("dE:", dE)
