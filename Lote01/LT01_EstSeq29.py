tipoInvestimento = int(input("Digite o tipo de conta que você ira investir\n [1] - Poupança\n [2] - Renda Fixa\n"))
valorInvestimento = float(input("Qual o valor que você deseja investir?"))

if tipoInvestimento == 1 or tipoInvestimento == 2:
    if tipoInvestimento == 1:
        investimento = valorInvestimento + (valorInvestimento*0.03)
        print(f"o valor de R${valorInvestimento} foi investido em 3%, totalizando {investimento}")
    else:
        investimento = valorInvestimento + (valorInvestimento*0.03)
        print(f"o valor de R${valorInvestimento} foi investido em 5%, totalizando {investimento}")
else:
    print("não valido")