cont_50_60 = 0
soma_idade_baixa = 0
cont_altura_baixa = 0
cont_olhos_azuis = 0
cont_ruivos_nao_azuis = 0

for i in range(1, 21):
    print(f"\nPessoa {i}:")
    
    idade = int(input("Idade: "))
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    olhos = input("Cor dos olhos (A/P/V/C): ").upper()
    cabelo = input("Cor do cabelo (P/C/L/R): ").upper()

    # Idade > 50 e peso < 60
    if idade > 50 and peso < 60:
        cont_50_60 += 1

    # Altura < 1.50
    if altura < 1.50:
        soma_idade_baixa += idade
        cont_altura_baixa += 1

    # Olhos azuis
    if olhos == "A":
        cont_olhos_azuis += 1

    # Ruivos e não olhos azuis
    if cabelo == "R" and olhos != "A":
        cont_ruivos_nao_azuis += 1

# Cálculos finais
if cont_altura_baixa > 0:
    media_idade = soma_idade_baixa / cont_altura_baixa
else:
    media_idade = 0

percentual_azuis = (cont_olhos_azuis / 20) * 100

print("\nRESULTADOS:")
print("Quantidade com idade > 50 e peso < 60:", cont_50_60)
print(f"Média das idades (altura < 1,50 m): {media_idade:.2f}")
print(f"Percentagem de olhos azuis: {percentual_azuis:.2f}%")
print("Quantidade de ruivos sem olhos azuis:", cont_ruivos_nao_azuis)