# Entrada de dados
tipo = int(input("Digite o tipo de investimento (1, 2 ou 3): "))
valor = float(input("Digite o valor do investimento: R$ "))

if tipo == 1:
    rendimento = 0.03
    descricao = "Poupança"
elif tipo == 2:
    rendimento = 0.04
    descricao = "Fundo de Renda Fixa"
elif tipo == 3:
    rendimento = 0.05
    descricao = "Fundo de Renda Variável"
else:
    print("Tipo de investimento inválido!")
    exit()

valor_corrigido = valor + (valor * rendimento)

print(f"Tipo de investimento: {descricao}")
print(f"Valor aplicado: R$ {valor:.2f}")
print(f"Rendimento: {rendimento * 100}% ao mês")
print(f"Valor corrigido: R$ {valor_corrigido:.2f}")