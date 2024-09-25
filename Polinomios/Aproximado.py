import random as rnd
X = rnd.randint( -100, 100)
print("El numero random es: ", X)
Contador = 0
while True:
    Contador += 1
    if (2*X**5-8*X**3+12*X) < 0:
        aux = X + 1
        X = aux
        print((X))
    else:
        aux = X - 1
        X = aux
        print(X)
    if abs(2*X**5-8*X**3+12*X) <= 0:
        print('Felicidades, la respuesta es: ', X)
        print('El número de iteraciones es: ', Contador)
        break
