Liimport dataset
import matplotlib.pyplot as plt
import numpy as np

def derivQ0(Q,x,y):
    V=0.0
    M= len(x)
    for i in range(M):
        V = x[i]*((h(x[i],Q) - y[i])) + V
    F = (1/M)*V
    return F

def derivQ1(Q,x,y):
    V = 0.0
    M= len(x)
    for i in range(M):
        V = ((h(x[i], Q) - y[i])) + V
    F = (1 / M) * V
    return F

def h(x,Q):
    F = Q[0]*x + Q[1]
    return F

def J(Q,x,y):

    V = 0.0
    M= len(x)
    for i in range(M):
        V = (h(x[i],Q) - y[i])**2 + V
    F = (1/(2*M))*V
    return F


def plotting(Q,x,y):
    plt.subplot(321)
    plt.scatter(x, y, s=2, marker=">")
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = Q[1] + Q[0] * x_vals
    plt.plot(x_vals, y_vals, '-', color='blue')

def plotting2(Q,x,y):
    plt.subplot(321)
    plt.scatter(x, y, s=2, marker=">")
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = Q[1] + Q[0] * x_vals
    plt.plot(x_vals, y_vals, '-', color='red')
    plt.show()


def linear_reg(X,Y,alfa=0.001, train_rate=10000):
    Q = [1.0,1.0]
    for i in range(train_rate):
        Q[0] = Q[0] - alfa * derivQ0(Q,X,Y)
        Q[1] = Q[1] - alfa * derivQ1(Q,X,Y)
        Q = [Q[0],Q[1]]
        if i%1000 == 1:
            plotting(Q, X, Y)
    plotting2(Q,X,Y)

X, Y= dataset.dataset()
print(X)
linear_reg(X,Y)
