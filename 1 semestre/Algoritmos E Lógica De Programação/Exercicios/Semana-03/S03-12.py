# Validação do número de degraus
degraus = int(input("Digite o número de degraus da escada: "))
while degraus <= 0:
    print("Erro: o número de degraus deve ser positivo.")
    degraus = int(input("Digite novamente: "))

# Validação do valor inicial
inicio = int(input("Digite o valor inicial: "))
while inicio <= 0:
    print("Erro: o valor inicial deve ser positivo.")
    inicio = int(input("Digite novamente: "))

# Construção da escada
numero_atual = inicio

print("\nEscada Numérica:\n")

for i in range(1, degraus + 1):  # controla os degraus
    for j in range(i):           # controla quantos números no degrau
        print(numero_atual, end=" ")
        numero_atual += 1
    print()