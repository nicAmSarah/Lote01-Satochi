hora_Inicio = int(input("Digite apenas a hora que você iniciou o jogo. Ex: se você iniciou as 10:30 da manhã, digitar apenas 10"))
minutos_inicio = int(input("Digite apenas os minutos que você iniciou"))
hora_Fim = int(input("Digite apenas a hora que você terminou o jogo. Ex: se você terminou as 10:30 da manhã, digitar apenas 10"))
minutos_fim = int(input("Digite apenas os minutos que você terminou"))

if hora_Inicio > 23 or hora_Inicio > 23:
    print("A hora deve estar entre o periodo 00h e 23h")
elif minutos_fim > 59 or minutos_inicio > 59:
    print("A hora deve estar entre o periodo 00h e 23h")

