'''
 Uma empresa decide dar um aumento de 30% aos  funcionários com salários inferiores a R$ 500,00.
 Faça um programa que receba o salário do funcionário e mostre o valor do salário reajustado ou uma mensagem,
 caso o funcionário não tenha direito ao aumento.
'''

salario = float(input("Digite o salário do funcionário: "))

if(salario < 500):
    salario += salario * 0.3
    print(f"O salario é menor que 500, com o aumento ficou {salario:.2f}")
else:
    print(f"O salario é maior que 500, sem direito a aumento de 30%, é {salario:.2f}")