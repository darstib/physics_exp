# 测量数据
## 第一组 方波形
s1_1 = "0.04 0.05 0.07 0.10 0.15 0.20"
S1_1 = [float(i) for i in s1_1.split()]
s2_1 = "0.44 0.45 0.37 0.50 0.45 0.40"
S2_1 = [float(i) for i in s2_1.split()]
dt_1 = "58.5 58.0 44.5 58.5 45.0 29.5"
dt_1s = [float(i) for i in dt_1.split()]
## 第二组 正弦波形
s1_1 = "0.01 0.03 0.05 0.07 0.09 0.11"
S1_2 = [float(i) for i in s1_1.split()]
s2_1 = "0.51 0.43 0.45 0.47 0.49 0.51"
S2_2 = [float(i) for i in s2_1.split()]
dt_2 = "73.0 59.5 57.5 59.0 59.5 58.0"
dt_2s = [float(i) for i in dt_2.split()]

# 频率
v = 1 * 10**8
v_ = 4.55 * 10**5


# 计算光速
def get_cs(S1, S2, dt_s):
    def get_c(ds, dt_):
        return (2 * ds * v) / (dt_ * v_)

    cs = []
    for s1, s2, dt_ in zip(S1, S2, dt_s):
        cs.append(get_c(s2 - s1, dt_))
    return cs


cs1 = get_cs(S1_1, S2_1, dt_1s)
cs2 = get_cs(S1_2, S2_2, dt_2s)
print("第一组：", cs1)
print("第二组：", cs2)


# 平均光速
def get_avg(cs):
    return sum(cs) / len(cs)


c1_avg = get_avg(cs1)
c2_avg = get_avg(cs2)
print("平均光速", c1_avg, c2_avg)


# 测量相对误差
def get_err(c_avg):
    c = 3  # * 10**8
    return abs(c - c_avg) / c


err1 = get_err(c1_avg)
err2 = get_err(c2_avg)
print("相对误差：", err1, err2)


# 计算不确定度 ua
def get_ua(cs):
    from math import sqrt

    c_avg = get_avg(cs)
    n = len(cs)
    return sqrt(sum([(c - c_avg) ** 2 for c in cs]) / ((n - 1) * n))


ua1 = get_ua(cs1)
ua2 = get_ua(cs2)
print("测得 U_a ：", ua1, ua2)
