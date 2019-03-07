import numpy as np
import math
from sklearn.datasets import load_breast_cancer

from sklearn.preprocessing import normalize

m = 569
n = 30

data = load_breast_cancer()
target = data["target"]
data = data["data"]
data = normalize(data)
# print(np.shape(data))
data = np.c_[np.ones(m), data]
input(data)
train_n = int((data.data.shape[0]) * 0.8)
val = data[train_n:m]
tar = target[train_n:m]

data = data[:train_n]
print(data)
print(data.shape)
input()
target = target[:train_n]
# print(data)
# print(np.shape(data))
# print(target)
# print(len(target))

theta = np.zeros(n + 1, dtype=float)


def g(x):
    return (1.0 / (1.0 + np.exp(-x)))


def hyp(x):
    z = g(np.dot(theta, np.transpose(x)))
    return z


# def g(x):
#    return ( 1 / ( 1 - np.exp(x) ) )
#
# def h(x, t):
#    return g(np.dot(t,x))
#
# def hyp(X_train,theta):
#    #print(theta.shape,X_train.shape)
#    #theta = np.reshape()
#    return g(theta.dot(np.matrix.transpose(X_train)))

def cost(x=data, y=target):
    y_1 = np.dot(np.transpose(y), np.log(hyp(x)))
    one = np.ones(455, dtype=float)
    y_2 = np.dot(((one - y).T), np.log(one - hyp(x)))
    j = (-1.0 / len(x)) * (y_1 + y_2)
    return j

    # s = (train_n, n + 1)
    ##print( "y: ", np.shape(y))
    ##print("  np.matmul(np.transpose(t),np.transpose(x)): ", np.shape(np.matmul(np.transpose(t),np.transpose(x))))
    ##print("one_y: g( np.matmul( np.transpose(t),np.transpose(x)): ",  np.shape(one_y - g( np.matmul( np.transpose(t),np.transpose(x)) )))
    ##print( "one: " , np.shape(one) )
    ##print( "one_y: " , np.shape(one_y) )
    ##print( "np.transpose: y " , np.shape(np.transpose(y)) )
    ##print( "t: " , np.shape(t) )
    ##print(np.shape(np.transpose(np.subtract(one_y, y))))
    ##print( np.transpose(np.log(np.subtract(one,hyp(x,t))) ))
    ##print( np.log(np.subtract(one,hyp(x,t))) )
    # first = np.dot(np.transpose(y), np.log(hyp(x,t)))
    # second = np.dot(np.transpose(np.subtract(one_y, y)), np.transpose(np.log(np.subtract(one,hyp(x,t)))))
    # a = ( -1/m ) * ( first + second )
    # return a
    ##return np.multiply(np.divide(1,m),(np.subtract(np.negative(np.matrix.transpose(y)),np.subtract(1,np.matrix.transpose(y).dot(np.log(np.subtract(1,hyp(x,t))))))))


deneme = cost()
alpha = 0.01

for i in range(1000):
    theta = theta - ((alpha / m) * np.dot((data.T), g(np.dot(data, theta)) - target))
    print(cost())

deneme = hyp(val) - tar
input(deneme)
k = 0
for i in deneme:
    k += abs(i)

print(1 - k)
#
# def grad(t,x,y):
#    alpha = 0.01
#    for i in range(50000):
#        t = theta - (alpha/m * np.dot(np.transpose(x), np.subtract(g(np.dot(x,theta)),y)))
#        #print(t.shape)
#        print(cost(x,y,t)[0])
#        #a = input("deneme")
#    return t
#
# print(deneme)
# grad = grad(theta, data, target)
##print(grad)
# last = cost(data,target,theta)
#
# a = []
# for i in range(len(val)):
#    print("prediction == {}, real value/label == {}".format(hyp(val[i],grad), validate_target[i]))
#    #a.append(hyp(val[i],grad))
#
##aslan = tar - a
##deneme = 0
##for i in aslan:
##    deneme = deneme + i
##deneme = deneme / len(val)
##print(1 - deneme)
# print("finitooo")
#

