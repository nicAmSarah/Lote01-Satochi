precoAtual = float(input("Digite o preço atual do produto\n"))
mediaVenda = int(input("Digite a media de quanto esse produto é vendido na loja\n"))

if mediaVenda <500 and precoAtual < 30:
    novoPreco = precoAtual + (precoAtual*0.10)
    print(f"O preço houve um aumento de 10%, ficando R${novoPreco}")
elif (mediaVenda >= 500 and mediaVenda < 1000) and (precoAtual >=30 and mediaVenda < 80):
    novoPreco =  precoAtual + (precoAtual*0.15)
    print(f"O preço houve um aumento de 15%, ficando R${novoPreco}")
elif mediaVenda >= 1000 and precoAtual >= 80:
    novoPreco = precoAtual - (precoAtual*0.05)
    print(f"O preço houve um ajuste de -5% devido sua alta demanda, ficando R${novoPreco}")
else:
    novoPreco = precoAtual
    print(f"O preço não houve alteração, ele se manteve em R${novoPreco}")
