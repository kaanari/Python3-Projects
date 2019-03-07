import numpy as np
from sklearn.datasets import make_regression


def dataset():
    rng = np.random.RandomState(1)
    X = list(map(lambda x: 5 * x, rng.rand(50)))
    y = list(map(lambda x: (x * 0.4 + float(rng.rand(1))), X))

    return X,y

def dataset_n():
    import numpy as np
    n = 15
    k = 500
    rng = np.random.RandomState(1)
    X = np.array(list(map(lambda x: 5 * x, rng.rand(n * k))))
    X = X.reshape((k, n))
    ones = np.ones((500, 1), dtype=float)
    Y = np.array(list(map(lambda x: (x[0] * 0.4 + rng.rand(1))[0], X)))
    X = np.c_[X, np.ones(500)]
    return X,Y

def dataset_n1():
    X, y = make_regression(n_samples=500, n_features=16, noise=0.1)
    return X,y

