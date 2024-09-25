import random
import numpy as np
import matplotlib.pyplot as plt
# Librerías necesarias

x1_min, x1_max = 0,5
x2_min, x2_max = 0,3
x1_dim, x2_dim = np.meshgrid(np.arange(x1_min, x1_max, 0.1), np.arange(x2_min, x2_max, 0.1))
X1 = x1_dim.ravel()
X2 = x2_dim.ravel()
Y = 2 * X1 + 1.5 * X2 + 3 + np.random.randn(*X1.shape) * 0.3

# Valores iniciales
m = random.randint(0, 5)
b = random.randint(0, 5)

# Opciones adicionales
display_step = 50 #Cada cuantas iteraciones deseamos ver los resultados
N = len(X1)
loss = [] 

# Proceso de optimización
epochs = 2000
learning_rate = 0.01
convergence_criteria = 1e-5 #0.00001

# Cracion del espacio de graficas, una 2D(MSE) y otra 3D(DATOS)
fig = plt.figure(figsize=(12,5))
axes1 = fig.add_subplot(1, 2, 1, projection='3d')
axes2 = fig.add_subplot(1, 2, 2)

for step in range(epochs+1):
  # Gradientes iniciales (Zero gradients)
  m_gradient = 0
  b_gradient = 0
  error = 0
  Diferencia = 0

  # Calculamos el error y con ello, el gradiente Modelo: Y = m*X1 + mX2 + b
  for i in range(N):
    Yp = (m*X1[i] + m*X2[i] + b)# Modelo: Y = m*X1 + mX2 + b
    Diferencia = Yp - Y[i]
    error += (Diferencia)**2 # MSE
    # Calculamos el gradiente
    m_gradient += (2/N)*(Diferencia)*X1[i] 
    b_gradient += (2/N)*(Diferencia)*1

  MSE = error/N # Caculamos el MSE
  # Actualizamos los valores de acuerdo al gradiente
  m = m - ( m_gradient * learning_rate )
  b = b - ( b_gradient * learning_rate )
  # Guardamos el objetivo por cada epoca
  loss.append(np.abs(MSE))

  # Mostramos cada display_step epocas haciendo el modulo
  if step % display_step == 0: 
    # Limpieza de las graficas para su actualizacion
    axes1.clear()
    axes2.clear()
    axes1.scatter(X1, X2, Y, c="b")# Plasmar los puntos
    axes1.set_title(f"Datos & Modelo\nEpoca: {step}")
    pred_x1, pred_x2 = np.meshgrid(np.array([0, max(X1)]), np.array([0, max(X2)]))# Calculamos la prediccion para X1 Y X2
    pred_y = m*pred_x1 + m*pred_x2 + b # Modelo: Y = m*X1 + mX2 + b
    axes1.plot_surface(pred_x1, pred_x2, pred_y, color='r',linewidth=0.5, alpha= 0.5)# Linea de prediccion
    axes1.set_xlabel('X1')
    axes1.set_ylabel('X2')
    axes1.set_zlabel('Y')
    axes2.plot(loss)# Grficacion de la linea de perdida 
    axes2.set_title(f"Costo (MSE)\nMSE: {MSE}")
    axes2.set_xlabel("Epochs")
    axes2.set_ylabel("MSE")
    fig.suptitle('Regresión lineal por aprendizaje 3D')
    plt.show(block = False)# Continuar generando graficas sin tener que cerrar la anterior
    plt.pause(0.5)# Tiempo de actualizacion de la grafica teniendo en cuenta el dysplay_Step

  # Paramos el algoritmo cuando los hiperparámetros no estén cambiando lo suficiente
  if max(abs(learning_rate * m_gradient), abs(learning_rate * b_gradient)) <= convergence_criteria:
    break

# =============Impresión de los resultados==========
print("===============================Impresión de los resultados============================")
print("")
print(f"Los valores obtenidos son: m = {m} y b = {b}")
print(f"Finalizado en {step} iteraciones ")
print('')
print(f'MSE= {MSE}')
print("")
print("======================================================================================")
input() # Pausa para mantener las grafica
