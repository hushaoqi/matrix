import numpy as np
# 原函数
def F(x):
    return x**3 + x**2 + x - 3
# 导数
def f(x):
    return 3*x**2 + 2*x + 1
# 牛顿迭代法
def Newton(x):
    return x -F(x) / f(x)
#初值
x = -0.7
e0 = 1.7
for i in range(7):
    print(i)
    x = Newton(x)
    print("x=", x)
    print("e=", np.fabs(x - 1))
    print("e_{i}/e_{i-1}=", np.fabs(x - 1)/ np.power(e0, 2))
    e0 = np.fabs(x - 1)