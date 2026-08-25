

# Entrada: pedir um número
numero = int(input("Digite um número: "))

# Processamento: calcular o dobro
dobro = numero * 2

# Saída: exibir o resultado
print(f"O dobro de {numero} é {dobro}")


### Explicação:
##- Usamos o operador `*` para multiplicar por 2
##- Poderia também ser `numero + numero`
##- Se o usuário digitar decimal, dará erro (use `float()` em vez de `int()`)
