import numpy as np
import matplotlib.pyplot as plt

def Varianza(X,Y):
    Pendiente = np.cov(X, Y)[0, 1] / np.var(X)
    b = np.mean(Y) - Pendiente * np.mean(X)
    Y_pred = Pendiente * X + b
    plt.plot(X, Y,'.k',X,Pendiente*X+b,'-b')
    plt.show()

X = np.array([5, 7, 9, 11, 13])
Y = np.array([1.20, 1.35, 1.50, 1.60, 1.65])

Varianza(X,Y)
