# 12. Elabore um algoritmo que dada a idade de um nadador classifica-o em uma das seguintes categorias:


# infantil A = 5 - 7 anos

# infantil B = 8-10 anos

# juvenil A = 11-13 anos

# juvenil B = 14-17 anos

# adulto = maiores de 18 anos
from colorama import Fore
def valid_idade(idade):
    if idade >= 5 and idade <= 7:
        x = "infantil A"
        return x
    if idade >= 8 and idade <= 10:
        x = "infantil B"
        return x
    if idade >= 11 and idade <= 13:
        x = "infantil C"
        return x
    if idade >= 14 and idade <= 17:
        x = "infantil D"
        return x
    if idade >= 18:
        x = "Adulto"
        return x
while True:
    idade = int(input("Digite sua idade aqui: "))
    if idade > 125:
        print("Idade maior que 125... ERRO")
    else:
        break
real = valid_idade(idade)
print(Fore.LIGHTMAGENTA_EX + f"A classe da sua idade é: {real}")




