matriz = []
qtdNum = 0

for i in range(3):
    lista = []
    for j in range(5):
        lista.append(int(input(f"Adicione o valor para a matriz[{i}][{j}]: ")))
        if 15 <= lista[j] <= 20:
            qtdNum += 1
    matriz.append(lista)

print(matriz)
print(f"A quantidade de numeros entre 15 e 20 é: {qtdNum}")