a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
i = int(input())
j = int(input())  
k = int(input()) 

soma1 = (
    a*10 + b*9 + c*8 + d*7 + e*6 +
    f*5 + g*4 + h*3 + i*2
)

resto1 = soma1 % 11

d1 = (resto1 < 2) * 0 + (resto1 >= 2) * (11 - resto1)

soma2 = (
    a*11 + b*10 + c*9 + d*8 + e*7 +
    f*6 + g*5 + h*4 + i*3 + d1*2
)

resto2 = soma2 % 11

d2 = (resto2 < 2) * 0 + (resto2 >= 2) * (11 - resto2)

valido = (d1 == j) * (d2 == k)

mensagem = (
    valido * "CPF válido\n" +
    (1 - valido) * "CPF inválido\n"
)

print(mensagem)