import numpy as np
import matplotlib.pyplot as plt
# 拉格朗日多项式插值函数
def Lagrange(x, y, a):
    result = 0.0
    for i in range(len(y)):
        t = y[i]
        for j in range(len(y)):
            if i != j:
                t *= (a - x[j]) / [x[i] - x[j]]
        result += t
    return result

# 输入表格数据
x = np.array(range(1994,2004))
y = np.array([67.052, 68.008, 69.803, 72.024, 73.400, 72.063, 74.669, 74.487, 74.065, 76.777])
# 画出源数据图像
plt.title('9th order polynomial curve')
plt.ylabel('Annual oil production')
plt.xlabel('year')

plt.xticks(x)
plt.plot(x, y, "b-o")
# 使用插值多项式描述这些数据图像
x1 = np.array(np.arange(1994,2003.1,0.1))
y1 = np.zeros(len(x1))
for i in range(len(x1)):
    y1[i]=Lagrange(x, y, x1[i])
plt.plot(x1, y1, "r-")
plt.show()
# 通过该模型预测2010年的产量
y0 = Lagrange(x,y,2010)
print("2010年产量为：", y0[0])