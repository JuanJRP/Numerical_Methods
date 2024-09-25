# Librerías necesarias
import random
import numpy as np
import matplotlib.pyplot as plt

# Generar datos de ejemplo
x1_min, x1_max = 0,5
x2_min, x2_max = 0,3
x1_dim, x2_dim = np.meshgrid(np.arange(x1_min, x1_max, 0.1), np.arange(x2_min, x2_max, 0.1))
X1 = x1_dim.ravel()
X2 = x2_dim.ravel()
Y = 2 * X1 + 1.5 * X2 + 3 + np.random.randn(*X1.shape) * 0.3

#coeficientes de regresión aleatoriamente
b0 = random.randint(-1, 1)
b1 = random.randint(-1, 1)
b2 = random.randint(-1, 1)

# Opciones adicionales
display_step = 10 #Cada cuantas iteraciones deseamos ver los resultados
N = len(X1)
loss = []

# Proceso de optimización
epochs = 500
learning_rate = 0.01
convergence_criteria = 1e-5 #0.00001

# Cracion del espacio de graficas, una 2D(MSE) y otra 3D(DATOS)
fig = plt.figure(figsize=(12,5))
axes1 = fig.add_subplot(1, 2, 1, projection='3d')
axes2 = fig.add_subplot(1, 2, 2)

for step in range(epochs+1):
    error = 0

    # Calculamos el error y con ello, el gradiente Modelo: Y = b0 + b1 * X1 + b2 * X2
    Yp = (b0 + b1 * X1 + b2 * X2)# Modelo: Y = b0 + b1 * X1 + b2 * X2
    Diferencia = Yp - Y
    error += np.mean(Diferencia ** 2) # MSE

    # Calculamos el gradiente
    b0_gradient = 2 * np.mean(Diferencia)
    b1_gradient = 2 * np.mean(Diferencia * X1)
    b2_gradient = 2 * np.mean(Diferencia * X2)        

    # Caculamos el MSE
    MSE = error/N 

    # Actualizamos los valores de acuerdo al gradiente
    b0 -= learning_rate * b0_gradient
    b1 -= learning_rate * b1_gradient
    b2 -= learning_rate * b2_gradient

    # Guardamos el objetivo por cada epoca
    loss.append(np.abs(MSE))

    # Mostramos cada display_step epocas haciendo el modulo
    if step % display_step == 0: 
        # Limpieza de las graficas para su actualizacion
        axes1.clear()
        axes2.clear()
        axes1.scatter(X1, X2, Y, c="b")# Plasmamos los puntos
        axes1.set_title(f"Datos & Modelo\nEpoca: {step}")
        pred_y = b0 + b1 * X1 + b2 * X2 # Modelo: Y = b0 + b1 * X1 + b2 * X2
        axes1.plot_wireframe(x1_dim, x2_dim, pred_y.reshape(x1_dim.shape), color='r', alpha=0.5)# Linea de prediccion
        axes1.set_xlabel('X1')
        axes1.set_ylabel('X2')
        axes1.set_zlabel('Y')
        axes2.plot(loss)# Grficacion de la linea de perdida 
        axes2.set_title(f"Costo (MSE)\nMSE: {MSE}")
        axes2.set_xlabel("Epochs")
        axes2.set_ylabel("MSE")
        fig.suptitle('Regresión lineal por aprendizaje 3D')
        plt.show(block = False)# Continuar generando graficas sin que se bloquee
        plt.pause(0.5)# Tiempo de actualizacion de la grafica teniendo en cuenta el dysplay_Step

    # Paramos el algoritmo cuando los hiperparámetros no estén cambiando lo suficiente y el MSE sea menor a 1
    if max(abs(learning_rate * b1_gradient), abs(learning_rate * b2_gradient)) <= convergence_criteria and MSE < 1:
        break

#=============Impresión de los resultados==========
print("===============================Impresión de los resultados============================")
print('')
print(f"Finalizado en {step} iteraciones ")
print("")
print(f"Los valores obtenidos son: \nb0 = {b0} \nb1 = {b1}  \nb2 = {b2}")
print('')
print(f'MSE= {MSE}')
print("")
print("======================================================================================")

#Realizacion de predicciones
while True:
    X_1 = float(input('Ingrese un valor X1: '))
    X_2 = float(input('Ingrese un valor X2: '))
    pre_y = b0 + b1 * X_1 + b2 * X_2
    print(f'Según el valor de entrada {X_1}, {X_2} la salida será: {pre_y}')
    