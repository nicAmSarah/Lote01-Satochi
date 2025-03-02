num1 = int(input("Digite o primeiro numero"))
num2 = int(input("Digite o segundo numero"))

if num1 > num2:
    if num1%num2 == 0:
        print(f"o {num1} é multiplo do {num2}")
    elif num1%num2 != 0:
        print("Os numeros não são multiplos")
elif num2 > num1:
    if num2%num1 ==0:
        print(f"o {num2} é multiplo do {num1}")
    elif num1%num2 != 0:
        print("Os numeros não são multiplos")

