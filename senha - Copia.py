from colorama import Fore
import time as t
#Esquema de acesso

users = []
password = []
repetir = "sim"

while repetir == "sim":
    usuario = input(Fore.LIGHTBLUE_EX + "Digite o nome do usuário: ").lower()

    while usuario in users:
        usuario = input(Fore.LIGHTBLUE_EX + "Usuário ja cadastrado tente outro nome de usário: " + Fore.RESET).lower()

    users.append(usuario)

    while True:
        try:
            password_ = input("Digite sua senha númerica: ")
            password_ = int(password_)
            break

        except:
            print("Não foi possivel identificar esse numeral! tente novamente!")
            t.sleep(2)
        
    password.append(password_)

    repetir = input(Fore.LIGHTMAGENTA_EX + "Deseja repetir a operação? 'sim' ou 'não': " + Fore.RESET).lower()

print("Todas a senhas e usuários criados..")

for u,s in zip(users,password):
    print(f"Usuário: {u}, e sua senha:{s}")