angulo = float(input("Digite o ângulo em graus: "))

# calculo do número de voltas
voltas = int(angulo // 360)

# determinar sentido
if voltas > 0:
    sentido = "anti-horário"
elif voltas < 0:
    sentido = "horário"
else:
    sentido = "nenhum"

# reducao do angulo para o intervalo [0, 360)
angulo_reduzido = angulo % 360

# determinacao do quadrante
if angulo_reduzido == 0 or angulo_reduzido == 90 or angulo_reduzido == 180 or angulo_reduzido == 270:
    quadrante = "Está sobre um eixo (não pertence a um quadrante)"
elif 0 < angulo_reduzido < 90:
    quadrante = "1º quadrante"
elif 90 < angulo_reduzido < 180:
    quadrante = "2º quadrante"
elif 180 < angulo_reduzido < 270:
    quadrante = "3º quadrante"
else:
    quadrante = "4º quadrante"

# saida
print(f"Ângulo original: {angulo}°")
print(f"Voltas completas: {abs(voltas)} ({sentido})")
print(f"Ângulo reduzido: {angulo_reduzido:.2f}°")
print(f"Localização: {quadrante}")