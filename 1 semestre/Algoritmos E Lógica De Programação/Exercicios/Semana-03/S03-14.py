n = int(input("Digite um número inteiro N: "))

# Validação simples (N deve ser >= 0)
while n < 0:
    print("Erro: N deve ser maior ou igual a 0.")
    n = int(input("Digite novamente N: "))

fatorial = 1

for i in range(1, n + 1):
    fatorial *= i

print(f"\n{n}! = {fatorial}")