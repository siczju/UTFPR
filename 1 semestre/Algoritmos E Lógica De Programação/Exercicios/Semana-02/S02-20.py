a = 12
b = 4

operacao = input("Digite a operação (soma, subtrai, multiplica, divide, potência): ")

match operacao:
    case "soma":
        resultado = a + b
        print(f"Resultado da soma: {resultado}")

    case "subtrai":
        resultado = a - b
        print(f"Resultado da subtração: {resultado}")

    case "multiplica":
        resultado = a * b
        print(f"Resultado da multiplicação: {resultado}")

    case "divide":
        if b != 0:
            resultado = a / b
            print(f"Resultado da divisão: {resultado}")
        else:
            print("Erro: divisão por zero não é permitida.")

    case "potência":
        resultado = a ** b
        print(f"Resultado da potência: {resultado}")

    case _:
        print("Operação inválida. Tente novamente.")