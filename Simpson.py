import numpy as np
def f(x):
    return np.exp(3 * x) * np.cos(np.pi * x)
# 复化梯形
def compoundTrapezoid(a, b, n):
    temp = 0
    for i in range(1,n):
        # print(i)
        temp += f(a + i * (b - a) / n)
    result = (b - a) * (f(a) + f(b) + 2 * temp)/(2 * n)
    return result

x = 35232483.36180032  # 精确解
cT50 = compoundTrapezoid(0, 2 * np.pi, 50)
print("cT50：", cT50, "error:", np.abs(cT50-x))
cT100 = compoundTrapezoid(0, 2 * np.pi, 100)
print("cT100：", cT100, "error:", np.abs(cT100-x))
cT200 = compoundTrapezoid(0, 2 * np.pi, 200)
print("cT200：", cT200, "error:", np.abs(cT200-x))
cT500 = compoundTrapezoid(0, 2 * np.pi, 500)
print("cT500：", cT500, "error:", np.abs(cT500-x))
cT1000 = compoundTrapezoid(0, 2 * np.pi, 1000)
print("cT1000：", cT1000, "error:", np.abs(cT1000-x))
# 复化Simpson:
def compoundSimpson(a, b, n):
    temp = 0
    temp1 = 0
    for i in range(1,n):
        temp += f(a + i * (b - a) / n)
    for i in range(n):
        temp1 += f((a + i * (b - a) / n + a + (i + 1) * (b - a) / n) / 2)
    result = (b - a) * (f(a) + f(b) + 2 * temp + 4 * temp1)/(6 * n)
    return result

cS50 = compoundSimpson(0, 2 * np.pi, 50)
print("cS50：", cS50, "error:", np.abs(cS50-x) )
cS100 = compoundSimpson(0, 2 * np.pi, 100)
print("cS100：", cS100, "error:", np.abs(cS100-x))
cS200 = compoundSimpson(0, 2 * np.pi, 200)
print("cS200：", cS200, "error:", np.abs(cS200-x))
cS500 = compoundSimpson(0, 2 * np.pi, 500)
print("cS500：", cS500, "error:", np.abs(cS500-x))
cS1000 = compoundSimpson(0, 2 * np.pi, 1000)
print("cS1000：", cS1000, "error:", np.abs(cS1000-x))