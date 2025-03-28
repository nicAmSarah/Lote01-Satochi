numeroVoltas = int(input("Digite o numero de voltas que você realizou\n"))
extensaoMetros= float(input("Digite a extensão do circuito em metros\n"))
tempoDuracao = int(input("Digite o tempo que durou em minutos\n"))

distancia = numeroVoltas * extensaoMetros

tempoHora = tempoDuracao/60

velocidadeMedia = distancia/tempoDuracao

print(f"a velocidade media é igual a {velocidadeMedia} km/h")