import numpy as np
import matplotlib.pyplot as plt
h = 0.001  # h=0.1, 0.01  注意改动t
t = np.array(np.arange(0, 1.001, 0.001))
# Euler法
u = np.zeros(len(t))
u[0] = 1
for i in range(1, len(u)):
    u[i] = u[i-1] + h*(u[i-1]*np.cos(t[i-1]))
print('Euler法：',u[-1])
plt.plot(t[-1], u[-1], 'ro')
plt.plot(t, u, 'r', label='Euler')
# 改进Euler法
u1 = np.zeros(len(t))
u1[0] = 1
for i in range(1, len(u1)):
    u1[i] = u1[i-1] + h*(u1[i-1]*np.cos(t[i-1]))
    u1[i] = u1[i - 1] + h/2 * (u1[i - 1] * np.cos(t[i - 1]) + u1[i] * np.cos(t[i]))
print('改进Euler法：',u1[-1])
plt.plot(t[-1], u1[-1], 'bo')
plt.plot(t, u1, 'b', label="Improved Euler")
# Runge-Kutta法
u2 = np.zeros(len(t))
u2[0] = 1
k = np.zeros(4)
for i in range(1, len(u2)):
    k[0] = u2[i-1]*np.cos(t[i-1])
    k[1] = (u2[i - 1] + h * k[0] / 2) * np.cos(t[i - 1] + h / 2)
    k[2] = (u2[i - 1] + h * k[1] / 2) * np.cos(t[i - 1] + h / 2)
    k[3] = (u2[i - 1] + h * k[2]) * np.cos(t[i - 1] + h)
    u2[i] = u[i-1] + h * (k[0] + 2 * k[1] + 2 * k[2] + k[3]) / 6
print("Runge-Kutta法：", u2[-1])
plt.plot(t[-1], u2[-1], 'go')
plt.plot(t, u2, 'g', label="Runge-Kutta")
# 设置图标签
plt.xlabel('t')
plt.ylabel('y')
plt.title('h=0.001')
plt.legend(loc='upper left')
plt.show()