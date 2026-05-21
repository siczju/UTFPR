'''Faça um programa que leia um vetor de dez posições. Em seguida criei um segundo vetor compactado em relação ao primeiro.
 Isto é, retirar todos os valores nulos e negativos colocando somente os valores positivos e diferentes de zero no segundo
vetor.

Mostrar o vetor resultante.

Observações:
Pode usar o comando append() para adicionar os valores no vetor. 
Os elementos do vetor devem ser acessados através do seus respectivos índices.'''

vetor = []

for i in range(10):
    valor = int(input(f"Digite o valor da posição {i}: "))
    vetor.append(valor)

compactado = []

for i in range(len(vetor)):
    if vetor[i] > 0:
        compactado.append(vetor[i])

# Mostra o vetor resultante
print("Vetor compactado:", compactado)