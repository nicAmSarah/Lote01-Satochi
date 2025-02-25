deposito_poupanca = float(input("Quanto vc deseja depositar"))

rendimento = deposito_poupanca * 0.013

saldo_poupanca = rendimento + deposito_poupanca

print(f"o valor de {deposito_poupanca} rendeu cerca de {rendimento} nesse mes. Seu saldo atual é de {saldo_poupanca}")