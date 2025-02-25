from math import sqrt

coeA = float(input("digite o valor do coeficienteA de uma equação do segundo grau.\n"))
coeB = float(input("digite o valor do coeficienteB de uma equação do segundo grau.\n"))
coeC = float(input("digite o valor do coeficienteC de uma equação do segundo grau.\n"))

delta = (coeB*coeB - (4*coeA*coeC))

raizP = (-(coeB) + delta**0.5)/2*coeA

raizN = (-(coeB) - sqrt(delta))/2*coeA

print(raizP,raizN)