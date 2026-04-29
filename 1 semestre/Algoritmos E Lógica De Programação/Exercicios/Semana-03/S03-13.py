import random

numero_secreto = random.randint(1, 50)
tentativas = 0
max_tentativas = 7

print("Jogo de Adivinhação!")
print("Tente descobrir o número entre 1 e 50.")
print(f"Você tem {max_tentativas} tentativas.\n")

acertou = False

while tentativas < max_tentativas:
    palpite = int(input(f"Tentativa {tentativas + 1}: "))

    # Validação do intervalo
    while palpite < 1 or palpite > 50:
        print("Número inválido! Digite um valor entre 1 e 50.")
        palpite = int(input("Digite novamente: "))

    tentativas += 1

    if palpite == numero_secreto:
        print("\nParabéns! Você acertou o número secreto!")
        acertou = True
        break
    elif palpite < numero_secreto:
        print("Dica: Maior\n")
    else:
        print("Dica: Menor\n")

if not acertou:
    print("\nSuas tentativas acabaram!")
    print(f"O número secreto era: {numero_secreto}")