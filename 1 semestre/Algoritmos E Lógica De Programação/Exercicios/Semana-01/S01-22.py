# Entrada
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

ab = (a == b)
bc = (b == c)
ac = (a == c)

todos_iguais = ab * bc  # se a == b e b == c
todos_diferentes = (1 - ab) * (1 - bc) * (1 - ac)
dois_iguais = (ab + bc + ac) * (1 - todos_iguais)

mensagem = (
    todos_iguais * "Todos os dígitos são iguais.\n" +
    todos_diferentes * "Todos os dígitos são diferentes.\n" +
    dois_iguais * "Dois dígitos são iguais.\n"
)

print(mensagem)