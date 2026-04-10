salario = float(input("Digite o salario fixo: "))
vendas = float(input("Digite o valor das vendas: "))

comissao = vendas * 4 / 100
salario_final = salario + comissao

print("O salario junto com a comissao ficou: ", salario_final)