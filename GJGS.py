import numpy as np
N = 4  # N = 8
hilbert = np.matrix(np.zeros((N, N)))
for i in range(len(hilbert)):
    for j in range(len(hilbert)):
        hilbert[i,j] = 1 / (i+j+1)
b = np.ones(N)
x = np.zeros(N)
"""高斯消元法"""
# 建立增广矩阵
augmentedMatrix = np.matrix(np.ones((N, N+1)))
for i in range(N):
    for j in range(N):
        augmentedMatrix[i, j] = hilbert[i, j]
# 执行高斯消元
for i in range(N-1):
    if (augmentedMatrix[i, i] != 0):
        augmentedMatrix[i+1:, :] = augmentedMatrix[i+1:, :] - (augmentedMatrix[i+1:, i] / augmentedMatrix[i, i]) * augmentedMatrix[i, :]
# 求解 x
for i in range(N-1, -1, -1):
    m = augmentedMatrix[i, N]
    for j in range(N-1, 0, -1):
        m -= x[j] * augmentedMatrix[i, j]
    x[i] = m /augmentedMatrix[i, i]
    # x[i] = (augmentedMatrix[i, 4] - x[3] * augmentedMatrix[i, 3] - x[2] * augmentedMatrix[i, 2] - x[1] * augmentedMatrix[i, 1]) / augmentedMatrix[i, i]
print(x)
"""Jacobi迭代法"""
x0 = np.zeros(N)
x = np.zeros(N)
# for iter0 in range(1000000):
while(True):
    for i in range(N):
        temp = 0
        for j in range(N):
            if i != j:
                temp += hilbert[i, j] * x[j]
        x[i] = (b[i]-temp) / hilbert[i, i]
    difference = max(abs(x - x0))
    if difference < 1e-4:
        break
    else:
        x0 = x.copy()
print(x)
"""GS法"""
x = np.zeros(N)
temp = np.zeros(N)
times = 0
while(True):
    for i in range(N):
        temp1 = 0
        for j in range(i):
            temp1 += hilbert[i, j] * x[j]
        for j in range(i+1, N):
            temp1 += hilbert[i, j] * x[j]
        x[i] = (b[i] - temp1) / hilbert[i, i]
    difference = max(abs(x - temp))
    if difference < 1e-4:
        break
    else:
        temp[:N] = x[:N]
print(x)
"""共轭梯度法"""
x = np.matrix(np.zeros(N)).T
b = np.matrix(np.ones(N)).T
r = b - hilbert * x
p = r
for i in range(N):
    alpha = r.T.dot(r)[0,0] / hilbert.dot(p).T.dot(p)[0,0]
    x = x + alpha * p
    r0 = r
    r = r - alpha * hilbert.dot(p)
    beta = r.T.dot(r)[0,0] / r0.T.dot(r0)[0,0]
    p = r + beta * p
print(x.T)