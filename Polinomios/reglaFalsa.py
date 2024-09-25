import Operaciones
a = Operaciones.random(1); b = Operaciones.random(0)
def F(x): return 2 * x**2 - 8
Contador = 0
while True: 
    Contador += 1
    c = (a - ((F(a) * (b - a)) / (F(b) - F(a))))
    if (F(a) > 0 and F(c) < 0): a = c
    else: b = c
    if (F(c) <= 0.001): break
print("Resultado: ", c ," Iteraciones: ", Contador)
