import os 
os.system('cls')

# Lista com 10 números inteiros
numeros = [1, 4, 7, 10, 13, 16, 19, 22, 25, 30]

# Listas vazias para pares e ímpares
pares = []
impares = []

# Separando os números
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Exibindo as listas
print("Lista de números:", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)