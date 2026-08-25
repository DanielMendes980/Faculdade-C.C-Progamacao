import os 
os.system('cls')
# Criando um dicionário com informações do aluno
aluno ={
    "nome":"luciano",
    "idade":"43",
    "curso":"infermaria",
}
# Exibindo cada informação separadamente
print("Nome:",aluno["nome"])
print("Nome: ",aluno["idade"])
print("Nome: ",aluno["curso"])
"""
resultado esperado:
Nome: luciano
Nome: 43
Nome: infermaria
"""
# Adicionando uma nova chave "nota"
aluno["nota"] = 9.5
# Exibindo o dicionário completo
print("dicionario: ",aluno)
"""
{'nome': 'luciano', 'idade': '43', 'curso': 'infermaria', 'nota': 9.5}       
"""