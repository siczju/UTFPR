media = float(input("Digite a média final do estudante: "))
renda = float(input("Digite a renda familiar mensal: R$ "))
horas = int(input("Digite as horas de serviço comunitário: "))

if renda <= 2500:
    if media >= 8.5:
        elegivel = True
    elif 8.0 <= media < 8.5 and horas >= 30:
        elegivel = True
    else:
        elegivel = False
else:
    elegivel = False

if elegivel:
    print("O estudante é elegível para a bolsa.")
else:
    print("O estudante não é elegível para a bolsa.")