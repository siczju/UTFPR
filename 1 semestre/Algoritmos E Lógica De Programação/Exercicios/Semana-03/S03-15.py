decimal = int(input("Digite um número decimal: "))

print("\nOpções de conversão:")
print("1 - Decimal para Binário")
print("2 - Decimal para Octal")
print("3 - Decimal para Hexadecimal")

opcao = int(input("\nEscolha a opção: "))

if decimal == 0:
    print("\nResultado: 0")

else:
    resultado = ""
    numero = decimal

    if opcao == 1:
        base = 2
        digitos = "01"

    elif opcao == 2:
        base = 8
        digitos = "01234567"

    elif opcao == 3:
        base = 16
        digitos = "0123456789ABCDEF"

    else:
        print("Opção inválida!")
        exit()

    while numero > 0:
        resto = numero % base
        resultado = digitos[resto] + resultado
        numero = numero // base

    if opcao == 1:
        print(f"\nDecimal em binário: {resultado}")
    elif opcao == 2:
        print(f"\nDecimal em octal: {resultado}")
    elif opcao == 3:
        print(f"\nDecimal em hexadecimal: {resultado}")