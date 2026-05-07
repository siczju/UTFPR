vetor = [2,3,4,5,6,7,8,9]

for i in range(len(vetor)):
    if vetor[i] % 2 == 0 and vetor[i] % 3 == 0:
        print(f"O indice {i}, com o valor {vetor[i]} é múltiplo de 2 e 3")    
    elif vetor[i] % 2 == 0:
        print(f"O indice {i}, com o valor {vetor[i]} é múltiplo de 2")
    elif vetor[i] % 3 == 0:
        print(f"O indice {i}, com o valor {vetor[i]} é múltiplo de 3")
    else:
        print(f"O indice {i}, com o valor {vetor[i]} não é múltiplo de nada")
