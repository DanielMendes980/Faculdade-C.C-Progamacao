"""
RGM: 48737534 Nome: DANIEL DA SILVA MENDES
"""

# Lista global de livros
livros = []


def cadastrar_livro():
    """Cadastra um novo livro na biblioteca."""
    print("\n=== CADASTRAR LIVRO ===")

    titulo = input("Título: ")
    autor = input("Autor: ")

    # Verifica duplicado
    for livro in livros:
        if livro["titulo"] == titulo:
            print(f"Erro: Livro '{titulo}' já cadastrado!")
            return

    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "emprestado": False,
        "pessoa": "",
        "historico": []
    }

    livros.append(novo_livro)
    print(f"\nLivro '{titulo}' cadastrado com sucesso!")


def buscar_livro(titulo):
    """Busca um livro pelo título e retorna o dicionário ou None."""
    for livro in livros:
        if livro["titulo"] == titulo:
            return livro
    return None


def emprestar_livro():
    """Empresta um livro disponível para uma pessoa."""
    print("\n=== EMPRESTAR LIVRO ===")

    titulo = input("Título do livro: ")
    livro = buscar_livro(titulo)

    if livro is None:
        print("Erro: Livro não encontrado!")
        return

    if livro["emprestado"]:
        print("Erro: Livro já está emprestado!")
        return

    pessoa = input("Nome da pessoa: ")

    livro["emprestado"] = True
    livro["pessoa"] = pessoa
    livro["historico"].append(pessoa)

    print(f"\nLivro '{titulo}' emprestado para {pessoa}!")


def devolver_livro():
    """Registra a devolução de um livro emprestado."""
    print("\n=== DEVOLVER LIVRO ===")

    titulo = input("Título do livro: ")
    livro = buscar_livro(titulo)

    if livro is None:
        print("Erro: Livro não encontrado!")
        return

    if not livro["emprestado"]:
        print("Erro: Este livro não está emprestado!")
        return

    livro["emprestado"] = False
    livro["pessoa"] = ""

    print(f"\nLivro '{titulo}' devolvido com sucesso!")


def listar_livros():
    """Lista todos os livros cadastrados."""
    print("\n=== BIBLIOTECA - ACERVO ===")

    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return

    print(f"\nTotal: {len(livros)} livro(s)\n")

    for i, livro in enumerate(livros, start=1):
        status = f"Emprestado para {livro['pessoa']}" if livro["emprestado"] else "Disponível"

        print(f"{i}. {livro['titulo']} - {livro['autor']}")
        print(f"Status: {status}\n")


def exibir_estatisticas():
    """Exibe estatísticas da biblioteca."""
    print("\n=== ESTATÍSTICAS DA BIBLIOTECA ===")

    total_livros = len(livros)

    disponiveis = 0
    for livro in livros:
        if not livro["emprestado"]:
            disponiveis += 1

    emprestados = total_livros - disponiveis

    print(f"Total de livros: {total_livros}")
    print(f"Disponíveis: {disponiveis}")
    print(f"Emprestados: {emprestados}")

    if total_livros > 0:
        percentual = (emprestados / total_livros) * 100
        print(f"Percentual emprestado: {percentual:.1f}%")


def exibir_menu():
    print("\n" + "=" * 50)
    print("   SISTEMA DE EMPRÉSTIMOS DE LIVROS")
    print("=" * 50)
    print("1. Cadastrar livro")
    print("2. Emprestar livro")
    print("3. Devolver livro")
    print("4. Listar livros")
    print("5. Exibir estatísticas")
    print("6. Sair")
    print("=" * 50)


# Loop principal
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_livro()

    elif opcao == "2":
        emprestar_livro()

    elif opcao == "3":
        devolver_livro()

    elif opcao == "4":
        listar_livros()

    elif opcao == "5":
        exibir_estatisticas()

    elif opcao == "6":
        print("Saindo do sistema... Até mais!")
        break

    else:
        print("Opção inválida!")