import random as rmd
import operaciones

def reglaFalsa(ecu):
  ecuacion = ecu
  cont = 0
  while True:
    Xa = operaciones.random()
    Xb = operaciones.random()
    if (operaciones.ecuacion(Xa, ecuacion))*(operaciones.ecuacion(Xb, ecuacion)) < 0:
      break
  while True:
    cont = cont + 1
    C = Xa - (((operaciones.ecuacion(Xa, ecuacion))*(Xb-Xa))/((operaciones.ecuacion(Xb, ecuacion))-(operaciones.ecuacion(Xa, ecuacion))))

    if abs((operaciones.ecuacion(Xa, ecuacion))*(operaciones.ecuacion(C, ecuacion))) <= 0.0001:
      break
  
    else:
      if (operaciones.ecuacion(Xa, ecuacion))*(operaciones.ecuacion(C, ecuacion)) < 0:
        Xb = C
      elif (operaciones.ecuacion(Xa, ecuacion))*(operaciones.ecuacion(C, ecuacion)) > 0:
        Xa = C
    return C, cont
  