# p 可能是 “气压”，也可能是 “密度”
t = 22.0  # ℃
pw0 = 2643.38  # Pa ，饱和水蒸气压
n = 0.615  # 相对湿度
pw = pw0 * n  # Pa ，水蒸气压
print("pw:", pw)

V = 159.326  # cm^3 玻璃泡的体积
dms = [0.1893, 0.1892, 0.1891]  # g m1-m0 空气质量
ps = [m / V for m in dms]  # g/cm^3 空气密度
print("ps:", ps)
avg_p = sum(ps) / len(ps) * 1e3  # g/cm^3 => kg/m^3 平均空气密度
print("平均密度：", avg_p, "kg/m^3")
p0 = 101325  # Pa ，标准大气压
p_ = 102510  # Pa ，气压
p = p_ * (1 - 0.000163)  # Pa 修正后的实验气压
print("p: ", p_)
a = 1 / 273.15
T0 = 273.15  # K
p_gan = avg_p * (p0 / p) * (a * t + 1) * ((3 * pw) / (8 * p) + 1)
print("p_gan:", p_gan)  # 标况下干燥气体的密度
Ma = 0.02898  # kg/mol ，空气的摩尔质量
R = (p0 * Ma) / (T0 * p_gan)  # J/(kg·K) 普适气体常数
print("R:", R)

print(p / 133.322 / 10)  # cmHg 附录中查找理论温度
