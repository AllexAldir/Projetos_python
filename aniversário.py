from colorama import Fore
from datetime import date 
# Após receber dia e mês, informe qual o signo correspondente a data informada.

dia = str(input("Digite o dia: "))

mes = str(input("Digite o mês: "))

ano = str(input("Digite o ano: "))

hoje = date.today()

hoje = "{}/{}/{}".format(hoje.day,hoje.month,hoje.year) #Formatação para a data brasileira

# print(type(hoje))

formato = "{}/{}/{}".format(dia,mes,ano)

if formato == hoje:
    print("Seu aniversario!")
else:
    print("k")
