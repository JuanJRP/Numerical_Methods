import random as rn
X_0 = rn.randint(-100,100)
contador = 0
while True:
    contador += 1
    if(abs(5*X_0**2+5*x) <= 0.001): break
    else:
        C = (X_0 - ((2*X_0**2-5*X_0+2) / (4*X_0-5)))
        X_0 = C
print ('El resultado es: '+ str(X_0) + ' y la cantidad de iteraciones es: ' + str(contador))
