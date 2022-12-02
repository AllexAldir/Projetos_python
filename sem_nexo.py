from colorama import Fore
from datetime import date
import time as ti


repetir = "sim"
cont = 0
lista_senha = []

senha_acesso = input("Digite a senha de acesso da conta: ").capitalize()
lista_senha.append(senha_acesso)

while senha_acesso in lista_senha:
    senha_acesso = input("Não foi possivel identificar a senha no nosso banco de dados.TENTE novamente: ").capitalize()

print("Agora tente ver o nome que você digitar ao contrário!")
ti.sleep(4)

nome = input("Digite o nome: ")

nome_mod = nome.split("")
nome_mod = nome_mod.reverse()
print(nome_mod)

