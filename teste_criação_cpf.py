from random import randint
from colorama import Fore
from time import sleep

# cpf testando
while True:

    numero = randint(9999999999, 99999999999) + 1

    cpf = ''.join(str(numero))

    print(Fore.LIGHTMAGENTA_EX + "Gerado CPF: " + Fore.GREEN + cpf)

    sleep(1)
