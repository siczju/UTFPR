valor = float(input("Digite o valor do carro: R$ "))

print("\nTabela de pagamento:")

# À vista (20% de desconto)
preco_vista = valor * 0.80
print(f"\nÀ vista (20% desconto):")
print(f"Preço final: R$ {preco_vista:.2f}")

print("\nParcelado:")
print("Parcelas | Preço Final | Valor da Parcela")

# Parcelamentos
for parcelas in range(6, 61, 6):
    
    if parcelas == 6:
        acrescimo = 0.03
    elif parcelas == 12:
        acrescimo = 0.06
    elif parcelas == 18:
        acrescimo = 0.09
    elif parcelas == 24:
        acrescimo = 0.12
    elif parcelas == 30:
        acrescimo = 0.15
    elif parcelas == 36:
        acrescimo = 0.18
    elif parcelas == 42:
        acrescimo = 0.21
    elif parcelas == 48:
        acrescimo = 0.24
    elif parcelas == 54:
        acrescimo = 0.27
    elif parcelas == 60:
        acrescimo = 0.30

    preco_final = valor + (valor * acrescimo)
    valor_parcela = preco_final / parcelas

    print(f"{parcelas:8} | R$ {preco_final:10.2f} | R$ {valor_parcela:10.2f}")