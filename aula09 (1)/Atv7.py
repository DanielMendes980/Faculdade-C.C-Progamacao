import os 
os.system('cls')

# Criando o dicionário com disciplinas e notas
disciplinas = {
    "Matemática": [8.0, 7.5, 9.0, 8.5],
    "Português": [7.0, 6.5, 8.0, 7.5],
    "História": [9.0, 8.5, 9.5, 10.0]
}

# Variáveis para armazenar a maior média
maior_media = 0
melhor_disciplina = ""

# Calculando e exibindo a média de cada disciplina
for disciplina, notas in disciplinas.items():
    media = sum(notas) / len(notas)

    print(f"Disciplina: {disciplina}")
    print(f"Média: {media:.2f}")
    print("-" * 30)

    # Verificando a maior média
    if media > maior_media:
        maior_media = media
        melhor_disciplina = disciplina

# Exibindo a disciplina com a maior média
print(f"Disciplina com maior média: {melhor_disciplina}")
print(f"Maior média: {maior_media:.2f}")