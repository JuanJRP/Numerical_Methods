#Implemente un algoritmo de regresión lineal por aprendizaje, para un caso donde las entradas tengan más de una columna. 
#Asuma el conjunto de datos generados por el siguiente código:

import matplotlib.pyplot as plt
import numpy as np
x1_min, x1_max = 0,5
x2_min, x2_max = 0,3
x1_dim, x2_dim = np.meshgrid(np.arange( x1_min , x1_max , 0.1), np.arange( x2_min , x2_max , 0.1))
X1=x1_dim.ravel()
X2=x2_dim.ravel()
Y=2*X1 + 1.5*X2 + 3 + np.random.randn(*X1.shape) * 0.3

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(X1, X2, Y)
ax.set_title("Datos artificiales")
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('Y')
plt.show()
