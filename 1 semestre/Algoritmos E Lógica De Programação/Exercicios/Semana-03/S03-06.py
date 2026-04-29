faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0
faixa5 = 0

for i in range(1, 16):
    print(f"\nPessoa {i}:")
    idade = int(input("Digite a idade: "))

    if idade <= 15:
        faixa1 += 1
    elif idade <= 30:
        faixa2 += 1
    elif idade <= 45:
        faixa3 += 1
    elif idade <= 60:
        faixa4 += 1
    else:
        faixa5 += 1

total = 15

perc_faixa1 = (faixa1 / total) * 100
perc_faixa5 = (faixa5 / total) * 100

print("\nQuantidade de pessoas em cada faixa etária:")
print("1ª faixa (até 15 anos):", faixa1)
print("2ª faixa (16 a 30 anos):", faixa2)
print("3ª faixa (31 a 45 anos):", faixa3)
print("4ª faixa (46 a 60 anos):", faixa4)
print("5ª faixa (acima de 60 anos):", faixa5)

print("\nPercentagens:")
print(f"1ª faixa: {perc_faixa1:.2f}%")
print(f"5ª faixa: {perc_faixa5:.2f}%")