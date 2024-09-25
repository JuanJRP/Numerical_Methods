import random 
Xa = random.randint(-20 , 0); Xb = random.randint(0,20)
def Fx(X): return 2*X**3-5*X**3+2*X**5
contador = 0; repeticion = 0; lista=[]; bandera = 0
while True:
    bandera += 1
    try:
        while True:
            repeticion += 1
            fx = (Fx(Xa) - Fx(Xb)) / (Xa - Xb)
            Xc = Xa - (Fx(Xa) / fx)
            Xa = Xc
            print(Xa)
            if(abs(Fx(Xa)) <= 0.0001): 
                if round(Xa,2) in lista:
                    Xa = random.randint(-20 , 0); Xb = random.randint(0,20)
                else:
                    lista.append(round(Xa,2))
                    contador += repeticion
                    repeticion = 0
            if repeticion == 10000:
                Xa = random.randint(-20 , 0); Xb = random.randint(0,20)
                repeticion = 0
                break
    except:
        Xa = random.randint(-20 , 0); Xb = random.randint(0,20)
    if bandera == 10: break
print ('El resultado es: ',lista, ' y la cantidad de iteraciones es: ', contador)
