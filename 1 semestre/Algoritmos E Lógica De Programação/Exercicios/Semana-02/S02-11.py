salario = float(input("Digite o salário do funcionário: R$ "))

if salario <= 300:
    percentual = 15
elif salario <= 600:
    percentual = 10
elif salario <= 900:
    percentual = 5
else:
    percentual = 0

aumento = salario * (percentual / 100)
novo_salario = salario + aumento

print(f"Salário original: R$ {salario:.2f}")
print(f"Percentual de aumento: {percentual}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")