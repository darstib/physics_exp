class Data:
    li = []
    length = 0
    avg = 0
    ua = 0
    standard = 0

    def __init__(self, li, standard):
        self.li = li
        self.length = len(li)
        self.avg = sum(li) / self.length
        self.ua = self.getUa()
        self.standard = standard
        self.E = abs(self.avg - self.standard) / self.avg

    def getUa(self):
        from math import sqrt

        return sqrt(
            sum([(i - self.avg) ** 2 for i in self.li])
            / ((self.length - 1) * self.length)
        )


print("\n" + ">" * 10 + "   part 3   " + "<" * 10)
fxs1 = [198.6, 199.2, 199.3, 199.1, 199.1]
fx1_data = Data(fxs1, 200)
print("fx1_data.avg = ", fx1_data.avg)
print("fx1_data.ua = ", fx1_data.ua)
print("fx1_data.E = ", fx1_data.E)

print("\n" + ">" * 10 + "   part 4   " + "<" * 10)
fys2 = [49.970, 49.997, 50.012, 50.028, 50.014]
fy2_data = Data(fys2, 50)
print("fy2_data.avg = ", fy2_data.avg)
print("fy2_data.ua = ", fy2_data.ua)
print("fy2_data.E = ", fy2_data.E)

print("\n" + ">" * 10 + "   part 5   " + "<" * 10)
U_2p = 1.92
U_1p_p = 5.12
U = U_1p_p / 2 - U_2p
print("U = ", U)

print("\n" + ">" * 10 + "   part 6   " + "<" * 10)

f = 1.98  # kHz
T = 1 / f  # ms
d_f = 9.61  # kHz
d_t = 1 / d_f  # ms
d_Phi = d_t / T * 360  # degree
print("T = ", T)
print("d_t =", d_t)
print("d_Phi = ", d_Phi)
