# 驻波法/相位差法 读数
read1 = [11.335, 15.540, 19.805, 24.110, 28.550, 33.002, 37.625, 42.065]
read2 = [38.805, 43.065, 47.390, 51.625, 56.000, 60.305, 64.655, 69.085]
# r1 = "5.017 9.764 14.102 18.618 22.941 27.998 31.829 36.491 41.003 45.981 51.258 55.994"
# read1 = [float(i) for i in r1.split()]
# r2 = "2.486 6.914 10.547 14.997 19.461 23.696 28.013 32.488 37.106 41.477 46.135 50.781"
# read2 = [float(i) for i in r2.split()]

# 频率
f = 40.1
# f = 39.4
# 温度
t = 25.2
# t = 24.9
# 不确定度 ub
ub = 0.030


# 获得半波长
def get_lambda_2(read):
    l = len(read)
    m = l // 2
    # print(m)
    sum1 = sum(read[:m])
    sum2 = sum(read[m:])
    # print(sum1, sum2)
    return (sum2 - sum1) / (m**2)


# 获得测量声速
def get_v(read, f):
    lambda_2 = get_lambda_2(read)
    # print(lambda_2)
    return 2 * lambda_2 * f


v1 = get_v(read1, f)
v2 = get_v(read2, f)

print("测得声速：", v1, v2)

from math import sqrt


# 获得温度为t时的声速
def get_v(t):
    return 331.45 * sqrt(t / 273.15 + 1)


vt = get_v(t)


# 测量相对误差
def get_err(v, vt):
    return abs(v - vt) / vt


print("实际声速：", vt)
err1 = get_err(v1, vt)
err2 = get_err(v2, vt)

print("相对误差：", err1, err2)


# 计算平均值
def get_overline(read):
    return sum(read) / len(read)


# 计算不确定度 ua
def get_ua(read):
    read_overline = get_overline(read)
    n = len(read)
    return sqrt(sum([(x - read_overline) ** 2 for x in read]) / ((n - 1) * n))


# print("测得 U_a ：", get_ua(read1, read1_overline), get_ua(read2, read2_overline))


# 获得多次测量的 lambda
def get_lams(read):
    l = len(read)
    m = l // 2
    lams = []
    for i in range(m):
        lams.append((read[i + m] - read[i]) * 2)
    return lams


ua1 = get_ua(get_lams(read1))
ua2 = get_ua(get_lams(read2))

print("测得 U_a ：", ua1, ua2)


def get_u(ua, ub):
    return sqrt(ua**2 + ub**2)


u1 = get_u(ua1, ub)
u2 = get_u(ua2, ub)

print("不确定度：", u1, u2)
