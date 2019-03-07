import numpy as np
import sklearn
from sklearn.datasets import load_breast_cancer
from sklearn import preprocessing

dataset = load_breast_cancer()
total_data_len,total_feature_len = dataset.data.shape

data_len = int(8*total_data_len/10)
train_len = total_data_len - data_len


features = dataset['data'][0:data_len]
features = preprocessing.scale(features)
print(features)
features = np.insert(features,0,1,axis=1)
labels = dataset['target'][0:data_len]
label_names = dataset['target_names']

test_features = dataset['data'][data_len:total_data_len]
test_features = preprocessing.scale(test_features)
test_features = np.insert(test_features,0,1,axis=1)
test_labels = dataset['target'][data_len:total_data_len]
data_len,feature_len = features.data.shape

alfa = 0.01
iteration = 50000


theta = np.zeros(feature_len, dtype=float)


def sigmoid(x):

    return 1. / (1 + np.exp(-x))


def hypotesis(features,theta):
    z = sigmoid(np.dot(features, theta))
    return z

def cost_function(features,theta,labels,data_len):
    z = 0
    for i in range(data_len):
        z += labels[i]*np.log(hypotesis(features[i],theta)) + (1 - labels[i])*np.log(1-hypotesis(features[i],theta))

    J = (-1/data_len)*z
    return J

def cost_function2(features,weights ,labels,data_len):

    predictions = hypotesis(features, weights)
    class1_cost = -np.dot(labels,np.log(predictions))
    class2_cost = np.dot((1-labels),np.log(1-predictions))
    cost = class1_cost - class2_cost
    cost = cost / data_len

    return cost

def update(theta,alfa,data_len,features,labels):

    theta = theta - (alfa/data_len)*np.dot(features.T,hypotesis(features,theta)-labels)
    print(theta.shape)

    return theta


def test(train_features,train_labels,label_names,test):
    prediction = hypotesis(train_features,theta)
    test.append(abs(train_labels - prediction))
    if prediction >= .5:
        predict_label = 1
        label_name = label_names[1]
    else:
        label_name = label_names[0]
        predict_label = 0



    print("Predicted Label = "+ str(predict_label) +", Possibility = %"+str(prediction*100)+", Predicted Cancer Type = "+str(label_name)+" ||| Real Label = "+str(train_labels)+", Real Cancer Type = "+str(label_names[train_labels])+"")


cost_history = []
for i in range(iteration):

    weights = update(theta, alfa,data_len,features,labels)
    cost = cost_function2(features, theta,labels, data_len)
    cost_history.append(cost)
    theta = weights
    print(cost)
    # Log Progress
    if i % 1000 == 0:
        print("iter: " + str(i) + " cost: " + str(cost))
test_result = []

for i in range(train_len):
    test(test_features[i],test_labels[i],label_names,test_result)

sum = 0
for i in test_result:
    sum += i
sum = sum / train_len
print(1-sum)