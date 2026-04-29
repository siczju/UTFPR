grupo = 1

while grupo <= 3:
    print(f"\n=== Grupo {grupo} ===")

    # Leitura dos valores
    A = int(input("Digite A: "))
    B = int(input("Digite B: "))
    C = int(input("Digite C: "))
    D = int(input("Digite D: "))
    E = int(input("Digite E: "))

    # Ordem digitada
    print("Ordem digitada:", A, B, C, D, E)

    # Ordenação manual (garantir A <= B <= C <= D <= E)
    if A > B:
        A, B = B, A
    if A > C:
        A, C = C, A
    if A > D:
        A, D = D, A
    if A > E:
        A, E = E, A

    if B > C:
        B, C = C, B
    if B > D:
        B, D = D, B
    if B > E:
        B, E = E, B

    if C > D:
        C, D = D, C
    if C > E:
        C, E = E, C

    if D > E:
        D, E = E, D

    # Ordem crescente
    print("Ordem crescente:", A, B, C, D, E)

    # Ordem decrescente
    print("Ordem decrescente:", E, D, C, B, A)

    # Segundo menor e segundo maior
    segundo_menor = B
    segundo_maior = D
    print("Segundo menor:", segundo_menor)
    print("Segundo maior:", segundo_maior)

    # Soma de pares e ímpares
    soma_pares = 0
    soma_impares = 0

    if A % 2 == 0:
        soma_pares += A
    else:
        soma_impares += A

    if B % 2 == 0:
        soma_pares += B
    else:
        soma_impares += B

    if C % 2 == 0:
        soma_pares += C
    else:
        soma_impares += C

    if D % 2 == 0:
        soma_pares += D
    else:
        soma_impares += D

    if E % 2 == 0:
        soma_pares += E
    else:
        soma_impares += E

    print("Soma dos pares:", soma_pares)
    print("Soma dos ímpares:", soma_impares)

    # Média ponderada (pesos 1,2,3,4,5)
    media_ponderada = (A*1 + B*2 + C*3 + D*4 + E*5) / 15
    print("Média ponderada:", media_ponderada)

    grupo += 1