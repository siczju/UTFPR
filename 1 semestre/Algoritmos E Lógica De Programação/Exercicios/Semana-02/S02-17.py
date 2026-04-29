# Entrada de dados
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário mensal: R$ "))
dividas = float(input("Digite o total de suas dívidas: R$ "))
pagamentos = int(input("Digite o número de pagamentos nos últimos 6 meses: "))

if 25 <= idade <= 60 and salario >= 3000:
    if dividas == 0:
        aprovado = True
    else:
        if dividas <= 0.2 * salario and pagamentos >= 2:
            aprovado = True
        else:
            aprovado = False
else:
    aprovado = False

if aprovado:
    print("Crédito aprovado")
else:
    print("Crédito negado")