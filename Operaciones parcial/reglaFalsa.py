import random
a = random.randint(-20,0); b = random.randint(0,20)
def F(x): return 2*x**3-5*x**3+2*x**5
Contador = 0; repeticion = 0; lista=[]; bandera = 0
while True: 
    bandera +=1 
    try:
        while True:
            repeticion += 1
            c = (a - ((F(a) * (b - a)) / (F(b) - F(a))))
            if (F(a) > 0 and F(c) < 0): a = c
            else: b = c
            if (abs(F(c)) <= 0.0000001): 
                if round(c,2) in lista: 
                    a = random.randint(-20,0); b = random.randint(0,20)
                else:
                    lista.append(round(c,2))
                    Contador += repeticion
                    repeticion = 0
            if  repeticion == 50000:
                a = random.randint(-20,0); b = random.randint(0,20)
                repeticion = 0
                break
    except: 
        a = random.randint(-20,0); b = random.randint(0,20)
    if(bandera == 10):break
        
print("Resultado: ", lista ," Iteraciones: ", Contador)