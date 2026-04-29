preco = float(input("Digite o preço do produto: R$ "))

if preco <= 50:
    percentual = 5
elif preco <= 100:
    percentual = 10
else:
    percentual = 15

aumento = preco * (percentual / 100)
novo_preco = preco + aumento

if novo_preco <= 80:
    classificacao = "Barata"
elif novo_preco <= 120:
    classificacao = "Normal"
elif novo_preco <= 200:
    classificacao = "Caro"
else:
    classificacao = "Muito Caro"

print(f"Preço original: R$ {preco:.2f}")
print(f"Percentual de aumento: {percentual}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo preço: R$ {novo_preco:.2f}")
print(f"Classificação: {classificacao}")