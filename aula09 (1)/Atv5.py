import os 
os.system('cls')
# Criando uma lista com 3 dicionários de produtos
produtos = [
    {"nome": "Notebook", "preco": 3500.00, "quantidade": 2},
    {"nome": "Mouse", "preco": 80.00, "quantidade": 5},
    {"nome": "Teclado", "preco": 150.00, "quantidade": 3}
]
# Variável para armazenar o valor total do estoque
total_estoque = 0

# Percorrendo a lista de produtos
for produto in produtos:
    nome = produto["nome"]
    preco = produto["preco"]
    quantidade = produto["quantidade"]

 # Exibindo os dados formatados
    print(f"Produto: {nome}")
    print(f"Preço: R$ {preco:.2f}")
    print(f"Quantidade: {quantidade}")
    print("-" * 30)

        # Calculando o valor total do estoque
    total_estoque += preco * quantidade

# Exibindo o valor total do estoque
print(f"Valor total do estoque: R$ {total_estoque:.2f}")

"""
Resultado
Produto: Notebook
Preço: R$ 3500.00
Quantidade: 2
------------------------------
Produto: Mouse
Preço: R$ 80.00
Quantidade: 5
------------------------------
Produto: Teclado
Preço: R$ 150.00
Quantidade: 3
------------------------------
Valor total do estoque: R$ 7850.00
"""