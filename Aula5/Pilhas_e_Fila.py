# Variáveis globais para as estruturas de dados
fila_atendimento = []  # Fila FIFO para clientes
pilha_documentos = []  # Pilha LIFO para documentos

# Variáveis globais para controle
total_atendimentos = 0  # Contador de atendimentos realizados
total_documentos_processados = 0  # Contador de documentos processados


def adicionar_cliente_fila():
    """
    Descreva com suas palavras o que esta função faz:
    função soçicita o nome do cliente e o adiciona
    ao final da fila de atendimento
    """
    print("\n=== ADICIONAR CLIENTE NA FILA ===")
    # Armazene na variável local 'nome_cliente'
    nome_cliente = input("Qual é o nome do cliente: ")
    print(f"Cliente {nome_cliente} adicionado na posição 2 da fila")
    print(len(fila_atendimento))
    # Use: fila_atendimento.append(nome_cliente)
    fila_atendimento.append(nome_cliente)
    # A posição é o tamanho da fila (len(fila_atendimento))
    posicao = len(fila_atendimento)
    print(f"\nCliente '{nome_cliente}' adicionado na posição {posicao} da fila.")
    print(f"Total de clientes aguardando: {len(fila_atendimento)}")


def atender_cliente_fila():
    """
    Descreva com suas palavras o que esta função faz:
    verifica se há clientes na fila e realiza o atendimento do primeiro clinte
    o removendo da fila e  atualizando o contador de atendimento
    """
    # Declare que irá modificar a variável global
    global total_atendimentos

    print("\n=== ATENDER CLIENTE ===")
    # Se len(fila_atendimento) == 0, exiba mensagem e retorne
    if len(fila_atendimento) == 0:
        print("\nNenhum cliente na fila.")
        return

    # Remova o PRIMEIRO cliente da fila
    cliente_atendido = fila_atendimento.pop(0)
    total_atendimentos += 1

    # Exiba as informações do atendimento
    print(f"\nAtendendo cliente: {cliente_atendido}")
    print(f"Total de atendimentos realizados: {total_atendimentos}")
    print(f"Clientes restantes na fila: {len(fila_atendimento)}")


def visualizar_fila():
    """
    Descreva com suas palavras o que esta função faz:
    exibe todos os clientes que estão aguardando
    atendimento na fila, mostrando suas posições e indicando
    qual será o próximo cliente atendido.
    """
    print("\n=== FILA DE ATENDIMENTO ===")

    # Verifique se a fila está vazia
    if len(fila_atendimento) == 0:
        print("\nNenhum cliente na fila.")
        return

    # Exiba o total de clientes
    print(f"\nTotal de clientes aguardando: {len(fila_atendimento)}\n")

    # Percorra a fila e exiba cada cliente com sua posição
    for i in range(len(fila_atendimento)):
        # Acesse o cliente usando: fila_atendimento[i]
        print(f"Posição {i+1}: {fila_atendimento[i]}")

    # Exiba qual cliente será atendido primeiro
    print(f"\nPróximo a ser atendido: {fila_atendimento[0]}")


def adicionar_documento_pilha():
    """
    Descreva com suas palavras o que esta função faz:
    função exibe todos os clientes presentes na fila de atendimento,
    mostrando a posição de cada um e indicando qual será o próximo a ser atendido
    """
    print("\n=== ADICIONAR DOCUMENTO NA PILHA ===")

    # Solicite o nome do documento
    nome_documento = input("Adicione um nome a o documento: ")

    # Adicione o documento no TOPO da pilha
    pilha_documentos.append(nome_documento)

    # Tarefa 3: Exiba confirmação
    print(f"\nDocumento '{nome_documento}' adicionado no topo da pilha.")
    print(f"Total de documentos na pilha: {len(pilha_documentos)}")


def processar_documento_pilha():
    """
    Descreva com suas palavras o que esta função faz:
    verifica se há documentos na pilha e, caso existam,
    remove o documento do topo (último a entrar) para processamento
    """
    # Declare que irá modificar a variável global
    global total_documentos_processados

    print("\n=== PROCESSAR DOCUMENTO ===")

    # Verifique se a pilha está vazia
    if len(pilha_documentos) == 0:
        print("\nNenhum documento na pilha para processar.")
        return

    # Remova o documento do TOPO da pilha
    documento_processado = pilha_documentos.pop()

    # Incremente o contador global
    total_documentos_processados += 1

    # Exiba as informações
    print(f"\nDocumento processado: {documento_processado}")
    print(f"Total de documentos processados: {total_documentos_processados}")
    print(f"Documentos restantes na pilha: {len(pilha_documentos)}")


def visualizar_pilha():
    """
    Descreva com suas palavras o que esta função faz:
    exibe todos os documentos armazenados na pilha,
    mostrando a ordem do topo até a base e indicando qual será
    o próximo documento a ser processado
    """
    print("\n=== PILHA DE DOCUMENTOS ===")

    # Verifique se a pilha está vazia
    if len(pilha_documentos) == 0:
        print("\nNenhum documento na pilha.")
        return

    # Exiba o total de documentos
    print(f"\nTotal de documentos na pilha: {len(pilha_documentos)}\n")

    # Exiba os documentos do TOPO para a BASE
    # Percorra de trás para frente usando range reverso
    # Use: for i in range(len(pilha_documentos) - 1, -1, -1):
    print("Pilha (do topo para a base):")

    for i in range(len(pilha_documentos) - 1, -1, -1):
        # Exiba cada documento
        # Marque o topo com uma seta
        if i == len(pilha_documentos) - 1:
            print(f"  [TOPO] -> {pilha_documentos[i]}")
        else:
            print(f"            {pilha_documentos[i]}")

    # Exiba qual documento será processado primeiro
    print(f"\nPróximo a ser processado: {pilha_documentos[-1]}")


def exibir_estatisticas():
    """
    Descreva com suas palavras o que esta função faz
    Exibe cada documento do topo até a base depois
    exibe qual documento será processado primeiro
    """
    print("\n=== ESTATÍSTICAS DO SISTEMA ===")

    # Variáveis locais para cálculos
    clientes_aguardando = len(fila_atendimento)
    documentos_pendentes = len(pilha_documentos)
    total_operacoes = total_atendimentos + total_documentos_processados

    # Exiba as estatísticas
    print(f"\n--- Fila de Atendimento ---")
    print(f"Clientes aguardando: {clientes_aguardando}")
    print(f"Total de atendimentos realizados: {total_atendimentos}")

    print(f"\n--- Pilha de Documentos ---")
    print(f"Documentos pendentes: {documentos_pendentes}")
    print(f"Total de documentos processados: {total_documentos_processados}")

    print(f"\n--- Geral ---")
    print(f"Total de operações realizadas: {total_operacoes}")

    # Calcule e exiba a taxa de ocupação (variável local)
    # Taxa = (clientes + documentos) / capacidade máxima (exemplo: 20)

    taxa = (clientes_aguardando + documentos_pendentes) / 20 * 100
    print(f"Taxa de ocupação do sistema: {taxa:.1f}%")


def exibir_menu():
    """
    Descreva com suas palavras o que esta função faz:
    exibe o menu principal do sistema de atendimento,
    mostrando todas as opções disponíveis para o usuário interagir,
    como adicionar clientes, atender clientes, manipular documentos
    e visualizar informações do sistema.
    """
    print("\n" + "=" * 50)
    print("    SISTEMA DE ATENDIMENTO - FILAS E PILHAS")
    print("=" * 50)
    print("1. Adicionar cliente na fila")
    print("2. Atender próximo cliente")
    print("3. Visualizar fila de atendimento")
    print("4. Adicionar documento na pilha")
    print("5. Processar documento do topo")
    print("6. Visualizar pilha de documentos")
    print("7. Exibir estatísticas")
    print("8. Sair")
    print("=" * 50)


# Loop principal do programa
while True:
    # Chame a função exibir_menu()
    exibir_menu()

    # Capture a opção do usuário
    opcao = input("Escolha uma opção: ")

    # Implemente a estrutura if/elif/else
    if opcao == "1":
        adicionar_cliente_fila()

    elif opcao == "2":
        atender_cliente_fila()
        pass

    elif opcao == "3":
        visualizar_fila()
        pass

    elif opcao == "4":
        adicionar_documento_pilha()
        pass

    elif opcao == "5":
        processar_documento_pilha()
        pass

    elif opcao == "6":
        visualizar_pilha()
        pass

    elif opcao == "7":
        exibir_estatisticas()
        pass

    elif opcao == "8":
        print("\nEncerrando o sistema. Até logo!")
        break

    else:
        print("\nOpção inválida! Tente novamente.")