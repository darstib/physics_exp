from math import sqrt

R1 = 1000  # Ω
R2 = 1000  # Ω

### part 1 ###

Rs1 = 227.2  # Ω
Rs2 = 236.5  # Ω

Rs = sqrt(Rs1 * Rs2)
print(f"Rs = {Rs} Ω")

dRs = 0.1  # Ω
dd = 10.0  # 格子

s = dd / (dRs / Rs)

print(f"s = {s} 格")


def E(Rs, s):
    m = 6
    return sqrt((0.001 + 0.002 * m / Rs) ** 2 + (0.2 / s) ** 2)


E = E(Rs, s)
print(f"E = {E*100} %")

dRx = Rs * E
print(f"dRx = {dRx} Ω")

### part 2 ###

Rns = [683.9, 679.5, 679.3, 679.7, 678.7, 675.4, 682.4, 683.5]

assert len(Rns) == 8

Rn = sum(Rns) / len(Rns)

print(f"Rn = {Rn} Ω")

S = sqrt(
    sum([(Rn - Rns[i]) ** 2 for i in range(len(Rns))]) / (len(Rns) - 1)
)  # 注意这个公式与老师要求一致

print(f"标准偏差 S = {S} Ω")

print(f"离散度 = {S / Rn * 100} %")
