#Aqui irei sincronizar as notas dos alunos junto com seus respctivos nomes 
#ao concluir no final irei mostrar a maior nota 

#1 método for.
from colorama import Fore
repetir = 'Sim'
lista_nota = []
lista_nome = []
maior_nota = 0

while repetir == "Sim":
    lista_nome.append(input("Digite aqui o nome do aluno: \n"))
    lista_nota.append(float(input("Digite aqui a nota do aluno: \n")))
    repetir = input("Deseja repetir a operação? 'sim' ou 'não': ").capitalize()
#estrutura com o for utiizando o zip(percorrendo duas listas simultâneamente)
for nome,nota in zip(lista_nome,lista_nota):
    print(f"Nome do aluno: {nome} e sua nota é: {nota}")
    if nota > maior_nota:
        maior_nota = nota
        nome_nota_maior = nome

print(f"""
Resultado da pesquisa:
A maior nota foi do aluno: {nome_nota_maior}
E sua nota foi: {maior_nota}
""")

#2 método utilizando a função index

repetir = 'Sim'
lista_nota = []
lista_nome = []

while repetir == "Sim":
    lista_nome.append(input("Digite aqui o nome do aluno: \n"))
    lista_nota.append(float(input("Digite aqui a nota do aluno: \n")))
    repetir = input("Deseja repetir a operação? 'sim' ou 'não': ").capitalize()

maximo_nota = max(lista_nota)
indec_max_nota = lista_nota.index(maximo_nota)
nome_maior_ = lista_nome[indec_max_nota]

print(f"""
Resultado da pesquisa:
Nome do aluno com maior nota: {nome_maior_}
E sua nota foi: {maximo_nota}
""")
