import numpy as np
import random
import sklearn
from sklearn import datasets

dataset = sklearn.datasets.fetch_california_housing()
#X = np.insert(dataset.data,0,1,axis=1)
#Y = dataset.target
m,n = dataset.data.shape
print(m/3)
Y=dataset.target
X = (dataset.data - np.resize(np.average(dataset.data,axis=0),(m,n)))/np.resize(np.std(dataset.data,axis=0),(m,n))
X = np.insert(X,0,1,axis=1)
print(X)
X1_Test, X2_Test = X[:int(3*m/4)], X[int(3*m/4):]
Y1_Test, Y2_Test = Y[:int(3*m/4)], Y[int(3*m/4):]

print(Y2_Test.shape)
m,n = X.shape
theta = np.ones(n, dtype=float)

def J(X,Y,theta):
    return (np.transpose(X@theta-Y)@(X@theta-Y))/(2*m)

theta = np.ones(n, dtype=float)
iteration= 30000
alpha=0.01


for i in range(2):
    (M,N)= X1_Test.shape

    #print(xs)
    #print(ys)
    #xs, ys = zip(*random.sample(list(zip(X, Y)), 1000))

    for i in range(iteration):
        theta = (theta-(alpha/M)*np.transpose(X1_Test)@(X1_Test@theta-Y1_Test))
        print(J(X1_Test,Y1_Test,theta))
print(theta)
def test(data,theta,n):
    total=0
    for i in range(n):
        total= data[i]*theta[i] + total

    return total
for i in range(5160):
    (M, N) = X2_Test.shape
    #print(X2_Test)
    print(Y2_Test[i],"=",test(X2_Test[i],theta,N))