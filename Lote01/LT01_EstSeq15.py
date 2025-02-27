import math

catetoA = float(input("Digite o valor do cateto adjacente para encontrar a hipotenusa"))
catetoO = float(input("Digite o valor do cateto oposto para encontrar a hipotenusa"))

hipotenusa =  catetoA*catetoA + catetoO*catetoO

print(math.sqrt(hipotenusa))
