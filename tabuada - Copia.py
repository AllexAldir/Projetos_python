from colorama import Fore
import time
num = int(input("Digite um número da tabuada que você quer: "))

while num <0:
    num = int(input("Número menor que '0' tente novamente: "))

for i in range(1,11):
    print(f"{num} x {i} = {num*i}")
    time.sleep(1)
print(Fore.LIGHTCYAN_EX + "Fim da tabuada a qual vocês escolheu" + Fore.RESET)
    

#mostrando todas as tabuadas!

# for i in range(1,11):
#     print(f"Tabuada do {i}")
#     for e in range(1,11):
#         print(f"{i} x {e} = {i*e}")

