num = int(input("digite o valor do numeto:"))

soma = 0
result = 0

for i in range(1, n + 1):
    serie = 1 / i
    result = serie + result

print(f"a série é: {result:.2f}")
