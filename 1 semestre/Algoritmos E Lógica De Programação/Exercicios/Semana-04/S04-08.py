vetor1 = [4,7,5,8,2,15,9,6,10,11]
vetor2 = [3,4,5,8,2]

vetorResultante1 = []
vetorResultante2 = []
soma = 0

for i in range(len(vetor1)):
    soma = 0
    if vetor1[i] % 2 == 0:
        for j in range(len(vetor2)):
            soma += vetor2[j]
        soma += vetor1[i]
        vetorResultante1.append(soma)

qtdDivisores = 0
for i in range(len(vetor1)):
    qtdDivisores = 0
    if vetor1[i] % 2 !=  0:
        for j in range(len(vetor2)):
            if vetor1[i] % vetor2[j] == 0:
                qtdDivisores += 1
        vetorResultante2.append(qtdDivisores)

print(vetorResultante1)
print(vetorResultante2)