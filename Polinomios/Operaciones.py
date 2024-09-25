def random(Opc):
    import random as rnd
    if (Opc == 0): resultadoRn = rnd.randint(0, 1000)
    if (Opc == 1): resultadoRn = rnd.randint(-1000, 0)
    if (Opc == 2): resultadoRn = rnd.randint(-1000, 1000)
    return resultadoRn

def aproximadoRnd():
    ResultadoAp = [0,0]
    ResultadoAp[0] = random(2)
    while True:
        ResultadoAp[1] += 1
        if (2 * ResultadoAp[0]) - 18 < 0:
            aux = ResultadoAp[0] + 0.2
            ResultadoAp[0] = aux
        else:
            aux = ResultadoAp[0] - 0.2
            ResultadoAp[0] = aux
        if abs(((2 * ResultadoAp[0])) - 18) <= 0.001: break
    return ResultadoAp

def Biseccion():
    ResultadoBc = [0,0]
    ResultadoBc[0] = random(0)
    X_1 = random(1)
    band = 0; C = 0
    while True:
        ResultadoBc[1] += 1
        if band == 0:
            if (3 * ResultadoBc[0]) - 27 > 0: band = 0.5
            if (3 * X_1) - 27 < 0 : band += 0.5
        if (band == 1): C = (ResultadoBc[0] + X_1)/2
        else:
            band = 0
            ResultadoBc[0] = random(0)
            X_1 = random(1)
        if (3 * C) - 27 > 0: ResultadoBc[0] = C
        if (3 * C) - 27 < 0: X_1 = C
        if abs(((3 * ResultadoBc[0])) - 27) <= 0.001: break
    return ResultadoBc

def reglaFalsa():
    a = random(1); b = random(0)
    def F(x): return x**4 - 16
    Contador = 0
    while True: 
        Contador += 1
        c = (a - ((F(a) * (b - a)) / (F(b) - F(a))))
        if abs(F(a)*F(c)) <= 0.001: break
        else:
            if (F(a)*F(c)) < 0: b = c
            if (F(a)*F(c)) > 0: a = c        
    print("Resultado: ", c ," Iteraciones: ", Contador)

def lista():
    import random as rn
    X_0 = rn.randint(-100,100)
    contador = 0
    while True:
        contador += 1
        if(abs(2*X_0**2-5*X_0+2) <= 0.001): break
        else:
            C = (X_0 - ((2*X_0**2-5*X_0+2) / (4*X_0-5)))
            X_0 = C
    return contador
