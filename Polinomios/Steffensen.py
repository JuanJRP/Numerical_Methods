import random
Xc=Xa=ram=random.randint(0,20)
def F(x): return 2*x**5-5*x+2
Contador=0; repeticion = 0; lista=[]
while True:
    try:
        while True:
            repeticion +=1
            if (abs(F(Xc)) <= 0.00001):
                if round(Xa,2) in lista: Xa=ram=ram-1
                else:
                    lista.append(round(Xa,2))
                    Contador += repeticion
            if ram==-20 or repeticion == 50000: 
                Xc=Xa=ram=ram-1
                repeticion = 0
                break
            Xa=Xc=Xa-((F(Xa)**2)/((F(Xa+F(Xa))-F(Xa))))
    except: Xc=Xa=ram=ram-1
    if(ram <= -20):break
print("Resultado: ", lista ," Iteraciones: ", Contador)
