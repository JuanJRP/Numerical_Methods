import random as rn
Xa = rn.randint(-100 , 0); Xb = Xa * -1
def Fx(X): return 2*X**3-8*X**2+5*X-2
contador = 0
while True:
    contador += 1
    fx = (Fx(Xa) - Fx(Xb)) / (Xa - Xb)
    if(abs(Fx(Xa)) <= 0.001): break
    else:
        Xc = Xa - (Fx(Xa) / fx)
        Xa = Xc
print ('El resultado es: '+ str(Xa) + ' y la cantidad de iteraciones es: ' + str(contador))
