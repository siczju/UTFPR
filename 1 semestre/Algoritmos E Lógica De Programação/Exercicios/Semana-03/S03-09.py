cont_idade50 = 0
soma_altura_10_20 = 0
cont_10_20 = 0
cont_peso40 = 0

for i in range(1, 26):
    print(f"\nPessoa {i}:")
    
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura (em metros): "))
    peso = float(input("Digite o peso (em kg): "))

    # Pessoas com idade superior a 50 anos
    if idade > 50:
        cont_idade50 += 1

    # Alturas entre 10 e 20 anos
    if 10 <= idade <= 20:
        soma_altura_10_20 += altura
        cont_10_20 += 1

    # Pessoas com peso inferior a 40 kg
    if peso < 40:
        cont_peso40 += 1

# Cálculos finais
if cont_10_20 > 0:
    media_altura = soma_altura_10_20 / cont_10_20
else:
    media_altura = 0

percentual_peso40 = (cont_peso40 / 25) * 100

print("\nRESULTADOS:")
print("Quantidade de pessoas com mais de 50 anos:", cont_idade50)
print(f"Média das alturas (10 a 20 anos): {media_altura:.2f} m")
print(f"Percentual com peso inferior a 40 kg: {percentual_peso40:.2f}%")