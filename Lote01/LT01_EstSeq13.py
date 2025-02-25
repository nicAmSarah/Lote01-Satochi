quilos = float(input("Digite a quantidade em quilos para saber quanto tempo durará o alimento\n"))

quilos_em_gramas = quilos * 1000

dias_duraveis = int(quilos_em_gramas / 50)

print(f"A quantidade de {quilos}kg durará cerca de {dias_duraveis} dias")