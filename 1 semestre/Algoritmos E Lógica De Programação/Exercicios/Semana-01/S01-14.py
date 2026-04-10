NHT = float(input("Digite o número de horas trabalhadas: "))
SM = float(input("Digite o valor do salário mínimo: "))
NHET = float(input("Digite o número de horas extras: "))

HT = SM / 8
HE = SM / 4

SB = NHT * HT
QR = NHET * HE

SR = SB + QR

print("Valor da hora trabalhada (HT):", HT)
print("Valor da hora extra (HE):", HE)
print("Salário bruto (SB):", SB)
print("Valor das horas extras (QR):", QR)
print("Salário a receber (SR):", SR)