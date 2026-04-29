# Programa para processar 5 grupos de 4 valores

grupo = 1

while grupo <= 5:
    print(f"\n=== Grupo {grupo} ===")

    # Leitura dos valores
    A = int(input("Digite o valor A: "))
    B = int(input("Digite o valor B: "))
    C = int(input("Digite o valor C: "))
    D = int(input("Digite o valor D: "))

    # Mostrar na ordem digitada
    print("Ordem digitada:", A, B, C, D)

    # Ordenação (método de trocas)
    # Garantir A <= B <= C <= D
    if A > B:
        A, B = B, A
    if A > C:
        A, C = C, A
    if A > D:
        A, D = D, A
    if B > C:
        B, C = C, B
    if B > D:
        B, D = D, B
    if C > D:
        C, D = D, C

    # Ordem crescente
    print("Ordem crescente:", A, B, C, D)

    # Ordem decrescente
    print("Ordem decrescente:", D, C, B, A)

    # Maior e menor
    menor = A
    maior = D
    print("Menor valor:", menor)
    print("Maior valor:", maior)

    # Média
    media = (A + B + C + D) / 4
    print("Média:", media)

    # Mediana (para 4 valores = média dos dois centrais)
    mediana = (B + C) / 2
    print("Mediana:", mediana)

    grupo += 1