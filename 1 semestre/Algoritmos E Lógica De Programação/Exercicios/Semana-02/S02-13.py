salario = float(input("Digite o salário do funcionário: R$ "))

if salario <= 300:
    percentual = 50
elif salario <= 500:
    percentual = 40
elif salario <= 700:
    percentual = 30
elif salario <= 800:
    percentual = 20
elif salario <= 1000:
    percentual = 10
else:
    percentual = 5

aumento = salario * (percentual / 100)
novo_salario = salario + aumento

print(f"Salário original: R$ {salario:.2f}")
print(f"Percentual de aumento: {percentual}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")