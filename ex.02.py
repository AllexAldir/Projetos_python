# 2. Escreva um algoritmo que leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão:

#  , onde  Image7.gif (19886 bytes)

from colorama import Fore

a = int(input(Fore.LIGHTCYAN_EX + "Digite o 1 número: "))
b = int(input("Digte aqui o 2 número: "))
c = int(input("Digite aqui o 3 número: " + Fore.RESET))

r = (a+b) * (a+b)
s = (b+c) * (b+c)

d = (r + s) / 2

print(f"Resultado da expressão: {d}")