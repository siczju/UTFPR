'''
Faça um programa para calcular e mostrar o salário reajustado de um funcionário. Sabe-se que o percentual de aumento é o mesmo da tabela a seguir:
 
    Salário                                                  Percentual de Aumento
    ------------------------------------------------------------------------------
    Até R$ 300,00                                                   35%
    Acima de R$ 300,00                                              15%
'''
salario = float(input("Digite o salário do funcionário: "))

if(salario <= 300):
    print(f"Salário do funcionario com o aumento de 35%: {salario + salario * 0.35:.2f}")
else:
    print(f"Salário do funcionario com o aumento de 15%: {salario + salario * 0.15:.2f}")