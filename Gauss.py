import numpy as np
from scipy import linalg
def f1(x):
    return x**2 / np.sqrt(1 - x**2)

def f2(x):
    return np.sin(x) / x

# 第一题
# 2点Gauss积分  解的x0=-1/sqrt(3), x1=1/sqrt(3)
x = np.array([-1/np.sqrt(3), 1/np.sqrt(3)])
A = np.array([[1, 1], [x[0], x[1]]])
b = np.array([2, 0])
a = linalg.solve(A, b)
I = a[0]*f1(x[0]) + a[1]*f1(x[1])
print("2点Gauss积分:",I)
# 3点Gauss积分  解的x0=-sqrt(3/5), x1=0, x2=sqrt(3/5)
x = np.array([-np.sqrt(3/5), 0, np.sqrt(3/5)])
A = np.array([[1, 1, 1],[x[0], x[1], x[2]], [x[0]**2, x[1]**2, x[2]**2]])
b = np.array([2, 0, 2/3])
a = linalg.solve(A, b)
I = a[0]*f1(x[0]) + a[1]*f1(x[1]) + a[2]*f1(x[2])
print("3点Gauss积分:",I)
# 5点Gauss积分  解的x0=-0.9061798459386646, x1=-0.5384693101056842, x2=0
# x3=0.5384693101056842, x4=0.9061798459386646
x = np.array([-0.9061798459386646, -0.5384693101056842, 0, 0.5384693101056842, 0.9061798459386646])
A = np.array([[1, 1, 1, 1, 1],[x[0], x[1], x[2], x[3], x[4]], [x[0]**2, x[1]**2, x[2]**2, x[3]**2, x[4]**2], [x[0]**3, x[1]**3, x[2]**3, x[3]**3, x[4]**3], [x[0]**4, x[1]**4, x[2]**4, x[3]**4, x[4]**4]])
b = np.array([2, 0, 2/3, 0, 2/5])
a = linalg.solve(A, b)
I = a[0]*f1(x[0]) + a[1]*f1(x[1]) + a[2]*f1(x[2]) + a[3]*f1(x[3]) + a[4]*f1(x[4])
print("5点Gauss积分:",I)

# 第二题
# 2点Gauss积分  替换公式为 x=t*pi/4+pi/4  解的t0=-1/sqrt(3), t1=1/sqrt(3)
t = np.array([-1/np.sqrt(3), 1/np.sqrt(3)])
A = np.array([[1, 1], [t[0], t[1]]])
b = np.array([2, 0])
a = linalg.solve(A, b)
I = np.pi/4 * (a[0]*f2(t[0]*np.pi/4+np.pi/4) + a[1]*f2(t[1]*np.pi/4+np.pi/4))
print("2点Gauss积分:",I)
# 3点Gauss积分  解的t0=-sqrt(3/5), t1=0, t2=sqrt(3/5)
t = np.array([-np.sqrt(3/5), 0, np.sqrt(3/5)])
A = np.array([[1, 1, 1],[t[0], t[1], t[2]], [t[0]**2, t[1]**2, t[2]**2]])
b = np.array([2, 0, 2/3])
a = linalg.solve(A, b)
I = np.pi/4 * (a[0]*f2(t[0]*np.pi/4+np.pi/4) + a[1]*f2(t[1]*np.pi/4+np.pi/4) + a[2]*f2(t[2]*np.pi/4+np.pi/4))
print("3点Gauss积分:",I)
# 5点Gauss积分  解的t0=-0.9061798459386646, t1=-0.5384693101056842, t2=0
# t3=0.5384693101056842, t4=0.9061798459386646
t = np.array([-0.9061798459386646, -0.5384693101056842, 0, 0.5384693101056842, 0.9061798459386646])
A = np.array([[1, 1, 1, 1, 1],[t[0], t[1], t[2], t[3], t[4]], [t[0]**2, t[1]**2, t[2]**2, t[3]**2, t[4]**2], [t[0]**3, t[1]**3, t[2]**3, t[3]**3, t[4]**3], [t[0]**4, t[1]**4, t[2]**4, t[3]**4, t[4]**4]])
b = np.array([2, 0, 2/3, 0, 2/5])
a = linalg.solve(A, b)
I = np.pi/4 * (a[0]*f2(t[0]*np.pi/4+np.pi/4) + a[1]*f2(t[1]*np.pi/4+np.pi/4) + a[2]*f2(t[2]*np.pi/4+np.pi/4) + a[3]*f2(t[3]*np.pi/4+np.pi/4) + a[4]*f2(t[4]*np.pi/4+np.pi/4))
print("5点Gauss积分:",I)