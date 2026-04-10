n1 = float(input("Digite a primeira nota"))
n2 = float(input("Digite a primeira nota"))
n3 = float(input("Digite a primeira nota"))
n4 = float(input("Digite a primeira nota"))

media = (n1 + n2 + n3 + n4) / 4

if(media >= 6.0):
    print("Aprovado com média: ", media)
else:
    print("Reprovado com média: ", media)

print("Fim do programa...")