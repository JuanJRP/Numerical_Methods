def random(Opc):
    import random as rnd
    if (Opc == 0): resultadoRn = rnd.randint(0, 1000)
    if (Opc == 1): resultadoRn = rnd.randint(-1000, 0)
    if (Opc == 2): resultadoRn = rnd.randint(-1000, 1000)
    return resultadoRn

def reglaFalsa():
    a = random(1); b = random(0)
    def F(x): return 2 * x**2 - 8
    Contador = 0
    while True: 
        Contador += 1
        c = (a - ((F(a) * (b - a)) / (F(b) - F(a))))
        if (F(a) > 0 and F(c) < 0): a = c
        else: b = c
        if (F(c) <= 0.001): break
    print("Resultado: ", c ," Iteraciones: ", Contador)

reglaFalsa()
