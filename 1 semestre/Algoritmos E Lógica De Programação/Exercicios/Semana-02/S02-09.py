'''
Um banco concederá um crédito especial aos seus clientes de acordo com o saldo médio no último ano. 
Faça um programa que receba o saldo médio de um cliente e calcule o valor do crédito, de acordo com a tabela a seguir. 
Mostre o saldo médio e o valor do crédito.

    Saldo Médio                                                                Percentual
    ---------------------------------------------------------------------------------------------------
    Acima de R$ 400,00                                                         30% do saldo médio
    R$ 400,00 (incluso)  até R$ 300,00 (não incluso)                           25% do saldo médio
    R$ 300,00 (incluso) até R$ 200,00 (não incluso)                            20% do saldo médio
    Até R$ 200,00 (incluso)                                                    10% do saldo médio
'''

saldoMedio = float(input("Digite o seu saldo médio no último ano: "))

if(saldoMedio > 400):
    print(f"Saldo Médio: {saldoMedio} e seu Crédito Especial é: {saldoMedio * 0.30} ")
elif(saldoMedio > 300 and saldoMedio <= 400):
    print(f"Saldo Médio: {saldoMedio} e seu Crédito Especial é: {saldoMedio * 0.25} ")
elif(saldoMedio <= 300 and saldoMedio > 200):
    print(f"Saldo Médio: {saldoMedio} e seu Crédito Especial é: {saldoMedio * 0.20} ")
else:
    print(f"Saldo Médio: {saldoMedio} e seu Crédito Especial é: {saldoMedio * 0.10} ")
