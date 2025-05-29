def receberValores():
    num1 = int(input("Digite um valor: "))
    num2 = int(input("Digite outro valor: "))
    return num1, num2

def maior_menor(num1, num2):
    if num1 > num2:
        maior = num1
        menor = num2
    else:
        maior = num2
        menor = num1
    return maior, menor

def somatoria(menor, maior):
    soma = 0
    for i in range(menor, maior + 1):
        if i % 2 == 1:
            soma += i
    return soma

def main():
    num1, num2 = receberValores()
    maior, menor = maior_menor(num1, num2)
    soma = somatoria(menor, maior)
    print(soma)

main()
