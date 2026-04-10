n = int(input("Digite um número inteiro: "))

div3 = (n % 3 == 0)
div5 = (n % 5 == 0)

mensagem = (
    div3 * div5 * "Divisível por 3 e por 5\n" +
    div3 * (1 - div5) * "Divisível apenas por 3\n" +
    (1 - div3) * div5 * "Divisível apenas por 5\n" +
    (1 - div3) * (1 - div5) * "Não é divisível por 3 nem por 5\n"
)

print(mensagem)