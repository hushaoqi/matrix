import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
import sympy
x = np.array((0, 1, 2, 3, 4))
y = np.array((1, 3, 3, 4, 2))
h = np.zeros(len(x))
for i in range(len(h)-1):
    h[i] = x[i+1] - x[i]
lam = np.zeros(len(x))
for i in range(1, len(lam)-1):
    lam[i] = h[i] / (h[i] + h[i-1])
miu = np.zeros(len(x))
for i in range(1, len(miu)-1):
    miu[i] = h[i-1] / (h[i] + h[i-1])
g = np.zeros(len(x))
for i in range(1, len(g)-1):
    g[i] = 3 * ( miu[i] * (y[i + 1] - y[i]) / h[i] + lam[i] * (y[i] - y[i - 1]) / h[i - 1] )
g[0] = 3*(y[1]-y[0])/h[0]
g[4] = 3*(y[4]-y[3])/h[3]
a = np.zeros([5,5])
for i in range(len(a)):
    a[i,i] = 2
    a[0,1], a[len(a)-1, len(a)-2] = 1, 1
    if i > 0 and i < len(a)-1:
        a[i,i-1] = lam[i]
        a[i,i+1] = miu[i]
m = linalg.solve(a, g)
def s(xx, x, y, h):
    result = -1
    for i in range(len(x)-1):
        if xx>=x[i] and xx<=x[i+1]:
            result = y[i] * (1 - 2 * (xx - x[i]) / (-h[i])) * ((xx - x[i+1]) / (-h[i])) ** 2 + y[i+1] * (1 - 2 * (xx - x[i+1]) / h[i]) * ((xx - x[i]) / h[i]) ** 2 + m[i] * (xx - x[i]) * ((xx - x[i+1]) / (-h[i])) ** 2 + m[i+1] * (xx - x[i+1]) * ((xx - x[i]) / h[i]) ** 2
    return result
xx = np.array(np.arange(0,4.1,0.1))
yy = np.zeros(len(xx))
for i in range(len(yy)):
    yy[i] = s(xx[i], x, y, h)
# 画图
plt.plot(x,y,'bo')
plt.plot(xx, yy, 'red',linestyle = '--')
plt.show()
# 输出各m的值
print("m:", m)
x0 = x
y0 = y
x = sympy.Symbol('x')
for i in range(len(x0)-1):
    s = (h[i] + 2 * (x - x0[i])) * (x - x0[i+1]) ** 2 * y[i] / (h[i] ** 3) + (h[i] - 2 * (x - x0[i+1])) * (x - x0[i]) ** 2 * y[i+1] / (h[i] ** 3) + (x - x0[i]) * (x - x0[i+1]) ** 2 * m[i] / (h[i] ** 2) + (x - x0[i+1]) * (x - x0[i]) ** 2 * m[i+1] / (h[i] ** 2)
    print("s[",i,"]:", sympy.simplify(s))