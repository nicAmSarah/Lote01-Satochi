horas_trabalhadas = int(input("Quantas horas você trabalha por dia?"))
valor_por_hora = float(input("Quanto você ganha por hora"))
desconto = float(input("Quantos porcento(%) será descontado do seu salário"))
dependentes = int(input("Quantos dependentes você possui?"))

salario = horas_trabalhadas * valor_por_hora
salario_liquido = salario -  ((salario * desconto) / 100)
valor_de_dependentes = dependentes * 100
salario_liquido = salario_liquido + valor_de_dependentes

print(salario_liquido)