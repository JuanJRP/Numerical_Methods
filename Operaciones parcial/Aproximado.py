import random
def F(x): return 2*x**3-5*x**3+2*x**5
Contador = 0; lista=[]; repeticion = 0; bandera = 0
while True:
    bandera += 1
    x = random.randint(-50, 50)
    if F(x) > 0.001:
        while True:
            Contador += 1
            x = aux = x - 0.01
            if F(aux) <= 0.001:
                if round(aux,2) not in lista: lista.append(round(aux,2))
                break
    if bandera == 200: break

print("Resultado: ", lista ," Iteraciones: ", Contador)