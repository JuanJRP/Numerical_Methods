import numpy as np
import matplotlib.pyplot as plt

def Pendiente(X,Y):
    Pendiente = np.sum((X - np.mean(X)) * (Y - np.mean(Y))) / np.sum((X - np.mean(X))**2)
    b = np.mean(Y) - Pendiente * np.mean(X)
    Yinicial= Pendiente * X + b
    plt.plot(X, Y,'.m',X,Pendiente*X+b,'-r')
    plt.show()

X = np.array([5, 7, 9, 11, 13])
Y = np.array([1.20, 1.35, 1.50, 1.60, 1.65])

Pendiente(X,Y)
