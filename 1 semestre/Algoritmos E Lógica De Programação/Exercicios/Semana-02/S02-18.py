idade = int(input("Digite sua idade: "))
renda = float(input("Digite sua renda mensal: R$ "))
dividas = float(input("Digite o total de dívidas nos últimos 2 anos: R$ "))

if 30 <= idade <= 50 and renda > 10000 and dividas == 0:
    risco_inicial = "Baixo Risco"
elif 25 <= idade <= 60 and 5000 <= renda <= 10000 and dividas < 5000:
    risco_inicial = "Médio Risco"
else:
    risco_inicial = "Alto Risco"

pontuacao = (renda / 1000) - (dividas / 2000) + (idade / 2)

risco_ajustado = risco_inicial

if pontuacao > 80:
    if risco_inicial == "Alto Risco":
        risco_ajustado = "Médio Risco"
    elif risco_inicial == "Médio Risco":
        risco_ajustado = "Baixo Risco"

print(f"Categoria de risco inicial: {risco_inicial}")
print(f"Pontuação de crédito: {pontuacao:.2f}")
print(f"Categoria de risco ajustada: {risco_ajustado}")