nomes = []
medias = []

for i in range(7):
    nome = input("Digite o nome do aluno: ")
    media = float(input("Digite a média final: "))

    nomes.append(nome)
    medias.append(media)

maior_media = medias[0]
indice_maior = 0

for i in range(1, 7):
    if medias[i] > maior_media:
        maior_media = medias[i]
        indice_maior = i
        
print("\nAluno com maior média:")
print(nomes[indice_maior], "-", maior_media)

print("\nAlunos que precisam de exame:")
for i in range(7):
    if medias[i] < 7.0:
        # cálculo da nota necessária no exame
        exame = 10 - medias[i]

        print(nomes[i], "precisa tirar", exame, "no exame")