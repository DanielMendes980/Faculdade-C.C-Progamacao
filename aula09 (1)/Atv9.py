import os 
os.system('cls')

# Lista com 3 vendas
vendas = [
    {"produto": "Notebook", "quantidade": 2, "valor_unitario": 3500.00},
    {"produto": "Mouse", "quantidade": 5, "valor_unitario": 80.00},
    {"produto": "Teclado", "quantidade": 3, "valor_unitario": 150.00}
]

# Variável para armazenar o total geral
total_geral = 0

# Percorrendo as vendas
for venda in vendas:
    produto = venda["produto"]
    quantidade = venda["quantidade"]
    valor_unitario = venda["valor_unitario"]

    # Calculando o total da venda
    total_venda = quantidade * valor_unitario

    # Somando ao total geral
    total_geral += total_venda

    # Exibindo os dados da venda
    print(f"Produto: {produto}")
    print(f"Quantidade: {quantidade}")
    print(f"Valor unitário: R$ {valor_unitario:.2f}")
    print(f"Total da venda: R$ {total_venda:.2f}")
    print("-" * 30)

# Exibindo o total geral
print(f"Total geral das vendas: R$ {total_geral:.2f}")

"""
Resultado
Produto: Notebook
Quantidade: 2
Valor unitário: R$ 3500.00
Total da venda: R$ 7000.00
------------------------------
Produto: Mouse
Quantidade: 5
Valor unitário: R$ 80.00
Total da venda: R$ 400.00
------------------------------
Produto: Teclado
Quantidade: 3
Valor unitário: R$ 150.00
Total da venda: R$ 450.00
------------------------------
Total geral das vendas: R$ 7850.00
"""