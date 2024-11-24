# 注意是 60' 进位为 1°，所以 60° = 59°60'
As = [59.59, 59.56, 59.58, 59.60, 59.57, 59.58]
A_avg = sum(As) / len(As)
print("A_avg = ", A_avg)

from math import sqrt

U_a = sqrt(sum([(a - A_avg) ** 2 for a in As]) / (len(As) * (len(As) - 1)))
U_b = 1 / sqrt(3)
U = sqrt(U_a**2 + U_b**2)
print("U_a = ", U_a)
print("U_b = ", U_b)
print("U = ", U)  # 注意最低精度为 1' ，所以保留整数
