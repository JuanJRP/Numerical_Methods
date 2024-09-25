import random
def bisection(F):
    lista = []; contador = 0 
    X_0 = random.randint(5,7)
    X = random.randint(-7,-5)
    while contador < 100:
        C = (X + X_0) / 2
        if abs(F(C)) < 0.00001 or abs(X_0-X)/2 < 0.00001: 
            if round(C,2) not in lista:
                lista.append(round(C,2))
        if F(C) * f(X) > 0: X = C
        else: X_0 = C
        contador += 1
    return lista, contador

def f(x): return 2*x**3-5*x**3+2*x**5

lista, contador = bisection(f)

print(lista, contador)