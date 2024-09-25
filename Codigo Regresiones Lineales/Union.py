import numpy as np
import matplotlib.pyplot as plt

j = 0
i = 0

while True:
    try:
        N = input('\nIngrese el numero de la cantidad de datos: ')
        while True:
            if(j < int(N)):
                X = np.empty(int(N), dtype="float")
                print('\nIngrese los valores en X uno a uno:\n')
                while i < int(N):
                    try:
                        X[i] = input(f"Valor {i}: ")
                        j+=1
                        i+=1
                    except:
                        print('No ha ingresado un número válido. Inténtelo de nuevo.')
                print('\nDatos en X: ',X)
            else:
                Y = np.empty(int(N), dtype="float")
                print('\nIngrese los valores en Y uno a uno:\n')
                i = 0
                while i < int(N):
                    try:
                        Y[i] = input(f"Valor {i}: ")
                        j+=1
                        i+=1
                    except:
                        print('No ha ingresado un número válido. Inténtelo de nuevo.')
                print('\nDatos en Y: ',Y)
            if(j >= int(N)*2 ):break
        break
    except:
        print('No ha ingresado un número válido. Inténtelo de nuevo.')


def Pendiente(X,Y):
    Pendiente = np.sum((X - np.mean(X)) * (Y - np.mean(Y))) / np.sum((X - np.mean(X))**2)
    b = np.mean(Y) - Pendiente * np.mean(X)
    Resultado = Pendiente * X + b
    print(f'\nPendiente: Y = {Pendiente} * X + {b}')
    return Resultado

def Varianza(X,Y):
    Pendiente = np.cov(X, Y)[0, 1] / np.var(X)
    b = np.mean(Y) - Pendiente * np.mean(X)
    Resultado = Pendiente * X + b
    print(f'\nVarianza: Y = {Pendiente} * X + {b}')
    return Resultado

def minimosCuadrados(X,Y):
    n = len(X)
    sumX = np.sum(X)
    sumY = np.sum(Y)
    sumXY = np.sum(X * Y)
    sumXX = np.sum(X * X)
    m = (n * sumXY - sumX * sumY) / (n * sumXX - sumX * sumX)
    b = (sumY - m * sumX) / n
    Resultado = m * X + b
    print(f'\nMinimos cuadrados: Y = {m} * X + {b}')
    return Resultado

fig, axs = plt.subplots(1, 3, figsize=(12, 4))
plt.subplots_adjust(wspace=0.3, top=0.75)
plt.suptitle(f'X: {X}\nY: {Y}', fontsize=16)
axs[0].plot(X, Pendiente(X,Y), '-b')
axs[0].set_title('Regresión lineal por pendiente')
axs[0].grid()
axs[1].plot(X, Varianza(X,Y), '-b')
axs[1].set_title('Regresión lineal por varianza')
axs[1].grid()
axs[2].plot(X, minimosCuadrados(X,Y), '-b')
axs[2].set_title('Regresión lineal por mínimos cuadrados')
axs[2].grid()
for ax in axs: ax.plot(X, Y, 'o', color='black')
plt.show()
