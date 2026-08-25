import os 
os.system('cls')

# Criando um dicionário vazio
contatos = {}

# Adicionando 4 contatos
contatos["Ana"] = "1199999-1111"
contatos["Carlos"] = "1198888-2222"
contatos["Marina"] = "1197777-3333"
contatos["João"] = "1196666-4444"

# Pedindo um nome para busca
nome = input("Digite o nome do contato: ")

# Verificando se o contato existe
if nome in contatos:
    print(f"Telefone de {nome}: {contatos[nome]}")
else:
    print("Contato não encontrado.")

# Exibindo todos os contatos formatados
print("\nLista de contatos:")
for nome, telefone in contatos.items():
    print(f"{nome}: {telefone}")