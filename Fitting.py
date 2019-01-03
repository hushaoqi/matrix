import numpy as np
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
# 初始化数据
x = np.array(range(1994,2004))
y = np.array([67.052, 68.008, 69.803, 72.024, 73.400, 72.063, 74.669, 74.487, 74.065, 76.777])
# 最小二乘法 y=a+bx 直线拟合
m11 = len(x)
m12 = np.sum(x)
m21 = m12
m22 = np.sum(np.power(x, 2))
n1 = np.sum(y)
n2 = x.dot(y)
a = (m22 * n1 - m12 * n2) / (m11 * m22 - m12 * m21)
b = (m11 * n2 - m21 * n1) / (m11 * m22 - m12 * m21)
# 画图
x1 = np.array(np.arange(1994,2004))
y1 = np.zeros(len(x1))
for i in range(len(x1)):
    y1[i]=a + b * x1[i]
plt.plot(x1, y1, "b-", label='直线拟合')
plt.plot(x, y, "ro")
# 计算均方误差
mae = 0
for i in range(len(x1)):
    mae += np.power((y[i] - y1[i]), 2)
mae /= len(x)
print("直线拟合均方误差为：", mae)
print("直线拟合最小二乘法预测2010产量为：", a + b * 2010)

# 二次曲线拟合 lny = a + 2 lnx
t2 = np.log(x)
z2 = np.log(y)
m11 = len(t2)
m12 = np.sum(t2)
m21 = m12
m22 = np.sum(np.power(t2, 2))
n1 = np.sum(z2)
n2 = t2.dot(z2)
b = 2
a = (n1 - b * m12) / m11
c = np.exp(a)
# 画图
x2 = np.array(np.arange(1994,2003.1, 0.1))
y2 = np.zeros(len(x2))
for i in range(len(x2)):
    y2[i]=c * pow(x2[i], 2)
plt.plot(x2, y2, "g-", label='二次曲线拟合')
# 计算均方误差
mae = 0
for i in range(10):
    mae += np.power((y[i] - y2[10*i]), 2)
mae /= 10
print("抛物线拟合均方误差为：", mae)
print("抛物线拟合最小二乘法预测2010产量为：", c * pow(2010, 2))

# 三次曲线拟合 lny = a + 3 lnx
t3 = np.log(x)
z3 = np.log(y)
m11 = len(t3)
m12 = np.sum(t3)
m21 = m12
m22 = np.sum(np.power(t3, 2))
n1 = np.sum(z3)
n2 = t2.dot(z3)
b = 3
a = (n1 - b * m12) / m11
c = np.exp(a)
# 画图
x3 = np.array(np.arange(1994,2003.1, 0.1))
y3 = np.zeros(len(x3))
for i in range(len(x3)):
    y3[i]=c * pow(x3[i], 3)
plt.plot(x3, y3, "r-", label='三次曲线拟合')
# 计算均方误差
mae = 0
for i in range(10):
    mae += np.power((y[i] - y3[10*i]), 2)
mae /= 10
print("三次曲线拟合均方误差为：", mae)
print("三次曲线拟合最小二乘法预测2010产量为：", c * pow(2010, 3))
plt.legend(loc='upper left')
plt.xticks(x)
plt.show()