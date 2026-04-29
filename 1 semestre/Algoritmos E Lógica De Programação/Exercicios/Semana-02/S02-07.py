'''
 Faça um programa que receba dois números e execute uma das operações listadas a seguir de acordo com a escolha do usuário.
 Se for digitada uma opção inválida mostrar mensagem de erro e terminar a execução do programa. As opções são:
    1)      Média entre os dois números
    2)      Diferença do maior pelo menor
    3)      O produto entre os dois números
'''

numeroParaOperar1 = float(input("Digite o primeiro número da operação: "))
numeroParaOperar2 = float(input("Digite o segundo número da operação: "))

operacaoEscolhida = int(input("\n\t1)      Média entre os dois números" +
                              "\n\t2)      Diferença do maior pelo menor" +
                              "\n\t3)      O produto entre os dois números" +
                              "\nEscolha uma dessas operações: "
                              ))

if(operacaoEscolhida == 1):
    print(f"Média: {(numeroParaOperar1 + numeroParaOperar2) / 2 :.2f}")
elif(operacaoEscolhida == 2):
    if(numeroParaOperar1 > numeroParaOperar2):
        print(f"Diferença do maior pelo menor: {numeroParaOperar1:.2f} - {numeroParaOperar2:.2f} = {numeroParaOperar1 - numeroParaOperar2:.2f}")
    elif(numeroParaOperar2 > numeroParaOperar1):
        print(f"Diferença do maior pelo menor: {numeroParaOperar2:.2f} - {numeroParaOperar1:.2f} = {numeroParaOperar2 - numeroParaOperar1:.2f}")  
    else: 
        print("Os números são iguais: 0")
elif(operacaoEscolhida == 3):
    print(f"Produto: {numeroParaOperar1 * numeroParaOperar2:.2f}")
else:
    print("Escolha inválida")