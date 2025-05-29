def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        print(a, end=' ')
        a, b = b, a + b

def main():
    num = int(input("Digite o número de termos da série de Fibonacci: "))
    fibonacci(num)

main()
