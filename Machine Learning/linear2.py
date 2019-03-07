import numpy as np
import dataset
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter1d

n= 14
#Xi = np.arange(n+2).reshape(1, n+2)
#Q = np.arange(n+2).reshape(1, n+2)
#Xi = np.ones(n+2, dtype=float)
#Xi[n+1] = 1
#Y = np.arange(500).reshape(1, 500)

Q = np.ones(n+2, dtype=float)
A = np.ones(n+2, dtype=float)

a = []
b = []

def h(Q,Xi): # COMPLETE
    Xi_T = np.transpose(Xi)
    F = np.dot(Q, Xi_T)
    return F

def J(K,Q,X,Y):
    V = 0
    for i in range(K):
        V = (h(Q,X[i])-Y[i])**2 + V
    F = (1/(2*K))*V
    print(F)
    return F

def derivative_J(K,Q,X,Y,j):
    V = 0
    Z = 0
    for i in range(K):
        V = (h(Q,X[i]) - Y[i])*X[i][j] + V
    Z = (1/K) * V + Z
    return Z

def linearization(n,Xi,Y,K,train_rate=500,alfa=0.01):
    for j in range(train_rate):

        Q = np.copy(A)
        a.append(J(K, Q, Xi, Y))
        b.append(j)
        for i in range(n+1):
            A[i] = A[i] - alfa*derivative_J(K,Q,Xi,Y,i)

def plotting(a,b):
    ysmoothed = gaussian_filter1d(a[1:], sigma=2)

    plt.plot(b[1:], ysmoothed, '-', color='red')
    axes = plt.gca()
    axes.set_ylim([0, 20])

    plt.autoscale(enable=True, axis='x')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


n = 15
k = 500

x,y = dataset.dataset_n()
#print(x)
linearization(n,x,y,k)
print(a)
print(len(b))

plotting(a,b)