import numpy as np
import matplotlib.pyplot as plt

def minimosCuadrados(X,Y):
    n = len(X)
    sumX = np.sum(X)
    sumY = np.sum(Y)
    sumXY = np.sum(X * Y)
    sumXX = np.sum(X * X)
    m = (n * sumXY - sumX * sumY) / (n * sumXX - sumX * sumX)
    b = (sumY - m * sumX) / n
    Y_pred = m * X + b
    plt.plot(X, Y,'.k',X,m * X + b,'-b')
    plt.show()

X = np.array([5, 7, 9, 11, 13])
Y = np.array([1.20, 1.35, 1.50, 1.60, 1.65])

minimosCuadrados(X,Y)
