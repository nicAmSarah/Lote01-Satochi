num1 = float(input("Digite os numeros em ordem crescente:\nNumero 1"))
num2 = float(input("Numero 2:\n"))
num3 = float(input("Numero 3:\n"))
num4 = float(input("digite o quarto numero, esse pode ser fora de ordem"))

if num4 < num1:
    print(f"a ordem crescente fica {num4}, {num1}, {num2}, {num3}")
elif num4 > num1 and num4 < num2:
    print(f"a ordem crescente fica {num1}, {num4}, {num2}, {num3}")
elif num4 > num2 and num4 < num3:
    print(f"a ordem crescente fica {num1}, {num2}, {num4}, {num3}")
elif num4 > num3:
    print(f"a ordem crescente fica {num1}, {num2}, {num3}, {num4}")