# Vetores
produtos = []
codigos = []
precos = []

# Entrada de dados
for i in range(10):
    print(f"\nProduto {i+1}")

    nome = input("Nome do produto: ")
    codigo = int(input("Código do produto: "))
    preco = float(input("Preço do produto: "))

    produtos.append(nome)
    codigos.append(codigo)
    precos.append(preco)

# Relatório
print("\nRELATÓRIO DE PRODUTOS COM AUMENTO")
print("-" * 50)

for i in range(10):

    aumento = 0

    # Verifica as condições
    if codigos[i] % 2 == 0 and precos[i] > 1000:
        aumento = 0.20

    elif codigos[i] % 2 == 0:
        aumento = 0.15

    elif precos[i] > 1000:
        aumento = 0.10

    # Mostra apenas os que tiveram aumento
    if aumento > 0:
        novo_preco = precos[i] + (precos[i] * aumento)

        print(f"Produto: {produtos[i]}")
        print(f"Código: {codigos[i]}")
        print(f"Preço antigo: R$ {precos[i]:.2f}")
        print(f"Novo preço: R$ {novo_preco:.2f}")
        print("-" * 50)