# 测量数据（用字符串是因为 ' ' 比 ',' 打起来方便，觉得丑陋的直接用列表就好）
# 标尺读数 s_ 表示 s' 单位为 mm
s = "21.4 26.8 33.0 38.9 44.5 50.8 57.0 63.0"
s_ = "22.8 28.0 34.5 40.1 46.0 51.8 57.5 63.1"
# 金属丝长L/直径d
L = "987.0 987.1 988.0 987.6 987.9"
d = "0.605 0.608 0.602 0.618 0.605"
# 光杠杆长短臂
D = "138.30 138.50 138.40 138.35 138.46"
b = "75.46 76.00 76.28 75.96 75.88"


# 转化为列表
s = [float(i) for i in s.split()]
s_ = [float(i) for i in s_.split()]
L = [float(i) for i in L.split()]
d = [float(i) for i in d.split()]
D = [float(i) for i in D.split()]
b = [float(i) for i in b.split()]


# 处理 s, d_s 表示 \delta_s
def get_d_s_avg(s, s_):
    s_avg = [(i + j) / 2 for i, j in zip(s, s_)]
    print("s_avg: ", s_avg)
    d_s = [(s_avg[i + 4] - s_avg[i]) / 4 for i in range(4)]
    print("d_s: ", d_s)
    d_s_avg = sum(d_s) / len(d_s)
    print("d_s_avg: ", d_s_avg)
    return d_s_avg


d_s_avg = get_d_s_avg(s, s_)


# 处理L d D b; d_ 表示 \delta
def deal_getAvg(name: str, li: list):
    print(">>>>> ", name, " <<<<<")
    avg = sum(li) / len(li)
    print("avg: ", avg)
    d_ = [abs(i - avg) for i in li]
    print("d_: ", d_, "\nd_avg: ", sum(d_) / len(d_))
    return avg


L_avg = deal_getAvg("L", L)
d_avg = deal_getAvg("d", d)
D_avg = deal_getAvg("D", D)
b_avg = deal_getAvg("b", b)

g = 9.793
F = 1 * g

###################### 作图法 #####################
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from math import pi, sqrt

# 创建 m 和 d_s 的数组
m_values = np.array([2, 3, 4, 5, 6, 7, 8, 9])  # 单位: kg
F_values = m_values * g  # 单位: N
# d_s_values = (
#     (8 * D_avg * L_avg * m_values * g) / (np.pi * (d_avg**2) * b_avg * E_avg) / (10**5)
# )  # 单位: mm
d_s_values = np.array(s) - s[0]

# 计算斜率和截距
slope, intercept, r_value, p_value, std_err = stats.linregress(F_values, d_s_values)

# 创建图表
plt.figure(figsize=(10, 6))
plt.scatter(F_values, d_s_values, color="blue", label="Data points")
plt.plot(F_values, slope * F_values + intercept, color="red", label="Fitted line")

plt.xlabel("F (N)")
plt.ylabel("△s (mm)")
plt.title("△s - F")
plt.legend(loc="upper left")  # 将图例放在左上角

# 添加斜率信息文本框
plt.text(
    0.05,
    0.05,
    f"slope: {slope:.6f} mm/N",
    transform=plt.gca().transAxes,
    verticalalignment="bottom",
    bbox=dict(boxstyle="round", facecolor="white", alpha=0.8),
)

plt.grid(True)

# 保存图片 因为在我这里这是第三个实验
plt.savefig("3_output.png", dpi=300, bbox_inches="tight")
print(f"\n直线的斜率 slope 是: {slope:.6f} mm/N")

E = [
    (8 * Di * Li) / (pi * (di**2) * bi * slope) / (10**4)
    for Di, Li, di, bi in zip(D, L, d, b)
]
print("E: ", E)
print("E_avg1: ", sum(E) / len(E))

###################### 直接计算法 #####################

E_avg = (
    (8 * D_avg * L_avg * F) / (pi * (d_avg**2) * b_avg * d_s_avg) / (10**4)
)  # 单位为 10**11 pa
print("E_avg2: ", E_avg)

# 计算不确定度
# >>>>> U_a <<<<<
# 可能并没有U_a ，直接用 U_b，但是我到现在都不确定，所以还是算一下
U_a = sqrt(sum([(i - E_avg) ** 2 for i in E]) / (len(E) * (len(E) - 1)))

# >>>>> U_b <<<<<
# u_ 表示仪器导致的 B 类误差
u_m = 0.0005
u_D = 0.5
u_L = 0.5
u_b = 0.02
u_d = 0.004
u_s = 0.2
U_b = sqrt(
    (
        ((u_m / 1) ** 2)
        + ((u_D / D_avg) ** 2)
        + ((u_L / L_avg) ** 2)
        + ((u_b / b_avg) ** 2)
        + ((2 * u_d / d_avg) ** 2)
        + ((u_s / d_s_avg) ** 2)
    )
    / 3
)

U = sqrt(U_a**2 + U_b**2)

print("U_a: ", U_a)
print("U_b: ", U_b)
print("U: ", U)
