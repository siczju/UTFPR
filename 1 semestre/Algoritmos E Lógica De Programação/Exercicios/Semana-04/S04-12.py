matriz = [[12,13,14,15], [14,15,16,18]]
qtdNum = 0
qtdPar = 0
soma = 0

for i in range(2):
    qtdNum = 0
    for j in range(4):
        if 12 <= matriz[i][j] <= 20:
            qtdNum += 1
        if matriz[i][j] % 2 == 0:
            qtdPar += 1
            soma += matriz[i][j]
    print(f"A qtd de numeros entre 12 a 20 na linha {i} foi {qtdNum}\n")

print(f"A media do pares é: {soma / qtdPar}")    