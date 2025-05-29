num1 = int(input("Digite o primerio numero"))
num2 = int(input("Digite o segundo numero"))

if num1 < num2:
    for num1 in range(num1,num2, num1+1):
        primo = num1 % num1
        if primo == 0:
            print(f"numero {num1} é primo\n")
        