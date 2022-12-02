import matplotlib.pyplot as plt         #Biblioteca de gráficos
from colorama import Fore               #Biblioteca de cores

meses = []
vendas = []

for i in range(0,12):
    meses.append(input(Fore.LIGHTCYAN_EX + "Dgite o mês da venda: " + Fore.RESET))
    vendas.append(float(input(f"Digite o valor das vendas do mês {meses[i]}: ")))

plt.plot(meses, vendas, label="Dados dos meses", color= "#150C6B")          #Gráfico comum
plt.title("Relatório de vendas")                                            #Titulo do gráfico
plt.xlabel("Meses do ano")                                    
plt.ylabel("Vendas do ano")
plt.legend()
plt.show()
