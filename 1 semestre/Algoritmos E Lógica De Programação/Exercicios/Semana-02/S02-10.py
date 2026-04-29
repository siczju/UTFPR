'''
O custo ao consumidor de um carro novo é a soma do custo de fábrica com a porcentagem do distribuidor e com os impostos,
ambos aplicados ao custo de fábrica.

Sabe-se que as porcentagens são as mesmas que estão na tabela a seguir. Faça um programa que receba o custo de fábrica
de um carro e mostre o custo ao consumidor.

    Custo de Fábrica                                             % do distribuidor                 % dos impostos
    ------------------------------------------------------------------------------------------------------------------
    até R$ 12.000,00                                                   05                              Isento
    entre R$ 12.000,00 e R$ 25.000,00                                  10                               15
    acima de R$ 25.000,00                                              15                               20

'''

custoDeFabrica = float(input("Digite o custo de fábrica do carro novo: "))

if custoDeFabrica < 12000:
    print(f"O custo total com os impostos de 5%: {(custoDeFabrica) + (custoDeFabrica * 0.05) }")
elif custoDeFabrica >= 12000 and custoDeFabrica <= 25000:
    print(f"O custo total com os impostos de 25%: {(custoDeFabrica) + (custoDeFabrica * 0.25) }")
else:
    print(f"O custo total com os impostos de 35%: {(custoDeFabrica) + (custoDeFabrica * 0.35)}")
