# =========================
# FUNÇÕES DE VALIDAÇÃO
# =========================

def ler_inteiro(msg):
    """Valida e retorna um número inteiro digitado pelo usuário."""
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um número inteiro válido!")


def ler_texto(msg):
    """Valida e retorna um texto não vazio."""
    while True:
        texto = input(msg).strip()
        if texto != "":
            return texto
        print("O campo não pode ser vazio!")


# =========================
# ATIVIDADES DO MENU
# =========================

def frutas():
    """Cria uma lista de frutas e exibe informações básicas."""
    frutas = ['maçã', 'banana', 'laranja', 'uva', 'morango']

    print("\nLista de frutas:", frutas)
    print("Primeira fruta:", frutas[0])
    print("Última fruta:", frutas[-1])
    print("Total de frutas:", len(frutas))


def tarefas():
    """Cria lista de tarefas, adiciona e remove itens."""
    tarefas = []

    tarefas.append("Estudar Python")
    tarefas.append("Fazer exercícios")
    tarefas.append("Ler livro")

    print("\nTarefas:", tarefas)

    tarefas.remove("Estudar Python")

    print("Após remoção:", tarefas)


def aluno():
    """Cria um dicionário de aluno e adiciona nota."""
    aluno = {
        "nome": "Carlos",
        "idade": 20,
        "curso": "Python"
    }

    print("\nNome:", aluno["nome"])
    print("Idade:", aluno["idade"])
    print("Curso:", aluno["curso"])

    aluno["nota"] = 9.0

    print("Aluno completo:", aluno)


def tupla_coordenadas():
    """Trabalha com tupla de coordenadas e demonstra imutabilidade."""
    coordenadas = (10, 20, 30)

    print("\nX:", coordenadas[0])
    print("Y:", coordenadas[1])
    print("Z:", coordenadas[2])

    novas = (40, 50, 60)
    print("Nova tupla:", novas)


def produtos_estoque():
    """Calcula valor total de estoque de produtos."""
    produtos = [
        {"nome": "Notebook", "preco": 3500.0, "quantidade": 2},
        {"nome": "Mouse", "preco": 80.0, "quantidade": 5},
        {"nome": "Teclado", "preco": 150.0, "quantidade": 3}
    ]

    total = 0

    print("\n--- ESTOQUE ---")
    for p in produtos:
        valor = p["preco"] * p["quantidade"]
        total += valor

        print(f"{p['nome']} - Total: R$ {valor:.2f}")

    print("Total do estoque:", total)


def pares_impares():
    """Separa números em pares e ímpares."""
    numeros = [1,2,3,4,5,6,7,8,9,10]

    pares = []
    impares = []

    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)

    print("\nNúmeros:", numeros)
    print("Pares:", pares)
    print("Ímpares:", impares)


def media_disciplinas():
    """Calcula média de disciplinas e mostra a maior média."""
    disciplinas = {
        "Matemática": [8, 7, 9, 10],
        "Português": [7, 6, 8, 7],
        "História": [9, 9, 10, 8]
    }

    maior = 0
    melhor = ""

    print("\n--- MÉDIAS ---")
    for d, notas in disciplinas.items():
        media = sum(notas) / len(notas)
        print(f"{d}: {media:.2f}")

        if media > maior:
            maior = media
            melhor = d

    print("Maior média:", melhor)


def contatos():
    """Gerencia contatos e permite busca."""
    contatos = {
        "Ana": "1111-1111",
        "Carlos": "2222-2222",
        "Maria": "3333-3333",
        "João": "4444-4444"
    }

    nome = ler_texto("Digite o nome para buscar: ")

    if nome in contatos:
        print("Telefone:", contatos[nome])
    else:
        print("Contato não encontrado.")

    print("\nContatos:")
    for n, t in contatos.items():
        print(f"{n}: {t}")


def vendas():
    """Calcula total de vendas de uma lista de dicionários."""
    vendas = [
        {"produto": "Notebook", "qtd": 2, "valor": 3500},
        {"produto": "Mouse", "qtd": 5, "valor": 80},
        {"produto": "Teclado", "qtd": 3, "valor": 150}
    ]

    total_geral = 0

    print("\n--- VENDAS ---")
    for v in vendas:
        total = v["qtd"] * v["valor"]
        total_geral += total

        print(f"{v['produto']} - Total: R$ {total:.2f}")

    print("Total geral:", total_geral)


def livros():
    """Filtra livros por categoria e calcula estatísticas."""
    livros = [
        {"titulo": "Python Básico", "ano": 2015, "categorias": ["tecnologia"]},
        {"titulo": "História Brasil", "ano": 2008, "categorias": ["história"]},
        {"titulo": "IA Moderna", "ano": 2022, "categorias": ["tecnologia"]},
        {"titulo": "Matemática", "ano": 2010, "categorias": ["educação"]}
    ]

    cat = ler_texto("Digite categoria: ").lower()

    print("\nLivros encontrados:")
    for l in livros:
        if cat in [c.lower() for c in l["categorias"]]:
            print(l["titulo"])

    mais_antigo = min(livros, key=lambda x: x["ano"])
    mais_novo = max(livros, key=lambda x: x["ano"])

    print("Mais antigo:", mais_antigo["titulo"])
    print("Mais recente:", mais_novo["titulo"])


# =========================
# MENU PRINCIPAL
# =========================

while True:
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Frutas")
    print("2 - Tarefas")
    print("3 - Aluno")
    print("4 - Tupla Coordenadas")
    print("5 - Estoque de Produtos")
    print("6 - Pares e Ímpares")
    print("7 - Médias de Disciplinas")
    print("8 - Contatos")
    print("9 - Vendas")
    print("10 - Livros")
    print("0 - Sair")

    opcao = ler_inteiro("Escolha: ")

    if opcao == 1:
        frutas()
    elif opcao == 2:
        tarefas()
    elif opcao == 3:
        aluno()
    elif opcao == 4:
        tupla_coordenadas()
    elif opcao == 5:
        produtos_estoque()
    elif opcao == 6:
        pares_impares()
    elif opcao == 7:
        media_disciplinas()
    elif opcao == 8:
        contatos()
    elif opcao == 9:
        vendas()
    elif opcao == 10:
        livros()
    elif opcao == 0:
        print("Saindo...")
        break
    else:
        print("Opção inválida!")