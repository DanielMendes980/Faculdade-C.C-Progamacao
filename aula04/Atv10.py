import os 
os.system('cls')

# Lista com 4 livros (cada um é um dicionário)
livros = [
    {"titulo": "Python Básico", "autor": "Ana Silva", "ano": 2015, "categorias": ["programação", "tecnologia"]},
    {"titulo": "História do Brasil", "autor": "Carlos Souza", "ano": 2008, "categorias": ["história", "educação"]},
    {"titulo": "IA Moderna", "autor": "Marina Lima", "ano": 2022, "categorias": ["tecnologia", "ciência"]},
    {"titulo": "Matemática Essencial", "autor": "João Pereira", "ano": 2010, "categorias": ["educação", "matemática"]}
]

# Pedindo categoria ao usuário
categoria_busca = input("Digite uma categoria para buscar: ").lower()

# Lista para armazenar resultados da busca
livros_encontrados = []

print("\nLivros encontrados:")

for livro in livros:
    # Verificando se a categoria está no livro
    if categoria_busca in [c.lower() for c in livro["categorias"]]:
        livros_encontrados.append(livro)
        print(f"- {livro['titulo']} ({livro['ano']}) - {livro['autor']}")

# Total de livros
total_livros = len(livros)

# Livro mais antigo e mais recente
livro_mais_antigo = min(livros, key=lambda x: x["ano"])
livro_mais_recente = max(livros, key=lambda x: x["ano"])

# Exibindo resultados gerais
print("\nResumo do catálogo:")
print(f"Total de livros: {total_livros}")
print(f"Livro mais antigo: {livro_mais_antigo['titulo']} ({livro_mais_antigo['ano']})")
print(f"Livro mais recente: {livro_mais_recente['titulo']} ({livro_mais_recente['ano']})")

"""
Resultado
Livros encontrados:

Resumo do catálogo:
Total de livros: 4
Livro mais antigo: História do Brasil (2008)
Livro mais recente: IA Moderna (2022)
"""