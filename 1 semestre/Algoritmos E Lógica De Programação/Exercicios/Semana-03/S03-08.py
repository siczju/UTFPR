total_vista = 0
total_prazo = 0

for i in range(1, 16):
    print(f"\nTransação {i}:")
    
    codigo = input("Digite o código (V para à vista / P para a prazo): ").upper()
    valor = float(input("Digite o valor da transação: R$ "))

    if codigo == "V":
        total_vista += valor
    elif codigo == "P":
        total_prazo += valor
    else:
        print("Código inválido! Considerando como 0.")

total_geral = total_vista + total_prazo
primeira_prestacao = total_prazo / 3

print("\nRESULTADOS:")
print(f"Total à vista: R$ {total_vista:.2f}")
print(f"Total a prazo: R$ {total_prazo:.2f}")
print(f"Total geral: R$ {total_geral:.2f}")
print(f"Valor da primeira prestação (3x): R$ {primeira_prestacao:.2f}")