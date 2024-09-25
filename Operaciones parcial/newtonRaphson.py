import random 
X_0 = ram = 100
def F(x): return 2*x**3-5*x**3+2*x**5
contador = 0; repeticion = 0; lista=[]
while True: 
    try:
        while True:
            repeticion +=1
            if(abs(F(X_0)) <= 0.00000001): 
                if round(X_0,2) in lista: X_0 = ram = ram - 0.01
                else:
                    lista.append(round(X_0,2))
                    contador += repeticion
                    repeticion = 0
            if ram==-20 or repeticion == 50000: 
                X_0 = ram = ram - 0.01
                repeticion = 0
                break
            X_0 = C = (X_0 - (F(X_0) / (6*X_0**2-15*X_0**2+10*X_0**4)))
    except:  X_0 = ram = ram - 0.01
    if(ram <= -20):break
        
print ('El resultado es: ',lista,' y la cantidad de iteraciones es: ',contador)