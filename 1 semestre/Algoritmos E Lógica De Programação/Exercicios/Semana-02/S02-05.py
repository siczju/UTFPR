n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))


escolha = int(input(
      "\n\t 1. Média entre os números digitados" +
      "\n\t 2. Diferença do maior pelo menor" +
      "\n\t 3. Produto entre os números digitados" +
      "\n\t 4. Divisão do primeiro pelo segundo\n" +
            "\nQual operação deseja fazer: "))

if(escolha == 1):
    print("Media: ", (n1 + n2) / 2)
elif(escolha == 2):
    print("Diferença: ", n1 - n2)
elif(escolha == 3):
    print("Produto: ", n1 * n2)
elif(escolha == 4):
    try:
        print("Divisão: ", n1 / n2)
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Numero invalido")
