import Operaciones
X = Operaciones.random(0)
X_1 = Operaciones.random(1)
Contador = 0; band = 0; C = 0
while True:
    Contador += 1
    if band == 0:
        if (2*X**2-5*X+2)> 0: band = 0.5
        if (2*X**2-5*X+2) < 0 : band += 0.5
        print("El numero random positivo es: ", X, " y el negativo es: ", X_1)
    if (band == 1): C = (X + X_1)/2
    else: 
        print ("No es posible operar con estos numeros.",X , X_1)
        band = 0
        X = Operaciones.random(0)
        X_1 = Operaciones.random(1)
    if (2*X**2-5*X+2) > 0: X = C
    if (2*X**2-5*X+2) < 0: X_1 = C
    if abs((2*X**2-5*X+2)) <= 0.001:
        print('Felicidades, la respuesta es: ', X)
        print('El número de iteraciones es: ', Contador)
        break
