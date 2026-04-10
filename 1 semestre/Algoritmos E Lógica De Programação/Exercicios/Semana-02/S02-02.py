n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a primeira nota: "))

media = (n1 + n2) / 2

if(media >= 0 and media < 4.0):
    print("Reprovado, média: ", media)
elif(media >= 4 and media < 7):
    print("Exame, média: ", media)
elif(media >= 7 and media <= 10):
    print("Aprovado, média: ", media)
else: 
    print("Valores errados...")

print("Fim do programa...")
