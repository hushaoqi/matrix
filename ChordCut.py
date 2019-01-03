import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return x**3 + 2 * x**2 + 10 * x - 100
x = np.array(np.arange(0, 10, 0.1))
y = np.zeros(len(x))
for i in range(len(y)):
    y[i] = f(x[i])
plt.plot(x, y)
plt.show()
x0 = 3
x1 = 3.1
times = 0
while(True):
    x = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    x0 = x1
    times += 1
    print(times, x)
    if abs(x - x1) < 1e-5 :
        break
    else:
        x1 = x
print(times)
print(x)
print(f(x))