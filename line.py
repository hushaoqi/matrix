from pylab import *
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
# 画出直线拟合图像
x1 = np.array(np.arange(1994,2004))
y1 = np.zeros(len(x1))
for i in range(len(x1)):
    y1[i]=a + b * x1[i]
plt.title('Straight line fitting')
plt.ylabel('Annual oil production')
plt.xlabel('year')
plt.plot(x1, y1, "r-")
plt.plot(x, y, "bo")
# 计算均方误差
mae = 0
for i in range(len(x1)):
    mae += np.power((y[i] - y1[i]), 2)
mae /= len(x)
print("直线拟合均方误差为：", mae)
print("直线拟合最小二乘法预测2010产量为：", a + b * 2010)
plt.show()