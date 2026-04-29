idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário mensal: "))
dependentes = int(input("Digite o número de dependentes: "))

if idade < 18 or salario < 1500 or dependentes > 5:
    print("Crédito Negado")
    print("Crédito negado: requisitos não atendidos.")

elif idade > 25 and salario > 3000 and dependentes <= 3:
    print("Crédito Aprovado")
    print("Crédito liberado com sucesso!")

elif (18 <= idade <= 25 and 1500 <= salario <= 3000) or \
     (idade > 25 and dependentes <= 3 and 1500 <= salario <= 2500):
    print("Crédito Parcialmente Aprovado")
    print("Crédito limitado: análise adicional necessária.")

else:
    print("Crédito Negado")
    print("Crédito negado: requisitos não atendidos.")