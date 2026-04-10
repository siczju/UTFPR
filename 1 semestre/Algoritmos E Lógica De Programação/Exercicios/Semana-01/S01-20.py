# Entrada
n = int(input("Digite um número inteiro: "))

par = (n % 2 == 0)
impar = (n % 2 != 0)

positivo = (n > 0)
negativo = (n < 0)
zero = (n == 0)

mensagem = (
    par * positivo * "Número par e positivo\n" +
    par * negativo * "Número par e negativo\n" +
    par * zero * "Número par e zero\n" +
    impar * positivo * "Número ímpar e positivo\n" +
    impar * negativo * "Número ímpar e negativo\n" +
    impar * zero * "Número ímpar e zero\n"
)

print(mensagem)