for i in range(1, 6):
    print(f"\nGrupo {i}:")
    
    A = float(input("Digite A: "))
    B = float(input("Digite B: "))
    C = float(input("Digite C: "))
    D = float(input("Digite D: "))

    print("\nOrdem lida:")
    print(A, B, C, D)

    # ORDEM CRESCENTE (método de trocas)
    a, b, c, d = A, B, C, D

    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if a > d:
        a, d = d, a
    if b > c:
        b, c = c, b
    if b > d:
        b, d = d, b
    if c > d:
        c, d = d, c

    print("Ordem crescente:")
    print(a, b, c, d)

    # ORDEM DECRESCENTE (ou reaproveita invertendo)
    print("Ordem decrescente:")
    print(d, c, b, a)