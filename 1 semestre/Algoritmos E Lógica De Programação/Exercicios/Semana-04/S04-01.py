vetor = [1,2,3,4,5,6]

# qtde de pares, quais sao os pares,  qtde de impares, quais sao os impares

qtdePares = 0
qtdeImpares = 0

pares = []
impares = []


for i in vetor:
    if i % 2 == 0:
        qtdePares += 1
        pares.append(i)
    else:
        qtdeImpares += 1
        impares.append(i)
    
print(f"Quantidade de pares: {qtdePares}")
print(f"Quantidade de impares: {qtdeImpares}")

print("Esses são os números pares: ", end="")
for i in pares:
    print(i, end=", ")

print("\nEsses são os números impares: ", end="")
for i in impares:
    print(i, end=", ")    