nota1 = float(input("Digite sua primeira nota"))
nota2 = float(input("Digite sua segunda nota"))
nota3 = float(input("Digite sua terceira nota"))
nota4 = float(input("Digite sua quarta nota"))

if nota1 and nota2 and nota3 and nota4 < 10 :

    media = (nota1 + nota2 + nota3 + nota4 ) / 4

    if media >= 6.0:
        print(f"nota:{media} Aprovado")
    elif media >=3.0 and media < 6.0:
        print(f"nota:{media} Devera fazer exame")
    elif media < 3.0:
        print(f"nota:{media} retido")

else:
    print("nao")