import matplotlib.pyplot as plt
import numpy as np

# 初始化数据
x = np.array(range(1994,2004))
y = np.array([67.052, 68.008, 69.803, 72.024, 73.400, 72.063, 74.669, 74.487, 74.065, 76.777])
z1 = np.polyfit(x, y, 3)#用3次多项式拟合
p1 = np.poly1d(z1)
print(p1) #在屏幕上打印拟合多项式
yvals=p1(x)#也可以使用yvals=np.polyval(z1,x)
plot1=plt.plot(x, y, '*')
plot2=plt.plot(x, yvals, 'r')

plt.title('Cubic curve fitting')
plt.ylabel('Annual oil production')
plt.xlabel('year')
# 计算均方误差
mae = 0
for i in range(len(x)):
    mae += np.power((y[i] - yvals[i]), 2)
mae /= len(x)
print("三次拟合均方误差为：", mae)
out =2010
print("三次拟合曲线预测2010产量为：",0.01821*out*out*out - 109.3*out*out + 2.185e+05*out - 1.457e+08)
plt.show()
#plt.savefig('p1.png')