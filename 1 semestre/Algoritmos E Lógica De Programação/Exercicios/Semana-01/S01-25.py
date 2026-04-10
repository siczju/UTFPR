
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
dv_informado = int(input())

soma = (
    a*9 + b*8 + c*7 + d*6 +
    e*5 + f*4 + g*3 + h*2
)

resto = soma % 11

resultado = 11 - resto

dv_calculado = (
    ((resultado == 10) + (resultado == 11)) * 0 +
    ((resultado != 10) * (resultado != 11)) * resultado
)

valido = (dv_calculado == dv_informado)

mensagem = (
    valido * "RG válido\n" +
    (1 - valido) * "RG inválido\n"
)

print(mensagem)