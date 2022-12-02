# 19. Um usuário deseja um algoritmo onde possa escolher que tipo de média deseja calcular a partir de 3 notas. Faça um algoritmo que leia as notas, a opção escolhida pelo usuário e calcule a média.

# 1 -aritmética
# 2 -ponderada (3,3,4)
# 3 -harmônica
from colorama import Fore

print(Fore.LIGHTCYAN_EX + """
Escolha as opções de números da lista as quais operações de sua escolha
1 -aritmética
2 -ponderada (3,3,4)
""" + Fore.RESET)

def valid_opcao(opcao):
    if opcao == 1:
        x = (nota1+ nota2 + nota3) / 3
        return x
    if opcao == 2:
        x = ((nota1*3) + (nota2*3) + (nota3*4)) / 3 + 3 + 4
        return x


lista_opcao = list(range(1,3))

nota1 = float(input("Digite aqui a sua primeira nota: "))
nota2 = float(input("Digite aqui a sua segunda nota: "))
nota3 = float(input("Digite aqui a sua terceira nota: "))

opcao = int(input("Digite aqui a opção da lista: "))

while opcao not in lista_opcao:
    opcao = int(input("Número não encontrado, Digite aqui a opção da lista: "))

resultado = valid_opcao(opcao)

print(f"Resultado da opção que você escolheu foi {resultado}")
