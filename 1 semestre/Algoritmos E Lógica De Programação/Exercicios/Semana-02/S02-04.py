n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if(n1 > n2 and n1 > n3):
    print("O primeiro número é o maior")
elif(n2 > n1 and n2 > n3):
    print("O segundo número é o maior")
else:
    print("O terceiro número e o maior")
