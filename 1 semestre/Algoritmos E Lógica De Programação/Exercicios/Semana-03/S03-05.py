for i in range(1, 16):
    print(f"\nCliente {i}:")
    
    nome = input("Digite o nome do cliente: ")
    valor = float(input("Digite o valor das compras no ano passado: R$ "))

    if valor < 1000:
        bonus = valor * 0.10
    else:
        bonus = valor * 0.15

    print("\nResultado:")
    print("Nome:", nome)
    print(f"Bônus: R$ {bonus:.2f}")