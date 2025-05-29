def verificar_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

num1 = int(input("Digite um numero"))
num2 = int(input("Digite outro numero "))

menor = min(num1, num2)
maior = max(num1, num2)

print(f"Números primos entre {menor} e {maior}:")

for n in range(menor, maior + 1):
    if verificar_primo(n):
        print(n, end=' ')
