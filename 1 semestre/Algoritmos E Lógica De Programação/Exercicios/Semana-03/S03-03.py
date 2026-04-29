def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

inicio = 92
fim = 1478

primos = []
produto = 1

for num in range(inicio, fim + 1):
    if eh_primo(num):
        primos.append(num)
        produto *= num

print("Números primos entre 92 e 1478:")
print(primos)

print("\nProduto dos números primos:")
print(produto)